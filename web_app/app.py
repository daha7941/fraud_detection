from flask import Flask, render_template, request
app = Flask(__name__)
#from flask_restful import Resource, Api
import cPickle as pickle
import pandas as pd
import pymongo
from pymongo import MongoClient
import socket
import requests
import time
import json 
from prediction_pipe import get_prediction

### Web Site
# home page
@app.route('/')
def index():
    return render_template('index.html')

# register
# Opens up a form to input 
#
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        body = ["Register"]
        return render_template('body.html', body = body)
    else:
        body = ["Register form"]
        return render_template('body.html', body = body)

# monitor
# Show page which monitors events for fraud
#
@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    global DATA, fraud_events, total_events, db
    if request.method == 'POST':
        body = ["Monitor - Reset stats"]
        DATA = []
        fraud_events = 0
        total_events = 0
        return render_template('body.html', body = body)
    else:
        dp = DATA[-1]
        body = ["Fraud Events = {0}\nTotal Events={1}".format(fraud_events, total_events)]
        body.append(" ")
        body.append("Current Event => '{0}'".format( dp['name']))
        body.append("Current Event Fraud Risk => '{0}'".format(dp['risk']))
        return render_template('body.html', body = body)

@app.route('/authors')
def authors():
    body = ["Brian McKean","Brent Lemieux","Daniel Hartley","JP Centeno"]
    #body = '''<H1 Brian McKean<br></H1>''' 
    return render_template('body.html', body = body)

# REST operation to add an event to score 
# score
@app.route('/score', methods=['POST'])
def score():
    global TIMESTAMP, DATA, fraud_events, total_events, db
    total_events += 1
    #dp = json.dumps(request.json, sort_keys=True, indent=4, separators=(',', ': '))
    dp = request.get_json(force=True)
    #dp = request.get_json()
    print "Received event ",dp['name'] 
    ###
    ### Risk from model
    ###
    risk = 'low'
    prob = 0
    # Score the risk of the event
    # Use copy of the data as function changes data 
    #
    temp = dp.copy()
    risk, prob = get_prediction(temp)
    print 'Fraud risk is {} -- {}%  chance of fraud'.format(risk, prob*100.) 
    dp['risk'] = risk
    dp['prob_fraud'] = prob
    if (dp['risk'] != 'low'):
        fraud_events += 1
    db.event.insert_one(dp)        
    DATA.append(dp)
    TIMESTAMP.append(time.time())
    return ""  

# Score function 
# -- called after data point put into DATA
def xscore():
    line1 = "Number of data points: {0}".format(len(DATA))
    if DATA and TIMESTAMP:
        dt = datetime.fromtimestamp(TIMESTAMP[-1])
        data_time = dt.strftime('%Y-%m-%d %H:%M:%S')
        line2 = "Latest datapoint received at: {0}".format(data_time)
        line3 = DATA[-1]
        output = "{0}\n\n{1}\n\n{2}".format(line1, line2, line3)
    else:
        output = line1
    #return output, 200, {'Content-Type': 'text/css; charset=utf-8'}
    return  

if __name__ == '__main__':
    PORT = 8080
    global TIMESTAMP
    global DATA
    TIMESTAMP = []
    DATA = []
    client = MongoClient('localhost', 27017)
    db = client['fraud-database']
    fraud_events = 0
    total_events = 0
    
    app.run(host='0.0.0.0', port=PORT, debug=True)
