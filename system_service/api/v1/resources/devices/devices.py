from flask_restful import Resource
from flask import request

from system_service.api.v1.common.errors import InternalServerError
from system_service.app import db, logger


class Device(Resource):
    def delete(self, _id):
        self.__remove_device(_id)

        return None, 200

    def __remove_device(self, _id):
        pass


class Devices(Resource):
    def get(self):

        pass

    def post(self):

        self.__add_devices()

        return None, 200

    def __add_devices(self, _request):
        devices = [tuple(device.values()) for device in _request['devices']]

        try:
            pass
        except Exception:
            raise InternalServerError(
                "[API] One of the added devices is already exists.")