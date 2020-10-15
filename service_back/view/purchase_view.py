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
            
            if product_order is True:   
                db.commit()
                return jsonify({'message': 'SUCCESS'}), 200

            elif  product_order is False:
                db.rollback()
                return jsonify({'message':'UNSUCCESS'}), 400

        except Exception as e:
            traceback.print_exc()
            db.rollback()
            return jsonify({'message':f'{e}'}), 400

        finally:
            db.rollback()
            db.close()

class MyOrder(MethodView):

    def __init__(self, service):
        self.service = service
    
    @login_confirm
    def get(self, token_paylod):
        """
            마이페이지에 구매 정보 가져오기 - Presentation Layer(view)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
            Returns:
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기 생성
        """
        try:
            db = get_connection()
            my_order = self.service.my_order(token_paylod, db)

        except Exception as e:
            traceback.print_exc()
            return jsonify({'message':f'{e}'}), 400

        else:
            return jsonify(my_order), 200

        finally:
                db.close()

class OrderCancellation(MethodView):

    def __init__(self, service):
        self.service = service
    
    @login_confirm
    def put(self, token_paylod):
        """
            상품 구매 취소하기 - Presentation Layer(view)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기 생성
        """
        try:
            db = get_connection()
            requestion = request.json
            order_cancellation = self.service.order_cancellation(token_paylod, requestion, db)
            if order_cancellation is False:
                db.rollback()
                return jsonify({'message': 'UNSUCCESS'}), 400

        except Exception as e:
            db.rollback()
            traceback.print_exc()
            return jsonify({'message':f'{e}'}), 400

        else:
            db.commit()
            return jsonify({'message': 'SUCCESS'}), 200

        finally:
                db.close()

class Refund(MethodView):

    def __init__(self, service):
        self.service = service
    
    @login_confirm
    def put(self, token_paylod):
        """
            환불 하기 - Presentation Layer(view)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기 생성
        """
        try:
            db = get_connection()
            requestion = request.json
            refund = self.service.refund(token_paylod, requestion, db)
            if refund is False:
                db.rollback()
                return jsonify({'message': 'UNSUCCESS'}), 400

        except Exception as e:
            db.rollback()
            traceback.print_exc()
            return jsonify({'message':f'{e}'}), 400

        else:
            db.commit()
            return jsonify({'message': 'SUCCESS'}), 200

        finally:
                db.close()