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
def get_all_races_year():
  year = "2006"
  races = {}
  r = requests.get(
     'http://ergast.com/api/f1/' + year + '/1/results.json')
  races[1] = json.loads(r.text)['MRData']['RaceTable']['Races']
  i = 2
  while(True):
    r = requests.get(
     'http://ergast.com/api/f1/' + year + '/' + str(i) + '/results.json')
    if(int(json.loads(r.text)['MRData']['total']) > 0):
      races[i] = json.loads(r.text)['MRData']['RaceTable']['Races']
      i += 1
    else:
      break
  print(races)
  return render_template('results_test.html', results=races)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)