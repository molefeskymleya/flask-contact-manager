from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Force the DB to save in the root folder, not /instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./contacts.db'
db = SQLAlchemy(app)

# 🧱 Contact model


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))


# 🛠️ Create the database and tables
with app.app_context():
    print("🔧 Creating database...")
    db.create_all()


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    new_contact = Contact(name=name, phone=phone)
    db.session.add(new_contact)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
