from agroTech import app
from flask import render_template, request
from agroTech.static.data.db import get_db, init_db

app.debug = True

@app.route('/')
@app.route('/index.html',methods=('GET','POST'))
def index():
    if request.method == 'POST':
        plantId = request.form['plantId']
        db = init_db()
        db.execute(
                'INSERT INTO pots (plantId) VALUES (?)',
                (plantId)
            )
        db.commit()
        return render_template('index.html',plantId=plantId)
    return render_template('index.html')

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('e404.html'), 404
