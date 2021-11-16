from flask import Flask

app = Flask(__name__)
# a random key for interacting with flask dictionaries - protects cookie tampering
app.config['SECRET_KEY'] = "a8e23cgqg45iy20120e19e2954796e8f"
from app import routes