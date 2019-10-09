from flask import Flask

from cookie.extensions import db, migrate, cache


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)


def register_blueprints(app):
    from cookie.views import blueprint
    app.register_blueprint(blueprint)


def register_commands(app):
    pass


def register_shell_context(app):
    def shell_context():
        return {
            'app': app,
            'db': db,
        }

    app.shell_context_processor(shell_context)
