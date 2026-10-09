"""Chromium interaction checks; the embedded host is a test double, not Codex."""
import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

root = Path(sys.argv[1]).resolve()
html = (root / "assets/panel.html").read_text(encoding="utf-8")
catalog = json.loads((root / "catalog.json").read_text())["skills"]
names = [entry["name"] for entry in catalog]
output = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else None

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 660, "height": 760}, color_scheme="light")
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto((root / "assets/panel.html").as_uri())
    expect(page.locator(".skill")).to_have_count(len(names))
    expect(page.locator(".title")).to_have_text(names)
    expect(page.locator(".source a")).to_have_count(sum(bool(entry["source"]["url"]) for entry in catalog))
    for link in page.locator(".source a").all():
        assert link.get_attribute("href").startswith("https://github.com/")
        assert "/blob/" in link.get_attribute("href")
        assert link.get_attribute("href").endswith("/SKILL.md")
    page.locator("#search").fill("paper-lookup")
    expect(page.locator(".skill")).to_have_count(1)
    expect(page.locator(".title")).to_have_text("paper-lookup")
    assert page.locator("textarea,form").count() == 0
    page.locator("#search").fill("ref-check")
    expect(page.locator(".skill")).to_have_count(1)
    # Clipboard success and refusal both preserve a paste-only workflow.
    page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async t=>{window.copied=t}}})")
    page.get_by_role("button", name="复制ref-check").click()
    expect(page.locator("#status")).to_contain_text("已复制")
    assert "ref-check" in page.evaluate("copied")
    page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw Error('denied')}}})")
    page.get_by_role("button", name="复制ref-check").click()
    expect(page.locator("#manual")).to_be_visible()
    expect(page.locator("#status")).to_contain_text("Ctrl+C")
    assert "ref-check" in page.locator("#manual").input_value()
    page.locator("#search").fill("no-match")
    expect(page.locator("#empty")).to_be_visible()
    page.locator("#search").fill("")
    page.set_viewport_size({"width": 390, "height": 844})
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
    page.emulate_media(color_scheme="dark")
    expect(page.locator(".skill")).to_have_count(len(names))
    page.emulate_media(color_scheme="light")
    page.set_viewport_size({"width": 660, "height": 760})

    page.set_content('<iframe id="panel" style="width:100%;height:740px;border:0"></iframe>')
    page.evaluate('''() => {
      window.requests=[];window.contexts=[];window.fail=false;window.delay=0;
      window.caps={updateModelContext:{text:{}},experimental:{'openai/modelContext':{}}};
      addEventListener('message', event => {
        if(event.source!==document.querySelector('iframe').contentWindow)return;
        const m=event.data;if(!m?.id)return;
        window.requests.push(m);
        if(m.method==='ui/initialize'){
          event.source.postMessage({jsonrpc:'2.0',id:m.id,result:{protocolVersion:'2026-01-26',hostCapabilities:window.caps,hostContext:{}}},'*');
        }else if(m.method==='ui/update-model-context'){
          if(!window.fail)window.contexts.push(m.params);
          const reply=window.fail?{error:{code:-32601,message:'unsupported'}}:{result:{_meta:{'openai/modelContext':{updateId:'test-id'}}}};
          setTimeout(()=>event.source.postMessage({jsonrpc:'2.0',id:m.id,...reply},'*'),window.delay);
        }
      });
    }''')
    def mount():
        page.locator("iframe").evaluate("(el,html)=>{el.srcdoc=html}", html)
        return page.frame_locator("iframe")

    frame = mount()
    expect(frame.locator("#hint")).to_contain_text("不会自动发送")
    assert page.evaluate("contexts.length") == 0
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        frame.locator("main").screenshot(path=str(output))
    page.evaluate("window.delay=150")
    button = frame.get_by_role("button", name="插入ref-check")
    button.click()
    expect(button).to_be_disabled()
    expect(frame.locator("#status")).to_contain_text("已插入")
    expect(button).to_be_enabled()
    assert page.evaluate("contexts.length") == 1
    attachment = page.evaluate("contexts[0].content[0]")
    assert attachment["_meta"]["openai/title"] == "ref-check"
    assert "ref-check" in attachment["text"]
    frame.get_by_role("button", name="插入paper-lookup").click()
    expect(frame.locator("#status")).to_contain_text("已插入「paper-lookup」")
    assert page.evaluate("contexts[1].content.length") == 1
    assert "paper-lookup" in page.evaluate("contexts[1].content[0].text")
    # Host removing the attachment clears stale confirmation; no re-insertion.
    page.evaluate("document.querySelector('iframe').contentWindow.postMessage({jsonrpc:'2.0',method:'ui/notifications/host-context-changed',params:{'openai/modelContext':null}},'*')")
    expect(frame.locator("#status")).to_be_empty()
    assert page.evaluate("contexts.length") == 2
    page.evaluate("window.fail=true")
    frame.get_by_role("button", name="插入reading-contract").click()
    expect(frame.locator("#status")).to_contain_text("未确认插入成功")
    expect(frame.get_by_role("button", name="复制reading-contract")).to_be_visible()
    # Neither message support nor generic context support proves composer insertion.
    for capabilities in [{"message": {"text": {}}}, {"updateModelContext": {"text": {}}}]:
        page.evaluate("caps=>{window.caps=caps;window.fail=false}", capabilities)
        frame = mount()
        expect(frame.locator("#hint")).to_contain_text("不支持直接插入")
        expect(frame.get_by_role("button", name="复制ref-check")).to_be_visible()
    assert not page.evaluate("requests.some(r=>r.method==='ui/message'||r.method==='tools/call')")
    assert not errors, errors
    browser.close()
print(json.dumps({"browser": "passed", "mock_composer_attachment": "passed", "no_auto_send": "passed", "real_codex_ui": "not_tested"}))
