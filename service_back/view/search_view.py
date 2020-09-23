from flask       import jsonify, request

from flask.views import MethodView

# 작성자: 김기욱
# 작성일: 2020.09.23.화
# 스토어 검색기능 Service
class SearchView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        Q     = request.args.get('q')
        limit = request.args.get('r')
        search_stores_results   = self.service.search_stores(Q, limit)
        search_products_results = self.service.search_products(Q, limit)

        return jsonify(
            {
            'stores'   : search_stores_results,
            'products' : search_products_results
            }), 200
    

  
