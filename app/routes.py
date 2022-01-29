from flask import Flask, request, render_template
from datetime import datetime

from app import app
import sqlalchemy
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy 
import uuid

import os 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lvopweizdnegil:b14d73a558cb9f531af9ba1af25549d0c15b128cd0756933c2886fb5080444a7@ec2-54-198-213-75.compute-1.amazonaws.com:5432/dd58a1j890ha1q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class Details(db.Model):
    id = db.Column(db.String, primary_key=True)
    animal = db.Column(db.String)


def create_tables():
    db.create_all()

@app.route('/')
def homepage_passcode_form():
    return render_template('homepage_passcode_form.html')


@app.route('/', methods=["POST"])
def index():
    passcodeInput = request.form["passcodeInput"]
    nameInput = request.form["nameInput"]

    if passcodeInput == 'taco':

        detailsUUID = str(uuid.uuid4().fields[-1])[:10]
        detailsUUID = str(detailsUUID)
        q = Details(id=detailsUUID, animal=nameInput)

        db.session.add(q)
        db.session.commit()

        returnString = "You're in, " + str(nameInput) + "." + "Your UUID is: " + detailsUUID

        return returnString
    return 'Thats not right, ' + nameInput + ' :('

    # if request.method == 'GET':
    #     return 'hi!'
    # if request.method == 'POST':
    #     form_data = request.form
    #     return 'got form data'
 
    # passcodeInput = request.form['passcode']
    # if passcodeInput == 'taco':

    #     detailsUUID = str(uuid.uuid4().fields[-1])[:10]
    #     detailsUUID = str(detailsUUID)
    #     q = Details(id=detailsUUID, animal='cat')

    #     db.session.add(q)
    #     db.session.commit()

    #     returnString = "Thanks for visiting. Your UUID is: " + detailsUUID

    #     return returnString
    # return 'Not the right passcode'
