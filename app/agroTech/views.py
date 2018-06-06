from agroTech import app
import random
import smtplib
from agroTech.sensorRead import getReadings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, request
from agroTech.static.data.db import get_db, init_db

app.debug = True
randTest = False
rpi = True
raspSerial = '/dev/ttyACM0'

@app.route('/')
@app.route('/index',methods=('GET','POST'))
def index():
	if request.method == 'POST':
		email = request.form['email']
		subject = '- Notification from AgroTech Automations -'
		msg = 'Please check the status of your SmartPots, we have received an alert that one of your plants requires attention.'
		sendemail(email,subject,msg)

	if rpi == False:
	    readings = getReadings('/dev/cu.usbmodem411')
	    if readings == 'ERROR: SERIAL CONNECTION':
		    readings = getReadings('/dev/cu.usbmodem411')
		    if readings == 'ERROR: SERIAL CONNECTION':
			    readings = [-404, -1, -1, -1]
	else:
		readings = getReadings(raspSerial)
		if readings == 'ERROR: SERIAL CONNECTION':
		    readings = getReadings(raspSerial)
		    if readings == 'ERROR: SERIAL CONNECTION':
			    readings = [-404, -1, -1, -1]

	temperature = float(readings[0])
	humidity = float(readings[1])
	ph = float(readings[2])
	gndHum = float(readings[3])
	if humidity is None:
		humidity = -1
	if temperature is None:
		temperature = -404
	if ph is None:
		ph = -1
	if gndHum is None:
		gndHum = -1

	if randTest == True:
		humidity = random.uniform(1,100)
		temperature = random.uniform(10,40)
		ph = random.uniform(6,7)
		gndHum = random.uniform(1,100)
		humidity1 = random.uniform(1,100)
		temperature1 = random.uniform(10,40)
		ph1 = random.uniform(6,7)
		gndHum1 = random.uniform(1,100)
		readings = [temperature, humidity, ph, gndHum, temperature1, humidity1, ph1, gndHum1]

	return render_template("index.html", temp=temperature, hum=humidity, ph=ph, gndHum=gndHum)

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/vegetables')
def vegetables():
    return render_template('vegetables.html')

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')

@app.route('/other')
def other():
    return render_template('other.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/newPot')
def newPot():
	return render_template('newPot.html')

@app.route('/contact',methods=('GET','POST'))
def contact():
	if request.method == 'POST':
		fname = request.form['firstname']
		lname = request.form['lastname']
		sub = request.form['subject']
		msg = request.form['message']
		sub = "From: " + fname + " " + lname + " Sub: " + sub
		sendemail("agrotech.notification@gmail.com",sub,msg)
		return render_template('aboutUs.html')

	return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('e404.html'), 404

def sendemail(to_email,sub,message):
	fromaddr = "agrotech.notification@gmail.com"
	toaddr = to_email
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = sub
	body = message
	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "smartpot06")
	text = msg.as_string()
	try:
	    server.sendmail(fromaddr, toaddr, text)
	except SMTPRecipientsRefused as err:
		print ("Error: Recipient(s) Refuesed")
		raise
	server.quit()
