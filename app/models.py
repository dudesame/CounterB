from app import db

class User (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name =  db.Column(db.String(64))
    file_path =  db.Column(db.String(128))