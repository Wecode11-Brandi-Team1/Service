import pymysql

import config

from flask        import Flask
from flask_cors   import CORS
from view         import create_endpoints

from model.user_dao       import UserDao
from service.user_service import UserService
from view.user_view       import SignUp
from model      import ProductDao, SearchDao
from service    import ProductService, SearchService

class Services:
    pass

def create_app(test_config = None):
    app = Flask(__name__)
    CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    #SetUp Persistence Layer
    product_dao = ProductDao()
    search_dao  = SearchDao()

    #SetUp Business Layer
    services = Services
    services.product_service = ProductService(product_dao)
    services.search_service  = SearchService(search_dao, product_dao)

    #SetUp Presentation Layer
    create_endpoints(app, services)

    return app