from flask import Flask, render_template, request
app = Flask(__name__)
import cPickle as pickle
import pandas as pd
import pymongo
from pymongo import MongoClient
import socket



#ip_addr = socket.gethostbyname(socket.getfqdn())
#print ip_addr
ip_addr = "127.0.0.0"
port = 8080

client = MongoClient('localhost', 27017)

db = client['fraud-database']


'''
with open('data/vectorizer.pkl') as f:
    vectorizer = pickle.load(f)
with open('data/model.pkl') as f:
    model = pickle.load(f)
'''


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
# SHow page which monitors events for fraud
#
@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    if request.method == 'POST':
        body = ["Monitor - Reset stats"]
        return render_template('body.html', body = body)
    else:
        body = ["Monitor display"]
        return render_template('body.html', body = body)

@app.route('/authors')
def authors():
    body = ["Brian McKean","Brent Lemieux","Daniel Hartley","JP Centeno"]
    #body = '''<H1 Brian McKean<br></H1>''' 
    return render_template('body.html', body = body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
