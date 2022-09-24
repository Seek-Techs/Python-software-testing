from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String())
    stores = db.relationship('StoreModel')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.get(userid)
