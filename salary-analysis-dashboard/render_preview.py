from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1200, 'height': 1600})
    page.goto('file:///' + os.path.abspath('A4_Dashboard_Poster.html').replace('\\', '/'))
    
    # Hide toolbar
    page.evaluate('''() => {
        const tb = document.querySelector(".toolbar");
        if (tb) tb.style.display = "none";
    }''')
    
    poster = page.query_selector('.a4-poster')
    if poster:
        poster.screenshot(path='dashboard_preview.png')
    else:
        page.screenshot(path='dashboard_preview.png')
    browser.close()
print("Rendered dashboard_preview.png successfully!")
