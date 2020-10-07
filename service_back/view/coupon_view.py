import traceback
import config, connection

from flask         import jsonify, request
from flask.views   import MethodView
from flask_request_validator import (
    GET,
    PATH,
    Param,
    JSON,
    validate_params
)

from utils import login_confirm

class CouponsView(MethodView):
    def __init__(self, service):
        self.service = service

    @login_confirm
    def get(self, token_payload):
        try :
            db = connection.get_connection(config.database)
            coupons = self.service.get_coupons(db)

        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify(coupons), 200
        
        finally:
            db.close() 
