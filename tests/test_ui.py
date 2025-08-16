# tests/test_ui.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_smoke_loads(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)
    # Prove the form renders
    wait.until(EC.presence_of_element_located((By.NAME, "name")))
    wait.until(EC.presence_of_element_located((By.NAME, "phone")))
