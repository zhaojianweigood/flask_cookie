from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app):
    pass
