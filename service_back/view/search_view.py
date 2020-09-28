import traceback

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


class SearchView(MethodView):
    def __init__(self, service):
        self.service = service
    
    @validate_params(
        Param('limit', GET, int, default = 50, required = False),
        Param('q', GET, str, required = True)
    )
    def get(self, *args):
        """
        Args :
            service: 서비스레이어 객체
            args = {
                'limit' : 데이터의 최대 갯수,
                'q'     : 검색어
            }
        Returns :
            200:
                쿼리파라미터와 매칭되는 상품 및 셀러정보 JSONDATA
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-04 : 예외처리 추가
            2020-09-23 : 초기 생성
        """
        try:
            db = connection.get_connection(config.database)
            params = {
                'limit' :args[0], 
                'q'     :args[1]
            }

            search_stores_results   = self.service.search_stores(params, db)
            if not search_stores_results :
                search_stores_results = "검색된 스토어가 없습니다."

            search_products_results = self.service.search_products(params, db)
            if not search_products_results :
                search_products_results = '검색된 상품이 없습니다.'
        
        except :
            traceback.print_exc()
        
        else:
            return jsonify(
                {
                'stores'   : search_stores_results,
                'products' : search_products_results
                }), 200
        
        finally:
            db.close()