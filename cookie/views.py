
from flask import Blueprint
from flask.views import MethodView

from cookie.extensions import cache

blueprint = Blueprint('public', __name__, static_folder='static', template_folder='templates')

@blueprint.route('/')
def index():
    cache.set('test', 'test_data')
    return 'hello world'


class HelloWorld(MethodView):
    def get(self):
        return 'hello'


blueprint.add_url_rule(rule='/hello', view_func=HelloWorld.as_view('hello_world'),
                       endpoint='hello_world_hello')
blueprint.add_url_rule(rule='/hi', view_func=HelloWorld.as_view('hello_world'),
                       endpoint='hello_world_hi')

# @blueprint.route('/hi')
# @blueprint.route('/hello')
# def say_hello():
#     return 'hello'


@blueprint.route('/greet', defaults={'name': 'programmer'})
@blueprint.route('/greet/<name>')
def greet(name):
    return 'hello %s' % name

