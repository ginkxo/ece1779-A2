from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
import time

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# a random key for interacting with flask dictionaries - protects cookie tampering
app.config['SECRET_KEY'] = "a8e23cgqg45iy20120e19e2954796e8f"
instance_start_time = time.time()
from app import routes, models