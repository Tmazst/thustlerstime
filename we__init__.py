from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET KEY'] = 'Tma*@1111'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.sqlite3'

db = SQLAlchemy(app)


with app.app_context():
    db.create_all()

# return app




#from __init__ import routes




