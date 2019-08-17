from flask import session, request


def is_authorized():
    """ Returns whether requester is authenticated. """
    return True

    # TODO: Bonus 1 - authentication guarding
    # if request.method == 'OPTIONS':
    #     return True
    # elif request.endpoint == 'login':
    #     return True
    # elif 'is_auth' in session and\
    #         session['is_auth'] is True and\
    #         'username' in session and\
    #         session['username'] is not None:
    #     return True
    # else:
    #     return False
