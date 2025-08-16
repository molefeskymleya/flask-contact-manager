# **Flask Contact Manager**

# Setup Instructions

## Create and activate a virtual environment

``` bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

## Install dependencies

``` bash
pip install -r requirements.txt
```

## Run locally

``` bash
python app.py
```

Visit: <http://127.0.0.1:5000>

## Live Demo

<https://flask-contact-manager.onrender.com>

## Running Tests on Render

-   Render installs Chromium and ChromeDriver during the build,
    configured in `render.yaml`.
-   UI tests use headless Chrome with system paths:
    -   Chrome binary: `/usr/bin/chromium`
    -   ChromeDriver: `/usr/bin/chromedriver`
-   Tests read the base URL from the `BASE_URL` environment variable.
    -   On Render: `https://flask-contact-manager.onrender.com`
    -   Locally you can override with:

``` bash
BASE_URL=http://127.0.0.1:5000 pytest
```

-   A worker service can run `pytest -q` against the live site and then
    exit.\
    Check results in the Render worker logs.

## Next Steps

-   Add an **Edit button** to update contact details from the UI
-   Create a **Search function** to quickly find contacts
-   Add a **Thank You page** after successfully adding a contact
-   Include a **Navigation link** to return to the home page from other
    views
-   Implement **Flask template inheritance** with a `layout.html` base
    file containing placeholders for titles, content blocks, and a
    shared footer
-   Break HTML into **reusable template parts** for a more maintainable
    structure
-   Enhance the interface by expanding **Bootstrap components and
    styling** so the app looks cleaner and is easier to use
-   Add **user authentication with logins** so users can manage their
    own contact lists
