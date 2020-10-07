import config

from flask         import Flask
from flask_cors    import CORS
from flask_caching import Cache
  
from view          import create_endpoints
from model         import (
    ProductDao, 
    SearchDao, 
    UserDao, 
    QuestionDao,
    CouponDao)
from service       import (
    ProductService, 
    SearchService, 
    UserService, 
    QuestionService,
    CouponService)

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://5cc349d8de88441c9c3427c07077f3a9@o453871.ingest.sentry.io/5443008",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

class Services:
    pass

def create_app(test_config = None):
    """
    Returns :
        생성된 플라스크 앱 객체
    Authors :
        1218kim23@gmail.com(김기욱)
        taeha7b@gmail.com(김태하)
    History :
        2020-10-02 : ASCCI형식 False로 변경(김기욱)
        2020-09-17 : 초기 생성(김기욱 김태하)
    """
    cache = Cache(config={'CACHE_TYPE': 'simple'})
    app = Flask(__name__)
    cache.init_app(app)

    app.config['JSON_AS_ASCII'] = False

    #SetUp CORS
    CORS(app)

    #SetUp config
    if test_config is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.update(test_config)

    #SetUp Persistence Layer
    product_dao  = ProductDao()
    search_dao   = SearchDao()
    user_dao     = UserDao()
    question_dao = QuestionDao()
    coupon_dao   = CouponDao()

    #SetUp Business Layer
    services                  = Services
    services.product_service  = ProductService(product_dao)
    services.search_service   = SearchService(search_dao)
    services.user_service     = UserService(user_dao)
    services.question_service = QuestionService(question_dao)
    services.coupon_service   = CouponService(coupon_dao)

    #SetUp Presentation Layer
    create_endpoints(app, services)

    return app
