"""Local, read-only MCP catalog with an optional MCP Apps UI; no model API."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated, Literal

from mcp.server.fastmcp import FastMCP
from mcp.types import ResourceLink, ToolAnnotations
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
UI_URI = "ui://chem-skill-panel/panel-v1.html"
SkillName = Annotated[str, Field(description="Exact name from this plugin's catalog; unknown names are rejected.")]
ANNOTATIONS = ToolAnnotations(readOnlyHint=True, destructiveHint=False,
                              idempotentHint=True, openWorldHint=False)


class SkillSource(BaseModel):
    name: str
    url: str


class SkillEntry(BaseModel):
    name: str
    title: str
    summary: str
    example_prompt: str
    source: SkillSource


class PanelSnapshot(BaseModel):
    package: str
    version: str
    skills: list[SkillEntry]
    status: Literal["catalog_only"] = "catalog_only"
    browser_panel: str


class PreparedTask(BaseModel):
    skill_name: str
    title: str
    prompt: str
    status: Literal["prepared"] = "prepared"


class SkillInstructions(BaseModel):
    skill_name: str
    title: str
    instructions: str
    skill_directory: str
    status: Literal["instructions_loaded"] = "instructions_loaded"


class MentionResults(BaseModel):
    items: list[ResourceLink]


def catalog() -> dict:
    return json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))


def entry(skill_name: str) -> dict:
    for item in catalog()["skills"]:
        if item["name"] == skill_name:
            return item
    raise ValueError("Unknown bundled skill")


def make_prompt(skill_name: str, task: str) -> str:
    item = entry(skill_name)
    task = task.strip()
    if not task or len(task) > 12000:
        raise ValueError("任务须为 1–12000 个字符。")
    return (
        f"请使用 chem-skill-panel 插件中的「{item['title']}」（{skill_name}）。\n"
        "先读取该技能的完整 SKILL.md 和本次需要的资源；已连接插件时可调用 "
        "get_skill_instructions。按我给定的范围开展工作，并区分已完成与尚未核验的内容。\n\n"
        f"我的任务：\n{task}"
    )


mcp = FastMCP("chem-skill-panel", instructions=(
    "This server lists bundled research skills, prepares task text, and reads their instructions. "
    "It never executes research, installs skills, or sends messages. Use open_skill_panel for a "
    "menu request. Read the selected skill before performing the user's research task."
))


@mcp.resource(UI_URI, name="chem-skill-panel", title="化学科研技能面板",
              mime_type="text/html;profile=mcp-app")
def panel_html() -> str:
    return (ROOT / "assets/panel.html").read_text(encoding="utf-8")


@mcp.tool(title="打开化学科研技能面板", annotations=ANNOTATIONS,
          meta={"ui": {"resourceUri": UI_URI},
                "openai/ui": {"entrypoints": [{"type": "thread"}]},
                "openai/outputTemplate": UI_URI})
def open_skill_panel() -> PanelSnapshot:
    """Show the bundled skill picker. Only returns a catalog; does not start research."""
    data = catalog()
    return PanelSnapshot(package=data["package"], version=data["version"],
                         skills=data["skills"], browser_panel=str(ROOT / "assets/panel.html"))


@mcp.tool(title="搜索科研技能", annotations=ANNOTATIONS,
          meta={"ui": {"visibility": ["app"]},
                "openai/extensions": {"mentions/search": {}}})
def search_skill_mentions(query: str) -> MentionResults:
    """Find Chinese skill names for the native composer picker; an empty query lists all."""
    query = query.strip().casefold()
    return MentionResults(items=[
        ResourceLink(type="resource_link", uri=f"chem-skill://skills/{item['name']}",
                     name=item["name"], title=item["name"],
                     description=f"{item['title']}：{item['summary']} 来源：{item['source']['name']}", mimeType="text/markdown")
        for item in catalog()["skills"]
        if query in " ".join([item["name"], item["title"], item["summary"], item["source"]["name"]]).casefold()
    ])


@mcp.resource("chem-skill://skills/{skill_name}", mime_type="text/markdown")
def mentioned_skill(skill_name: str) -> str:
    item = entry(skill_name)
    return (ROOT / "skills" / item["name"] / "SKILL.md").read_text(encoding="utf-8")


@mcp.tool(title="准备技能调用指令", annotations=ANNOTATIONS,
          meta={"ui": {"visibility": ["model", "app"]}})
def prepare_skill_task(skill_name: SkillName,
                       task: Annotated[str, Field(min_length=1, max_length=12000)]) -> PreparedTask:
    """Prepare a user-selected skill invocation. Does not run the task or send a message."""
    return PreparedTask(skill_name=skill_name, title=entry(skill_name)["title"],
                        prompt=make_prompt(skill_name, task))


@mcp.tool(title="读取所选技能原文", annotations=ANNOTATIONS)
def get_skill_instructions(skill_name: SkillName) -> SkillInstructions:
    """Read one bundled SKILL.md so the host can follow it for the user's task."""
    item = entry(skill_name)
    directory = ROOT / "skills" / item["name"]
    return SkillInstructions(skill_name=skill_name, title=item["title"],
                             instructions=(directory / "SKILL.md").read_text(encoding="utf-8"),
                             skill_directory=str(directory))


if __name__ == "__main__":
    mcp.run(transport="stdio")
