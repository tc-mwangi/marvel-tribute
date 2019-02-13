from . import db
# from werkzeug.securirty import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(db.Model):
    '''creates instances of users
    
    Arguments:
        db {[type]} -- [connects object to marvel_app database]
    
    Returns:
        [type] -- [description]
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    '''defines roles granting different levels of access in application
    
    Arguments:
        db {[type]} -- [connects object to marvel_app database]
    '''
    __tablename__='roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')


    def __repr__(self):
        return f'Role{self.name}'









