import asyncio
import json
from playwright.async_api import async_playwright

output_file = "alfa_laval_menu.json"

async def extract_menu():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Navigating to Alfa Laval...")
        await page.goto("https://www.alfalaval.com/", wait_until="domcontentloaded")
        
        # Custom Wait for cookie banner
        try:
            # Wait a bit for banner to potentially appear
            await asyncio.sleep(2)
            accept_btn = page.locator("#onetrust-accept-btn-handler")
            if await accept_btn.is_visible():
                print("Cookie banner detected. Clicking Accept...")
                await accept_btn.click()
                # Wait for banner to disappear
                await page.locator("#onetrust-consent-sdk").wait_for(state="hidden", timeout=5000)
                print("Cookie banner handled.")
            else:
                print("Cookie banner not visible.")
        except Exception as e:
            print(f"Cookie banner handling warning: {e}")
            
        # Ensure overlay is gone before clicking Industries
        await asyncio.sleep(1)

        print("Opening Industries menu...")
        industries_btn = page.locator("button.c-header-main-menu-item", has_text="Industries")
        
        # Force click if needed or wait
        await industries_btn.wait_for(state="visible")
        try:
            await industries_btn.click()
        except:
            print("Regular click failed, trying force click...")
            await industries_btn.click(force=True)
        
        # Wait for the menu container to appear
        menu_container = page.locator(".l-megaMenu-navigation-new-main")
        await menu_container.wait_for(state="visible")

        # Function to scrape a specific level
        async def scrape_level(level_idx):
            # The column for this level
            col_locator = page.locator(f".l-megaMenu-navigation-col.level-{level_idx}")
            
            # Check if column has any items
            items = col_locator.locator(".l-megaMenu-column-item")
            count = await items.count()
            
            results = []
            
            for i in range(count):
                # Re-locate item by index to avoid stale elements if DOM updated
                item = col_locator.locator(".l-megaMenu-column-item").nth(i)
                
                name = await item.text_content()
                name = name.strip() if name else "Unknown"
                
                # Get Link
                link_element = item.locator("a")
                href = await link_element.get_attribute("href")
                if href and not href.startswith("http"):
                    href = "https://www.alfalaval.com" + href
                
                item_data = {
                    "text": name,
                    "url": href,
                    "children": []
                }
                
                # Check for arrow indicating children
                has_arrow = await item.locator("i.icon-angle-right").count() > 0
                
                if has_arrow:
                    # Hover to reveal children
                    # We need to dispatch mouseover often or just hover
                    await item.hover()
                    
                    # Wait for the item to become active, which triggers the next column update
                    # The active class is added to the span .l-megaMenu-column-item
                    await item.wait_for(state="visible")
                    # Small sleep to allow JS to populate the next column
                    await asyncio.sleep(0.5) 
                    
                    # Recursively scrape the next level
                    children = await scrape_level(level_idx + 1)
                    item_data["children"] = children
                
                results.append(item_data)
                
            return results

        print("Starting extraction...")
        # Level 1 is where it starts under Industries
        menu_data = await scrape_level(1)
        
        print(f"Extraction complete. Found top-level items: {len(menu_data)}")
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(menu_data, f, indent=2)
            
        print(f"Saved to {output_file}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(extract_menu())
