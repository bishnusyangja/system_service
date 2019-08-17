from flask import Flask
from flask_mongoengine import MongoEngine


def create(app: Flask):
    app.logger.info('[DATABASE] Starting MongoDB...')
    db = MongoEngine()

    db.init_app(app)
    app.logger.info('[DATABASE] MongoDB started on "{}" '
                    '{}.'.format(db.get_db().name, db.get_db().client.address))

    return db