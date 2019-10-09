
from flask import Blueprint

blueprint = Blueprint('public', __name__, static_folder='static', template_folder='templates')


@blueprint.route('/')
def index():
    return 'hello world'


@blueprint.route('/hi')
@blueprint.route('/hello')
def say_hello():
    return 'hello'


@blueprint.route('/greet', defaults={'name': 'programmer'})
@blueprint.route('/greet/<name>')
def greet(name):
    return 'hello %s' % name
