import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

OUTPUT_CSV = "snapdeal_products.csv"
HEADLESS = False
PAGE_WAIT = 3
SCROLL_PAUSE = 2

BASE_URLS = {
    "Accessories": "https://www.snapdeal.com/search?keyword=accessories",
    "Mobiles": "https://www.snapdeal.com/search?keyword=mobile",
    "Mens Clothing": "https://www.snapdeal.com/search?keyword=mens%20clothing",
}


def human_sleep(sec=2):
    time.sleep(sec)

def safe_text(el):
    try:
        return el.text.strip()
    except:
        return ""

def safe_attr(el, attr):
    try:
        return el.get_attribute(attr)
    except:
        return ""

def scroll_to_bottom(driver, max_scrolls=5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        human_sleep(SCROLL_PAUSE)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


chrome_options = Options()
if HEADLESS:
    chrome_options.add_argument("--headless=new")

chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


data = []

try:
    for category, url in BASE_URLS.items():
        print(f"Scraping category: {category}")
        driver.get(url)
        human_sleep(PAGE_WAIT)

        scroll_to_bottom(driver)

        products = driver.find_elements(By.CLASS_NAME, "product-tuple-listing")

        for product in products:
            name = safe_text(
                product.find_element(By.CLASS_NAME, "product-title")
            ) if product.find_elements(By.CLASS_NAME, "product-title") else ""

            price = safe_text(
                product.find_element(By.CLASS_NAME, "product-price")
            ) if product.find_elements(By.CLASS_NAME, "product-price") else ""

            link = safe_attr(
                product.find_element(By.TAG_NAME, "a"),
                "href"
            ) if product.find_elements(By.TAG_NAME, "a") else ""

            data.append({
                "Category": category,
                "Product Name": name,
                "Price": price,
                "Product Link": link
            })

finally:
    driver.quit()


df = pd.DataFrame(data)
df.to_csv(OUTPUT_CSV, index=False)
print("Data saved to", OUTPUT_CSV)