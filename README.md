##Flask Contact Manager##

#Features

	•	Add, view, update, and delete contacts via HTML form or API requests
	•	Persistent storage with SQLite
	•	JSON API endpoints for automated testing
	•	Basic validation and error handling
	•	Styled with Bootstrap
	•	Ready for Selenium UI tests and Postman API tests

#Tools & Technologies

	•	Python 3
	•	Flask
	•	Flask-SQLAlchemy
	•	SQLite
	•	HTML/CSS + Bootstrap
	•	Postman
	•	Selenium + pytest
	•	Git/GitHub
	•	Render (deployment)

#API Endpoints

	•	GET /api/contacts – Get all contacts in JSON
	•	POST /api/contacts – Create a new contact
	•	PUT /api/contacts/<id> – Update a contact
	•	DELETE /api/contacts/<id> – Delete a contact
	•	GET /healthz – Health check

#Setup

	1.	Clone the repo


git clone https://github.com/molefeskymleya/flask-contact-manager.git

cd flask-contact-manager


	2.	Create and activate a virtual environment (optional but recommended)


python -m venv venv

source venv/bin/activate  # Mac/Linux

venv\Scripts\activate     # Windows


	3.	Install dependencies

pip install -r requirements.txt


	4.	Run locally

python app.py

Visit http://127.0.0.1:5000


#Live Demo

	•	https://flask-contact-manager.onrender.com

#Next Steps

	•	Add an Edit button to update contact details from the UI
	•	Create a Search function to quickly find contacts
	•	Add a Thank You page after successfully adding a contact
	•	Include a Navigation link to return to the home page from other views
	•	Implement Flask template inheritance with a layout.html base file containing placeholders for titles, content blocks, and a shared footer
	•	Break HTML into reusable template parts (header, footer, navigation) for a more dynamic and maintainable structure
