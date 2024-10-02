import os 
from datetime import timedelta

from flask import ( 
    flash,
    Flask, 
    jsonify, 
    redirect, 
    render_template, 
    request, 
    url_for, 
)

from dotenv import load_dotenv
from werkzeug.security import(
    generate_password_hash, 
    check_password_hash,
) #clase 3/09
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from werkzeug.security import(
    generate_password_hash, 
    check_password_hash,
)

app = Flask(__name__) 

# Configuracion de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
load_dotenv()


@app.route("/")
def index():
    return render_template('index.html')


