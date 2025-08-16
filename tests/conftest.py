# tests/conftest.py
import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

RENDER_CHROME = "/usr/bin/chromium"
RENDER_CHROME_ALT = "/usr/bin/chromium-browser"

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

def _strip_old_chromedriver_from_path():
    """Remove any PATH entries that contain a 'chromedriver' file, so Selenium
    Manager is forced to fetch a matching driver for the installed Chrome."""
    parts = os.environ.get("PATH", "").split(os.pathsep)
    keep = []
    for d in parts:
        try:
            if os.path.exists(os.path.join(d, "chromedriver")):
                # Skip directories that ship an old chromedriver
                continue
        except Exception:
            pass
        keep.append(d)
    os.environ["PATH"] = os.pathsep.join(keep)

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://flask-contact-manager.onrender.com")

@pytest.fixture(scope="session")
def driver():
    _strip_old_chromedriver_from_path()

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1366,768")

    chrome_bin = _detect_browser_binary()
    if chrome_bin:
        opts.binary_location = chrome_bin

    # No Service path. Let Selenium Manager fetch the right driver for Chrome 141.
    drv = webdriver.Chrome(options=opts)
    yield drv
    drv.quit()
