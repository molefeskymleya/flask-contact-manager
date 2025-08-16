import time
import requests

OK = {200, 301, 302}
TRANSIENT = {502, 503, 504}

def wait_until_ready(url: str, timeout=90, interval=5):
    """Poll the app until it returns an OK status or timeout."""
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=10)
            last = r.status_code
            if r.status_code in OK:
                return r
            if r.status_code not in TRANSIENT:
                # Hard failure, no need to keep waiting
                return r
        except requests.RequestException:
            pass
        time.sleep(interval)
    # Return a final attempt for assertion context
    return requests.get(url, timeout=10)

def test_homepage_status(base_url):
    r = wait_until_ready(base_url + "/")
    assert r.status_code in OK, f"Expected {OK}, got {r.status_code}"
