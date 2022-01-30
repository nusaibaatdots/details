import uuid

from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy 

from app import app
from app.models import Details

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lvopweizdnegil:b14d73a558cb9f531af9ba1af25549d0c15b128cd0756933c2886fb5080444a7@ec2-54-198-213-75.compute-1.amazonaws.com:5432/dd58a1j890ha1q'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# def create_tables():
#     db.create_all()

@app.route('/')
def homepage_passcode_form():
    return render_template('homepage_passcode_form.html')


@app.route('/', methods=["POST"])
def index():
    passcodeInput = request.form["passcodeInput"]
    nameInput = request.form["nameInput"]

    if passcodeInput == 'taco':

        detailsUUID = str(uuid.uuid4().fields[-1])[:5]
        detailsUUID = str(detailsUUID)
        q = Details(id=detailsUUID, animal=nameInput)

        db.session.add(q)
        db.session.commit()

        returnString = "You're in, " + str(nameInput) + "." + "Your UUID is: " + detailsUUID

        return returnString
    return 'Thats ain\'t right, ' + nameInput + ' :('

