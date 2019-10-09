from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_shell_context(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    from cookie.views import blueprint
    app.register_blueprint(blueprint)


def register_commands(app):
    pass


def register_shell_context(app):
    def shell_context():
        return {
            'app': app,
        }

    app.shell_context_processor(shell_context)
