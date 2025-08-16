import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_BIN = "/usr/bin/chromium"           # or try "/usr/bin/chromium-browser"
CHROMEDRIVER = "/usr/bin/chromedriver"     # or try "/usr/bin/chromium-driver"

def make_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = CHROME_BIN
    service = Service(CHROMEDRIVER)
    return webdriver.Chrome(service=service, options=options)

def test_homepage_loads():
    base_url = os.getenv("BASE_URL", "http://localhost:10000")
    driver = make_driver()
    try:
        driver.get(base_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        assert "Contacts" in driver.page_source
    finally:
        driver.quit()

