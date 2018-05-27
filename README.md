# AgroTech
Automatic agricultural monitoring.
# Basic Requirements
Raspberry Pi3 (required wifi)(only tested on Raspian OS)
<br>
python3
# Installation
`git clone https://github.com/ctezna/AgroTech.git`<br>
`cd AgroTech/`<br>
`cd app/`<br>
`sudo pip3 install -r requirements.txt`<br>
`gunicorn -b 'RPI IP Address':'PORT' agroTech:app`<br>
# Ex.
`gunicorn -b 192.168.1.67:8000 agroTech:app`
# Usage
Monitor the temperature, relative humidity, and pH levels of<br>
a plant located within an <em><b>Agro</b>Tech <b>Smart</b>Pot</em>.<br><br>
Once installed use a web browser connected to the LAN and direct<br>
to the url : `'RPI IP Address':'PORT'`<br><br>
Software allows for up to 6 different plants per server (RPi).<br>
Navigate to <strong><em>+New Pot</em></strong> on the Navbar to begin.
