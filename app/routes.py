import datetime

from app import app
from flask_sqlalchemy import SQLAlchemy 

import os 

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lvopweizdnegil:b14d73a558cb9f531af9ba1af25549d0c15b128cd0756933c2886fb5080444a7@ec2-54-198-213-75.compute-1.amazonaws.com:5432/dd58a1j890ha1q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.Text)

@app.route('/')
@app.route('/index')
def index():
    print('HELLO!')

    q = Details(id='1', animal='cat')
    db.session.add(q)
    db.session.commit()

    return "Nusaiba was here :)"