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
from connection  import get_connection
from utils       import catch_exception

class SearchView(MethodView):
    def __init__(self, service):
        self.service = service
    
    @catch_exception
    #표시되는 데이터 갯수는 50개가 default지만 필요에 따라 쿼리파라미터로 수정이 가능하다
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
            db = get_connection()
            params = {
                'limit' :args[0], 
                'q'     :args[1]
            }

            search_stores_results   = self.service.search_stores(params, db)
            search_products_results = self.service.search_products(params, db)
            
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify(
                {
                'stores'   : search_stores_results,
                'products' : search_products_results
                }), 200
        
        finally:
            db.close()