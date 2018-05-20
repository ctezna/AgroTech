from agroTech import app
#import Adafruit_DHT
import random
from flask import render_template, request
from agroTech.static.data.db import get_db, init_db

app.debug = True

@app.route('/')
@app.route('/index.html',methods=('GET','POST'))
def index():
	#humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
	humidity = random.uniform(1,1001)
	temperature = random.uniform(-20,100)
	ph = random.uniform(6,7)
	#humidity = None
	#temperature = None
	#ph = None
	if humidity is None:
		humidity = -1
	if temperature is None:
		temperature = -404
	if ph is None:
		ph = -1

	return render_template("index.html", temp=temperature, hum=humidity, ph=ph)

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/vegetables.html')
def vegetables():
    return render_template('vegetables.html')

@app.route('/fruits.html')
def fruits():
    return render_template('fruits.html')

@app.route('/other.html')
def other():
    return render_template('other.html')

@app.route('/aboutUs.html')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/newPot.html')
def newPot():
	return render_template('newPot.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('e404.html'), 404
