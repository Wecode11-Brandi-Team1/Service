from flask       import jsonify, request
from flask.views import MethodView

import config, connection

# 작성자: 김기욱
# 작성일: 2020.09.23.화
# 검색기능 View
class SearchView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        try:
            db = connection.get_connection(config.database)
            Q     = request.args.get('q')
            limit = int(request.args.get('r'))
            search_stores_results   = self.service.search_stores(Q, limit, db)
            search_products_results = self.service.search_products(Q, limit, db)
        
        except:
            return jsonify({'message':'FAILED'}), 400
        
        else:
            return jsonify(
                {
                'stores'   : search_stores_results,
                'products' : search_products_results
                }), 200
        
        finally:
            db.close()