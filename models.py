from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer(), primary_key = True)
    spotid = db.Column(db.Integer())
    name = db.Column(db.String())
    popularity = db.Column(db.Integer())
    followers = db.Column(db.Integer())
    image = db.Column(db.String())
    top_tracks = db.Column(db.String())

    def __init__ (self, mydata):
        self.mydata = mydata
