import logging

from flask import Flask


def load_logger(app: Flask):
    if app.debug is not True and app.logger.level is logging.NOTSET:
        app.logger.setLevel(logging.INFO)

    return app.logger
