import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Paths installed by render.yaml using: apt-get install -y chromium chromium-driver
CHROME_BIN = "/usr/bin/chromium"             # sometimes "/usr/bin/chromium-browser"
CHROMEDRIVER = "/usr/bin/chromedriver"       # sometimes "/usr/bin/chromium-driver"

@pytest.fixture(scope="session")
def base_url():
    # Read from env on Render. Fallback keeps things working if you forget to set it.
    return os.getenv("BASE_URL", "https://flask-contact-manager.onrender.com")

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = CHROME_BIN
    service = Service(CHROMEDRIVER)
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()
