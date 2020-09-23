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
        search_results = self.service.search_stores(Q, limit)

        return jsonify({'data' : search_results}), 200
