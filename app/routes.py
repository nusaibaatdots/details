from datetime import datetime

from app import app
import sqlalchemy
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy 
import uuid

import os 

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lvopweizdnegil:b14d73a558cb9f531af9ba1af25549d0c15b128cd0756933c2886fb5080444a7@ec2-54-198-213-75.compute-1.amazonaws.com:5432/dd58a1j890ha1q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
class Details(db.Model):
    # id: uuid.UUID = db.Column(postgresql.UUID(as_uuid=True), unique=True,
    #                                    nullable=False, server_default=sqlalchemy.text('uuid_generate_v4()'))
    id = db.Column(db.String, primary_key=True)
    animal = db.Column(db.String)

def create_tables():
    db.create_all()

@app.route('/')
@app.route('/index')
def index():
    print('HELLO!')
    detailsUUID =  str(uuid.uuid4().fields[-1])[:10]
    detailsUUID = str(detailsUUID)
    q = Details(id=detailsUUID, animal='cat')
    db.session.add(q)
    db.session.commit()

    return "Nusaiba was here :)"