from flask       import jsonify, request
from flask.views import MethodView
from flask_request_validator import (
    GET,
    PATH,
    Param,
    JSON,
    validate_params
)

import config, connection

# 작성자: 김기욱
# 수정일: 2020.09.25 금
# 카테고리 View 추가, 예외처리 구문 추가 및 수정
# 작성일: 2020.09.22.화
# 상품 데이터와 연결된 View
class MainProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try:
            db = connection.get_connection(config.database)
            products = self.service.get_main_products(db)

            if products == None:
                # 요청한 데이터가 존재하지 않는 경우 에러 전달
                return jsonify({'message':'VALUES DO NOT EXIST'}), 400
        
        except Exception as e:
            return jsonify({'Error':f'{e}'}), 400
        
        else:
            return jsonify({'data' : products}), 200
        
        finally:
            db.close()

class CategorySetView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try:
            db = connection.get_connection(config.database)
            Q     = int(request.args.get('q'))
            category_set = self.service.get_category_set(Q, db)
        
        except Exception as e:
            return jsonify({'Error':f'{e}'}), 400
        
        else:
            return jsonify(category_set), 200
        
        finally:
            db.close()

class ProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    @validate_params(
        Param('limit',  GET, int, default = 100, required = False),
        Param('offset', GET, int, required = False),
        Param('sp_id',  GET, int, required = False),
        Param('fc_id',  GET, int, required = False),
        Param('sc_id',  GET, int, required = False),
        Param('is_discounted', GET, bool, required = False),
        Param('is_popular', GET, bool, required = False),
        Param('is_new',   GET, bool, required = False),
        Param('is_cheap', GET, bool, required = False)
    )
    def get(self, *args):
        try:
            db = connection.get_connection(config.database)
            params = {
                'limit'         :args[0],
                'offset'        :args[1],
                'sp_id'         :args[2],
                'fc_id'         :args[3],
                'sc_id'         :args[4],
                'is_discounted' :args[5],
                'is_popular'    :args[6],
                'is_new'        :args[7],
                'is_cheap'      :args[8]
            }
            print('@@@@@@@@@view@@@@')
            print(params)
            products = self.service.get_products(params, db)
        
        except Exception as e:
            return jsonify({'Error on View':f'{e}'}), 400
        
        else:
            return jsonify(products), 200
        
        finally:
            db.close()