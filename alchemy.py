import os
import pymysql
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


# Get username from Heroku workspace
# Modify this variable if running in another environment

app = Flask(__name__)
app.config["CLEARDB_DATABASE_URI"] = 'heroku_5743e02b43306cc'

connection = os.getenv('CLEARDB_DATABASE_URI')

db = SQLAlchemy(app)

app = Flask(__name__)


@app.route('/')
@app.route('/get_artists', methods=['GET', 'POST'])
def get_artists():
    
    """
    List all artists
    """
    
    artists = Artist.query.all()
            
    return render_template("artists.html",  title='Welcome', artists=artists)

    
if __name__ == '__main__':
    app.run(host = os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug = True)
    