import datetime

from app import app
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

@app.route('/')
@app.route('/index')
def index():

    db.session.add(datetime.datetime.now().time())
    db.session.commit()
    return "Nusaiba was here :)"