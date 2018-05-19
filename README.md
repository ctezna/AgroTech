# AgroTech
Automatic agricultural monitoring.

# Installation
git clone https://github.com/ctezna/AgroTech.git
#
cd AgroTech/
#
cd app/
#
sudo pip3 install -r requirements.txt
#
gunicorn -b 'RPI IP Address':'PORT' agroTech:app
#
# Ex.
gunicorn -b 192.168.1.67:8000 agroTech:app
