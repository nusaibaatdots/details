from flask_sqlalchemy import SQLAlchemy 

from app import app

db = SQLAlchemy(app)

class Details(db.Model):
    id = db.Column(db.String, primary_key=True)
    animal = db.Column(db.String)
