from . import db
# from werkzeug.securirty import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(db.Model):
    '''creates instances of users
    
    Arguments:
        db {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    '''

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'







