import os
import requests

def test_homepage_status(base_url):
    r = requests.get(base_url + "/")
    assert r.status_code in (200, 302)
