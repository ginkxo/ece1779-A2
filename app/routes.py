from flask import render_template, url_for, flash, redirect, request
from app import app
import boto3

#Default route and login route the same
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/workers')
def workers():
    
    pass