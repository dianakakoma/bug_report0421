from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#database schema for the user and the bug report models
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    issue = db.Column(db.String(1000))
    url = db.Column(db.String(150))
    
    #timestamp for report creation
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    #associate each report with a user through through a foreign key.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    
    #associate each user with their report
    reports = db.relationship("Report")