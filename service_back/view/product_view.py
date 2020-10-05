import traceback
import config, connection

from flask         import jsonify, request
from flask.views   import MethodView
from flask_request_validator import (
    GET,
    PATH,
    Param,
    JSON,
    validate_params
)

import config, connection
from cache import cache

class MainProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        """
        Args:
            service: 서비스 레이어 객체
        Returns:
            200:    
                할인률이 존재하는 상품 & 판매량 상위 상품들로 묶은 리스트 JSONDATA
            400: 
                VALUES DO NOT EXIST : 요청한 데이터가 존재하지 않음
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-22(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            products = self.service.get_main_products(db)

            if products is None:
                # 요청한 데이터가 존재하지 않는 경우 에러 전달
                return jsonify({'message':'VALUES DO NOT EXIST'}), 400
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify({'data' : products}), 200
        
        finally :
            db.close()


class CategorySetView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        """
        Args:
            service: 서비스 레이어 객체
        Returns:
            200:    
                쿼리파라미터에 해당되는 카테고리 JSONDATA
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-25(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            q  = int(request.args.get('q')) 
            category_set = self.service.get_category_set(q, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify(category_set), 200
        
        finally :
            db.close()

class ProductsView(MethodView):
    def __init__(self, service):
        self.service = service

    #Validation_params 데코레이터를 통해 유효성 검사 후 통과한 파라미터들만 튜플로 반환
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
        """
        Args:
            service: 서비스 레이어 객체
            args = {
                'limit'         : 데이터의 최대 갯수,
                'offset'        : 페이지네이션 시작점,
                'sp_id'         : 셀러속성 별 필터링,
                'fc_id'         : 메인카테고리 별 필터링,
                'sc_id'         : 서브카테고리 별 필터링,
                'is_discounted' : 세일상품 필터링,
                'is_popular'    : 인기순 정렬,
                'is_new'        : 신상품 순 정렬,
                'is_cheap'      : 낮은 가격순 정렬
            }

        Returns:
            200:    
                쿼리파라미터에 해당되는 카테고리 JSONDATA
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-28(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            #통과한 파라미터들을 딕셔너리 패킹
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
            products = self.service.get_products(params, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else :
            return jsonify(products), 200
        
        finally :
            db.close() 

class ProductView(MethodView):
    def __init__(self, service):
        self.service = service
    
    def get(self, product_id):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
        Returns:
            200:    
                상품상세 JSONDATA
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-09-29(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            product = self.service.get_product(product_id, db)
        
        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify(product), 200
        
        finally:
            db.close() 