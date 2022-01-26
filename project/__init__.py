from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import dotenv_values


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
setup = dotenv_values('.env_local')
app = Flask(__name__)


def create_app():

    
    app.config['SECRET_KEY'] = setup['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = setup['SQLALCHEMY_DATABASE_URI']
    app.config['MQTT_BROKER_URL']=setup['MQTT_BROKER_URL']
    app.config['MQTT_BROKER_PORT']=int(setup['MQTT_BROKER_PORT'])
    app.config['MQTT_USERNAME']=setup['MQTT_USERNAME']
    app.config['MQTT_PASSWORD']=setup['MQTT_PASSWORD']
    app.config['MQTT_KEEPALIVE']=int(setup['MQTT_KEEPALIVE'])
    app.config['MQTT_TLS_ENABLED']=(setup['MQTT_TLS_ENABLED']=="True")

    app.app_context().push()
    db.init_app(app)


    from .models import User
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

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

    # blueprint for mqtt parts of app
    from .mqtt import mqtt as mqtt_blueprint
    app.register_blueprint(mqtt_blueprint)
    from .mqtt import mqtt_var
    mqtt_var.init_app(app)

    return app

