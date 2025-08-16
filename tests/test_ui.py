# tests/test_ui.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_smoke_loads(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.NAME, "name")))
    wait.until(EC.presence_of_element_located((By.NAME, "phone")))

def test_add_contact(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 15)

    name_input = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form button[type='submit']")))

    unique = str(int(time.time()))
    new_name = f"UI-{unique}"
    new_phone = f"080-{unique[-4:]}-{unique[-4:]}" if len(unique) >= 8 else "080-0000-0000"

    name_input.clear(); name_input.send_keys(new_name)
    phone_input.clear(); phone_input.send_keys(new_phone)
    submit_btn.click()

    # Wait for the new contact to appear in page HTML
    wait.until(lambda d: new_name in d.page_source)
    assert new_name in driver.page_source
