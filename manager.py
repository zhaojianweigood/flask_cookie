import os

from cookie.app import create_app
from cookie.settings import ProdConfig, DevConfig


CONFIG = ProdConfig if os.environ.get('FLASK_ENV') == 'production' else DevConfig
app = create_app(config=CONFIG)

if __name__ == '__main__':
    app.run()
