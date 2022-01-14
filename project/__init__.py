from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from dotenv import dotenv_values

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
setup = dotenv_values('.env')

def create_app():

    
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = setup['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = setup['SQLALCHEMY_DATABASE_URI']

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    from .models import Node

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
