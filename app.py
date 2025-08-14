from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

# --------------------------
# App and Database Setup
# --------------------------
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./contacts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# --------------------------
# Model
# --------------------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

# --------------------------
# DB Init
# --------------------------
with app.app_context():
    db.create_all()

# --------------------------
# HTML Views
# --------------------------
@app.route("/")
def index():
    contacts = Contact.query.order_by(Contact.id.desc()).all()
    return render_template("index.html", contacts=contacts)

@app.post("/add")
def add_contact():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    if not name or not phone:
        # Keep it simple on the HTML side
        return redirect(url_for("index"))
    db.session.add(Contact(name=name, phone=phone))
    db.session.commit()
    return redirect(url_for("index"))

@app.get("/delete/<int:contact_id>")
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for("index"))

# --------------------------
# Health check for Render
# --------------------------
@app.get("/healthz")
def healthz():
    return {"status": "ok"}, 200

# --------------------------
# JSON API
# --------------------------
@app.get("/api/contacts")
def api_list_contacts():
    contacts = Contact.query.order_by(Contact.id.desc()).all()
    data = [{"id": c.id, "name": c.name, "phone": c.phone} for c in contacts]
    return data, 200

@app.post("/api/contacts")
def api_create_contact():
    if not request.is_json:
        return {"error": "Content-Type must be application/json"}, 415

    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    phone = str(payload.get("phone", "")).strip()

    if not name or not phone:
        return {"error": "Both name and phone are required"}, 400

    contact = Contact(name=name, phone=phone)
    db.session.add(contact)
    db.session.commit()
    return {"status": "created", "id": contact.id}, 201

@app.put("/api/contacts/<int:contact_id>")
def api_update_contact(contact_id):
    if not request.is_json:
        return {"error": "Content-Type must be application/json"}, 415

    contact = Contact.query.get_or_404(contact_id)
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    phone = data.get("phone")

    if name is not None:
        name = str(name).strip()
        if not name:
            return {"error": "name cannot be empty"}, 400
        contact.name = name

    if phone is not None:
        phone = str(phone).strip()
        if not phone:
            return {"error": "phone cannot be empty"}, 400
        contact.phone = phone

    db.session.commit()
    return {"status": "updated", "id": contact.id}, 200

@app.delete("/api/contacts/<int:contact_id>")
def api_delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return {"status": "deleted", "id": contact_id}, 200

# --------------------------
# API Error Handlers
# --------------------------
@app.errorhandler(404)
def not_found(e):
    # Return JSON for API paths, HTML for others
    if request.path.startswith("/api/"):
        return {"error": "not found"}, 404
    return render_template("404.html"), 404

@app.errorhandler(400)
def bad_request(e):
    if request.path.startswith("/api/"):
        return {"error": "bad request"}, 400
    return render_template("400.html"), 400

# --------------------------
# Local Run
# --------------------------
if __name__ == "__main__":
    # Render will use gunicorn via Procfile
    app.run(debug=True, host="0.0.0.0", port=5000)
