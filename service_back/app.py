import pymysql

import config

from flask        import Flask
from flask_cors   import CORS
from view         import create_endpoints

from model.user_dao       import UserDao
from service.user_service import UserService
from view.user_view       import SignUp

class Services:
    pass

def create_app(test_config = None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    user_dao = UserDao()
    services = Services
    services.user_service = UserService(user_dao, app.config)
    create_endpoints(app, services)
    return app