Login page using python flask
Digital Ocean Tutorial in:
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

To init database type on a python terminal:
 from project import db, create_app, models
 db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.

To run flask server (visible on local machine only):
 export FLASK_APP=project
 export FLASK_DEBUG=1
 flask run

Pages should be visible by local machine at localhost:5000

To run flask server (visible by other machines):
 export FLASK_APP=project
 export FLASK_DEBUG=1
 flask run --host=0.0.0.0

Pages should be visible at [Server IP]:5000

