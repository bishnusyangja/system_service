class InternalServerError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class DeviceAlreadyExistsError(Exception):
    pass


class DeviceNotExistsError(Exception):
    pass


errors = {
    'InternalServerError': {
        'status': 500
    },
    'UnauthorizedError': {
        'status': 401
    },
    'SchemaValidationError': {
        'message': 'Request is missing required JSON values',
        'error': 1,
        'status': 400,
    },
    'DeviceNotExistsError': {
        'error': 1,
        'status': 404
    }
}
