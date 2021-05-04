from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#define and initialize the database
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Report

    create_database(app)

    return app

def create_database(app):
    #if the database does already exist them create one.
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')