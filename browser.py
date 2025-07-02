import undetected_chromedriver as uc
from fake_useragent import UserAgent
import time
import random
from selenium.webdriver.common.by import By

def make_options():
    ua = UserAgent()
    user_agent = ua.random

    options = uc.ChromeOptions()
    #options.add_argument('--headless=new')  # less detectable
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options

def wait_for_dom_stability(driver, timeout=60, interval=0.5):
    stable_count = 0
    last_html = ""
    start_time = time.time()

    while time.time() - start_time < timeout:
        current_html = driver.page_source
        if current_html == last_html:
            stable_count += 1
            if stable_count >= 3:  # stable for ~1.5s
                return True
        else:
            stable_count = 0
            last_html = current_html
        time.sleep(interval)
    raise TimeoutError("DOM did not stabilize within timeout.")

def getRawHTML(url):
    print("getRawHTML Called...")
    options = make_options()
    driver = uc.Chrome(options=options)
    driver.get(url)
    wait_for_dom_stability(driver)
    html = driver.page_source
    driver.quit()
    return html

def getAllVisibleText(url):
    print("getAllVisibleText Called...")
    options = make_options()
    driver = uc.Chrome(options=options)
    driver.get(url)
    wait_for_dom_stability(driver)
    
    full_visible_text = driver.execute_script("return document.body.innerText").strip()
    anchors = driver.find_elements(By.TAG_NAME, "a")

    visible_links = []
    for a in anchors:
        try:
            if a.is_displayed():
                link_text = a.text.strip()
                href = a.get_attribute("href")
                if link_text and href:
                    visible_links.append(f"{link_text} → {href}")
        except Exception:
            continue

    output = full_visible_text
    if visible_links:
        output += "\n" + "\n".join(visible_links)

    driver.quit()
    return output
