import datetime
import json
from pathlib import Path

from flask import Flask, jsonify, request, Response
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


def get_db_instance():
    from .database import database
    
    
    global db
    
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://tests:tests12345@cluster0-sf4tf.mongodb.net'
    }
    
    app.secret_key = 'this is very secret'
    
    db = database.create(app)


def run(*args, **kwargs):
    global api
    get_db_instance()

    logger.info('[SERVICE] Started.')

    from .api import api

    api = api.create(app)

    CORS(app, origins=CORS_ALLOWED_ORIGINS_LIST,
         supports_credentials=True)

    app.run(*args, **kwargs)


get_db_instance()


# class Device(db.EmbeddedDocument):
class Device(db.Document):
    name = db.StringField()
    created_on = db.DateTimeField()


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(max_length=50)
    created_on = db.StringField(max_length=50)
    device = db.ReferenceField(Device)


@app.route('/')
def home_page():
    return "welcome to Home Page"


# json response view testing
@app.route('/json')
def json_test():
    dct = {'a': 1}
    return jsonify(dct)


@app.route('/about')
def about_page():
    about_text = "This is system service developed by elsight"
    return about_text


def get_all_devices():
    qs = Device.objects.all()
    results = []
    response = {'count': qs.count()}
    for item in qs:
        results.append(dict(pk= str(item.pk), name=item.name, created_on=datetime.datetime.strftime(item.created_on, '%Y-%m-%d %H:%M')))
    response['results'] = results
    return Response(json.dumps(response), status=200, mimetype='application/json')


def add_new_device(data):
    name = data.get('name', '')
    if not name:
        status = 400
        response = dict(name='Required a device name')
    else:
        device = Device(name=name, created_on=datetime.datetime.now())
        device.save()
        response = dict(name=device.name, created_on=device.created_on)
        status = 201
    return Response(json.dumps(response), status=status, mimetype='application/json')


def update_a_device(device_id, name):
    if not name:
        status = 400
        response = dict(name='Required a device name')
    else:
        try:
            obj = Device.objects.get(pk=device_id)
        except Exception as exc:
            print('GETDeviceExcep', exc)
            response = dict(detail='No device found')
            status = 404
        else:
            obj.name = name
            obj.save()
            status = 200
            response = dict(name=obj.name, pk=obj.pk, created_on=obj.created_on)
    return Response(json.dumps(response), status=status, mimetype='application/json')


def delete_a_device(device_id):
    try:
        obj = Device.objects.get(pk=device_id)
    except Exception as exc:
        print('GETDeviceExcep', exc)
        response = dict(detail='No device found')
        status = 404
        return Response(json.dumps(response), status=status, mimetype='application/json')
    else:
        status = 204
        obj.delete()
    return Response(status=status, mimetype='application/json')


@app.route('/devices/', methods=['GET', 'POST'])
@app.route('/devices/<path:device_id>/', methods=['PATCH', 'DELETE', 'PUT'])
def devices_view(device_id=None):
    if request.method.upper() == 'GET':
        return get_all_devices()
    
    if request.method.upper() == 'POST':
        data = request.get_json()
        return add_new_device(data)
        
    if request.method.upper() == 'PUT':
        data = request.get_json()
        name = data.get('name')
        return update_a_device(device_id, name)
    
    if request.method.upper() == 'DELETE':
        return delete_a_device(device_id)


def add_device_to_user():
    status = 200
    return Response( status=status, mimetype='application/json')