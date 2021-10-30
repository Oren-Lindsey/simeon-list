#Made by Oren Lindsey and Simeon Lindsey, ©2021

from flask import Flask, render_template
from replit import db
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#API
items = {
  "nerf-saturn": False,
}
#db["nerf-saturn"] = False
#db["nerf-pharaoh"] = False
#db["nerf-echo"] = False
#db["nerf-turbine"] = False
#db["nerf-rh"] = False
#db["nerf-rt"] = False
#db["lr1"] = False
#db["nerf-thunderhawk"] = False
#db["nerf-kronos"] = False
#db["mask-yellow"] = False
#db["mask-blue"] = False
#db["nerf-dreadbolt"] = False
#db["sb-game"] = False
#db["lego-train"] = False
#db["nerf-supreme"] = False
#db["chess"] = False
#db["test-item"] = True
#db["uno"] = False
#db["yahtzee"] = False
#db["nerf-curve"] = False
#db["nerf-mercury"] = False

def setDict():
  for i in db:
    items[i] = db[i]

setDict()

def setDB():
  for n in items:
    db[n] = items[n]
  print(db.keys())

@app.route('/api/')
def apiHome():
    return "If you don't know what this is you shouldn't be here"

@app.route('/api/get-status/')
def returnAllItems():
    itemsJson = json.dumps(items)
    response = itemsJson
    return response

@app.route('/api/toggle-item/<string:itemToSwitch>', methods=['GET','POST'])
def toggleItem(itemToSwitch):
      if itemToSwitch in items:
        if items[itemToSwitch] == True:
          items[itemToSwitch]  =  False
          setDB()
          response = "Toggled to false"
          return response
        elif items[itemToSwitch] == False:
          items[itemToSwitch]  =  True
          setDB()
          response = "Toggled to true"
          return response
        else:
          return "Error - It seems that the item was neither true nor false. It should be one or the other"
      else:
        return "That item doesn't exist"

@app.route('/sizes')
def sizes():
    return render_template("sizes.html")

@app.route('/credits')
def credits():
    return render_template("credits.html")

@app.route('/list')
def list():
    return render_template("list.html")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('pageNotFound.html'), 404

print("Starting up")
app.run(host='0.0.0.0', port=8080)
