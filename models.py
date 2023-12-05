from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    username = db.Column(db.Integer,
                         primary_key = True,
                         autoincrement = True,
                         unique = True,
                         maximum = 50)
    password = db.Column(db.Text,
                         nullable = False)
    email = db.Column(db.Text,
                      nullable=False,
                      maximum= 50)
    first_name = db.Column(db.Text,
                           nullable = False,
                           maximum = 30)
    last_name = db.Column(db.Text,
                           nullable = False,
                           maximum = 30)