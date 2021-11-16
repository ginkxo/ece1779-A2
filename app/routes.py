from flask import render_template, url_for, flash, redirect, request
from app import app
import boto3
import sys

#Default route and login route the same
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/workers')
def workers():
    # creates a connection to aws services for ec2
    ec2 = boto3.resource('ec2')

    # find all instances with a filter name and running
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # low level client to interact with cloud watch
    # tracks metrics for aws resources
    client = boto3.client('cloudwatch')
    metric_name = 'CPUUtilization'
    statistic = 'Average'

    
    return render_template('workers.html')