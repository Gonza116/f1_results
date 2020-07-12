from flask import Flask, render_template, jsonify, request, redirect
import requests
import json
import xmltodict
import xml
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/consult_year/', methods=['GET'])
def get_all_races_year():
  year = str(request.args.get("year"))
  race = str(request.args.get("race"))
  if(race == "None"):
    race = "1"
  try:
    int(year)
    int(race)
  except:
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  if(race == "0" or int(year) < 1950):
    return render_template('not_available.html')
  r = requests.get(
    'http://ergast.com/api/f1/' + year + '/' + race + '/results.json')  
  print(r.text)
  print('http://ergast.com/api/f1/' + year + '/' + race + '/results.json')
  data= {}
  try:
    whole_json = json.loads(r.text)
    data['results'] = whole_json['MRData']['RaceTable']['Races']
  except:
    print("ERROR: API down")
    return render_template('error_api.html')
  if(whole_json["MRData"]["total"] == "0"):
    return render_template('not_available.html')
  data['prev'] = str(int(race) - 1)
  data['next'] = str(int(race) + 1)
  data['year'] = year
  return render_template('results_test.html', data=data)
  
  
  
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)