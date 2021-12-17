Login page using python flask

Digital Ocean Tutorial in:

https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login



To init database type on a python terminal:
```
from project import db, create_app, models
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
```



To run flask server (visible at http://localhost:5000, local machine only):
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
```




To run flask server (visible by other machines on http://[Server IP]:5000 ):
```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run --host=0.0.0.0
```


