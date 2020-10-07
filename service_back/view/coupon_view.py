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

class CouponView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try :
            db = connection.get_connection(config.database)
            coupons = self.service.get_coupons(db)

        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify({'coupons' : coupons}), 200
        
        finally:
            db.close() 

    @validate_params(
        Param('c', GET, int, required = True)
    )
    @login_confirm
    def post(self, token_payload, c):
        try :
            db = connection.get_connection(config.database)
            params = {
                'user_id'   : token_payload['id'],
                'coupon_id' : c
            }
            self.service.download_coupons(params, db)
        
        except Exception as e:
            db.rollback()
            return jsonify({'message':f'{e}'}), 400
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        
        finally:
            db.close()