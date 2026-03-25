from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() #imported it

def create_app():
    app = Flask(__name__)

    # ---------------------configurations start------------------------
    app.config['SECRET_KEY'] = 'secret-key'
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