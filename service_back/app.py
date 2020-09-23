import pymysql

from flask      import Flask
from flask_cors import CORS

from model      import ProductDao, SearchDao
from service    import ProductService, SearchService
from view       import create_endpoints

import config

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
    db = config.database
    product_dao = ProductDao(db)
    search_dao  = SearchDao(db)

    #SetUp Business Layer
    services = Services
    services.product_service = ProductService(product_dao, app.config)
    services.search_service  = SearchService(search_dao, app.config)

    #SetUp Presentation Layer
    create_endpoints(app, services)

    return app