from flask       import jsonify
from flask.views import MethodView

import config, connection

# 작성자: 김기욱
# 작성일: 2020.09.22.화
# 상품 데이터와 연결된 View
class ProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try:
            db = connection.get_connection(config.database)
            products = self.service.get_products(db)

            if products == None:
                # 요청한 데이터가 존재하지 않는 경우 에러 전달
                return jsonify({'message':'VALUES DO NOT EXIST'}), 400
        
        except Exception as e:
            return jsonify({f'{e}'}), 400
        
        else:
            return jsonify({'data' : products}), 200
        
        finally:
            db.close()