from flask       import jsonify

from flask.views import MethodView

# 작성자: 김기욱
# 작성일: 2020.09.22.화
# 상품 데이터와 연결된 class
class ProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try:
            products = self.service.get_products()

            if products == None:
                # 요청한 데이터가 존재하지 않는 경우 에러 전달
                return jsonify({'message':'VALUES DO NOT EXIST'}), 400

            return jsonify({'data' : products}), 200

        except:
            return jsonify({'message':'FAILED'}), 400