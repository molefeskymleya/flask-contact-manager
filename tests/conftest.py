# tests/conftest.py
import os, shutil, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

RENDER_CHROME = "/usr/bin/chromium"
RENDER_CHROME_ALT = "/usr/bin/chromium-browser"
RENDER_DRIVER = "/usr/bin/chromedriver"
RENDER_DRIVER_ALT = "/usr/bin/chromium-driver"

def _detect_browser_binary():
    env_path = os.getenv("CHROME_PATH")
    if env_path and (shutil.which(env_path) or os.path.exists(env_path)):
        return env_path
    gh_path = shutil.which("google-chrome") or "/usr/bin/google-chrome"
    if gh_path and os.path.exists(gh_path):
        return gh_path
    for p in (RENDER_CHROME, RENDER_CHROME_ALT):
        if os.path.exists(p):
            return p
    return None

def _detect_chromedriver():
    env_drv = os.getenv("CHROMEDRIVER_PATH")
    if env_drv and os.path.exists(env_drv):
        return env_drv
    for p in (RENDER_DRIVER, RENDER_DRIVER_ALT):
        if os.path.exists(p):
            return p
    return None

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://flask-contact-manager.onrender.com")

@pytest.fixture(scope="session")
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1366,768")

    chrome_bin = _detect_browser_binary()
    if chrome_bin:
        opts.binary_location = chrome_bin

    chromedriver_path = _detect_chromedriver()
    if chromedriver_path:
        service = Service(chromedriver_path)
        drv = webdriver.Chrome(service=service, options=opts)
    else:
        drv = webdriver.Chrome(options=opts)

    yield drv
    drv.quit()
