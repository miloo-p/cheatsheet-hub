import asyncio
from playwright.async_api import async_playwright
B = "http://localhost:8765/"
SK = "<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1, viewport-fit=cover'></head><body style='margin:0'>"
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        async def page(w, scheme="light"):
            pg = await b.new_page(viewport={"width": w, "height": 844 if w < 500 else 1000}, color_scheme=scheme)
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" and "net::" not in m.text and "Failed to load resource" not in m.text else None)
            await pg.route("**/*", lambda r: r.abort() if not r.request.url.startswith(B) else r.continue_())
            return pg, errs
        # Hub: index.html wird beim Veröffentlichen in ein Gerüst gesteckt -> nachbilden
        hub_html = open("site/index.html").read()
        pg, errs = await page(390)
        await pg.route(B + "hubtest.html", lambda r: r.fulfill(body=SK + hub_html + "</body></html>", content_type="text/html"))
        await pg.goto(B + "hubtest.html")
        await pg.fill("#q", "consent")
        await pg.wait_for_timeout(400)
        r = await pg.evaluate("() => ({ hits: document.querySelectorAll('#results a').length, first: document.querySelector('#results a') && document.querySelector('#results a').getAttribute('href'), overflow: document.documentElement.scrollWidth - innerWidth })")
        print("hub search", r, errs)
        await pg.fill("#q", "stale closure")
        await pg.wait_for_timeout(300)
        print("hub fulltext", await pg.evaluate("[...document.querySelectorAll('#results a')].map(a => a.getAttribute('href'))"))
        await pg.screenshot(path="ux2_hub_mobile.png")
        # Weiterleitung per Kürzel
        await pg.goto(B + "hubtest.html#css-grid-2")
        await pg.wait_for_timeout(600)
        print("redirect ->", pg.url, await pg.evaluate("document.querySelector('.card.flash') ? document.querySelector('.card.flash').id : null"))
        # Unterseiten
        for k in ["html","css","js","ts","gsap","three","cro"]:
            for w, sc in [(390, "light"), (1280, "dark")]:
                pg, errs = await page(w, sc)
                await pg.goto(B + k + ".html")
                await pg.wait_for_timeout(200)
                m = await pg.evaluate("""() => ({ bar: Math.round(document.getElementById('topbar').getBoundingClientRect().height), over: document.documentElement.scrollWidth - innerWidth, copy: document.querySelectorAll('.copy').length, anchors: document.querySelectorAll('.anchor').length, hl: document.querySelectorAll('pre .k').length })""")
                print(k, w, sc, m, errs[:2])
                await pg.close()
        # Interaktion auf CSS-Seite, Desktop
        pg, errs = await page(1280)
        await pg.goto(B + "css.html")
        await pg.evaluate("document.querySelector('#grundlagen').scrollIntoView()")
        await pg.click("#css-grundlagen-2 .explain > summary")
        await pg.wait_for_timeout(500)
        r = await pg.evaluate("""() => { const c = document.getElementById('css-grundlagen-2'); const g = c.parentElement.getBoundingClientRect(); const r = c.getBoundingClientRect(); return { cardW: Math.round(r.width), gridW: Math.round(g.width), cols: getComputedStyle(c).gridTemplateColumns }; }""")
        print("open card", r)
        await pg.screenshot(path="ux2_open_desktop.png")
        # Menü + Filter mobil
        pg, errs = await page(390)
        await pg.goto(B + "gsap.html")
        await pg.click("details.menu >> nth=0")
        await pg.wait_for_timeout(200)
        await pg.screenshot(path="ux2_menu_mobile.png")
        await pg.click("details.menu >> nth=0 >> a >> nth=2")
        await pg.wait_for_timeout(400)
        await pg.mouse.wheel(0, 600)
        await pg.wait_for_timeout(500)
        print("bar hidden after scroll down:", await pg.evaluate("document.getElementById('topbar').classList.contains('hide')"), "url", pg.url)
        await pg.mouse.wheel(0, -200)
        await pg.wait_for_timeout(400)
        print("bar shown after scroll up:", not await pg.evaluate("document.getElementById('topbar').classList.contains('hide')"))
        # Demo-Klick ohne Netz -> sauberer Fehlertext
        await pg.click(".demo .run >> nth=0")
        await pg.wait_for_timeout(800)
        print("demo offline note:", await pg.evaluate("document.querySelector('.demo .stage').textContent.trim().slice(0,60)"), errs[:2])
        await pg.screenshot(path="ux2_mobile_scrolled.png")
        await b.close()
asyncio.run(main())
