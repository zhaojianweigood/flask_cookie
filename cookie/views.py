
from flask import Blueprint

from cookie.extensions import cache

blueprint = Blueprint('public', __name__, static_folder='static', template_folder='templates')


@blueprint.route('/')
def index():
    cache.set('test', 'test_data')
    return 'hello world'


@blueprint.route('/hi')
@blueprint.route('/hello')
def say_hello():
    return 'hello'


@blueprint.route('/greet', defaults={'name': 'programmer'})
@blueprint.route('/greet/<name>')
def greet(name):
    return 'hello %s' % name
