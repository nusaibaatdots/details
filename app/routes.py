import datetime

from app import app
from flask_sqlalchemy import SQLAlchemy 

import os 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():

    db.session.add(datetime.datetime.now().time())
    db.session.commit()

    return "Nusaiba was here :)"