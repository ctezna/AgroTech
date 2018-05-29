from agroTech import app
import random
import smtplib
from agroTech.sensorRead import getReadings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, request
from agroTech.static.data.db import get_db, init_db

app.debug = True

@app.route('/')
@app.route('/index.html',methods=('GET','POST'))
def index():
	if request.method == 'POST':
		email = request.form['email']
		subject = '- Notification from AgroTech Automations -'
		msg = 'Please check the status of your SmartPots, we have received an alert that one of your plants requires attention.'
		sendemail(email,subject,msg)

	# humidity = random.uniform(1,1001)
	# temperature = random.uniform(-20,100)
	# ph = random.uniform(6,7)
	readings = getReadings()
	if readings == 'ERROR: SERIAL CONNECTION':
		readings = getReadings()
		if readings == 'ERROR: SERIAL CONNECTION':
			return render_template("index.html", temp=-404, hum=-1, ph=-1)
	temperature = float(readings[0])
	humidity = float(readings[1])
	ph = float(readings[2])
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
