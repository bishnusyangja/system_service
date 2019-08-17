from flask_restful import Api

from system_service.api.v1.common.authorization import is_authorized
from system_service.api.v1.common.errors import UnauthorizedError
from system_service.api.v1.resources.devices.devices import Devices, Device
from system_service.app import logger, app


def create(api: Api):
    api_prefix = "/api/v1"
    device_id = "<string:nic_id>"

    api.add_resource(Devices, "{}/devices".format(api_prefix))
    api.add_resource(Device, "{}/devices/{}".format(api_prefix, device_id))

    logger.info("[API] Loaded \'devices\' resource.")


@app.before_request
def authorize():
    if is_authorized() is False:
        raise UnauthorizedError
