import os

from cookie.app import create_app
from cookie.settings import ProdConfig, DevConfig
CONFIG = ProdConfig if os.environ.get('FLASK_ENV') == 'production' else DevConfig
app = create_app(config=CONFIG)


@app.route('/')
def index():
    return 'hello world'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return 'hello'


@app.route('/greet', defaults={'name': 'programmer'})
@app.route('/greet/<name>')
def greet(name):
    return 'hello %s' % name


if __name__ == '__main__':
    app.run()
