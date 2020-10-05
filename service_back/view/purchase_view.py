from flask import jsonify, request
from flask.views import MethodView

from pymysql import err
from utils import login_confirm

from connection import get_connection

import traceback

class ProductPurchase(MethodView):
    
    def __init__(self, service):
        self.service = service

    @login_confirm
    def post(self, token_paylod):
        """
            상품구매 - Presentation Layer(view)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 로직변경
                2020-10-05 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = get_connection()     
            requestion = request.json
            product_order = self.service.purchase(token_paylod, requestion, db)
            
            if product_order == len(requestion['option_id']):
                db.commit()
                return jsonify({'message': 'SUCCESS'}), 200

            elif  product_order == False:
                db.rollback()
                return jsonify({'message':'UNSUCCESS'}), 400

        except Exception as e:
            traceback.print_exc()
            db.rollback()
            return jsonify({'message':f'{e}'}), 400

        finally:
            db.close()
