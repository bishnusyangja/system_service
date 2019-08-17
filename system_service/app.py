from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

from system_service.logger import load_logger

CORS_ALLOWED_ORIGINS_LIST = ["?"]

app = Flask(
    __name__,
    static_folder=str(Path(__file__).resolve().parents[1]/'static')
)

logger = load_logger(app)
api = None
db = None


def run(*args, **kwargs):
    from .database import database

    global api
    global db

    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://tests:tests12345@cluster0-sf4tf.mongodb.net'
    }

    app.secret_key = 'this is very secret'

    db = database.create(app)

    logger.info('[SERVICE] Started.')

    from .api import api

    api = api.create(app)

    CORS(app, origins=CORS_ALLOWED_ORIGINS_LIST,
         supports_credentials=True)

    app.run(*args, **kwargs)


class Device(db.EmbeddedDocument):
    name = db.StringField()
    created_on = db.DateTimeField()


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(max_length=50)
    created_on = db.StringField(max_length=50)
    device = db.ReferenceField(Device)


@app.route('/')
def home_page():
    print('home page here')
    return "welcome to Home Page"


# json response view testing
@app.route('/json')
def json_test():
    dct = {'a': 1}
    return jsonify(dct)


@app.route('/about')
def about_page():
    print(request.method)
    about_text = "This is system service developed by elsight"
    return about_text