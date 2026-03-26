from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy() #imported it

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    # ---------------------configurations start------------------------
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    # ---------------------configurations end------------------------

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from . import models
    return app

# Template inheritance can be added to keep things like navigation same
# on all the pages. implement the navigation.