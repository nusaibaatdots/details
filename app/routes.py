import uuid

from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy 

from app import app
from app.models import Details

db = SQLAlchemy(app)

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

