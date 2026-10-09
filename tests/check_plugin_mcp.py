"""Exercise the real stdio server through the official MCP Python client."""
import json
import sys
from pathlib import Path

import anyio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def check(root):
    parameters = StdioServerParameters(command=sys.executable, args=[str(root / "scripts/server.py")])
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as client:
            await client.initialize()
            tools = {t.name: t for t in (await client.list_tools()).tools}
            assert set(tools) == {"open_skill_panel", "prepare_skill_task", "get_skill_instructions", "search_skill_mentions"}
            assert all(t.outputSchema and t.annotations.readOnlyHint for t in tools.values())
            assert tools["search_skill_mentions"].meta["openai/extensions"] == {"mentions/search": {}}
            assert tools["search_skill_mentions"].meta["ui"]["visibility"] == ["app"]
            uri = tools["open_skill_panel"].meta["ui"]["resourceUri"]
            panel = (await client.read_resource(uri)).contents[0]
            assert panel.mimeType == "text/html;profile=mcp-app"
            assert "__CHEM_CATALOG_JSON__" not in panel.text
            result = await client.call_tool("open_skill_panel", {})
            assert not result.isError
            assert result.structuredContent["status"] == "catalog_only"
            skills = result.structuredContent["skills"]
            mentions = await client.call_tool("search_skill_mentions", {"query": ""})
            assert len(mentions.structuredContent["items"]) == len(skills)
            for item, skill in zip(mentions.structuredContent["items"], skills):
                assert item["name"] == skill["name"]
                assert skill["source"]["name"] in item["description"]
                original = (root / "skills" / skill["name"] / "SKILL.md").read_text(encoding="utf-8")
                resource = (await client.read_resource(item["uri"])).contents[0]
                assert resource.text == original
            filtered = await client.call_tool("search_skill_mentions", {"query": "参考文献"})
            assert len(filtered.structuredContent["items"]) == 1
            assert filtered.structuredContent["items"][0]["uri"] == "chem-skill://skills/ref-check"
            missing = await client.call_tool("search_skill_mentions", {"query": "nonexistent"})
            assert missing.structuredContent["items"] == []
            try:
                await client.read_resource("chem-skill://skills/unknown-skill")
            except Exception:
                pass
            else:
                raise AssertionError("Unknown mention resource was accepted")
            for skill in skills:
                loaded = await client.call_tool("get_skill_instructions", {"skill_name": skill["name"]})
                assert not loaded.isError
                assert loaded.structuredContent["instructions"] == (root / "skills" / skill["name"] / "SKILL.md").read_text(encoding="utf-8")
            task = '核验输入：C:\\研究\\references.bib；不要执行 $(echo surprise) 或 <script>。'
            prepared = await client.call_tool("prepare_skill_task", {"skill_name": "ref-check", "task": task})
            assert prepared.structuredContent["status"] == "prepared"
            assert prepared.structuredContent["prompt"].endswith(task)
            for name in ["../../catalog.json", "uninstalled-example-skill", "not-a-skill"]:
                failure = await client.call_tool("get_skill_instructions", {"skill_name": name})
                assert failure.isError
            for task in [" ", "x" * 12001]:
                failure = await client.call_tool("prepare_skill_task", {"skill_name": "ref-check", "task": task})
                assert failure.isError
    print(json.dumps({"stdio_mcp": "passed", "tools": len(tools), "bundled_skills": len(skills),
                      "resource": "passed", "input_rejections": 5}))


if __name__ == "__main__":
    anyio.run(check, Path(sys.argv[1]).resolve())
