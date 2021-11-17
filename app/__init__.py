from flask import Flask
import time

app = Flask(__name__)
# a random key for interacting with flask dictionaries - protects cookie tampering
app.config['SECRET_KEY'] = "a8e23cgqg45iy20120e19e2954796e8f"
instance_start_time = time.time()
from app import routes