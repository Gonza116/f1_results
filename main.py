from flask import Flask, render_template, jsonify
import requests
import json
import xmltodict
import xml
import xml.etree.ElementTree as ET

app = Flask(__name__)


#def home():
#    return render_template('hello.html')
@app.route('/')
def homepage():
  r = requests.get(
     'http://ergast.com/api/f1/1998/6/results.json')
  return render_template('results_test.html', results=json.loads(r.text)['MRData']['RaceTable'])

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)