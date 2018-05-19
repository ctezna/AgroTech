# AgroTech
Automatic agricultural monitoring.
# Basic Requirements
Raspberry Pi3 (required wifi)
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
