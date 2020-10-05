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

class QuestionView(MethodView):
    def __init__(self, service):
        self.service = service
    
    @validate_params(
        Param('product_id', PATH, int, required = True),
        Param('u', GET, str, required = False),
        Param('limit', GET, int, default = 5, required = False),
    )
    def get(self, *args):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
            u          : 유저아이디(필터링용)
        Returns:
            200:    
                상품아이디에 매칭되는 Questions JSONDATA
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            params = {
                'product_id': args[0],
                'u'         : args[1],
                'limit'     : args[2]   
            }
            questions = self.service.get_questions(params, db)
        
        except :
            traceback.print_exc()
        
        else:
            return jsonify(questions), 200
        
        finally:
            db.close() 

    @validate_params(
        Param('product_id', PATH, int, required = True),
        Param('questions', JSON, dict, required = True)
    )
    def post(self, *args):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
            q_info     : JSON_DATA
        Returns:
            200:    
                {'message':'SUCCESS'}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            params = {
                'product_id': args[0],
                'q_info'    : args[1]
            }
            self.service.insert_question(params, db)
            
        except :
            traceback.print_exc()
            db.rollback
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 201
        
        finally:
            db.close()

    @validate_params(
        Param('product_id', PATH, int, required = True),
        Param('q', GET, int, required = True)
    )
    def delete(self, *args):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
            q          : 문의글아이디
        Returns:
            200:    
                {'message':'SUCCESS'}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-04(김기욱) : 초기 생성
        """
        try :
            db = connection.get_connection(config.database)
            params = {
                'product_id': args[0],
                'q'         : args[1]
            }
            self.service.delete_question(params, db)
        
        except :
            traceback.print_exc()
            db.rollback
        
        else:
            db.commit()
            return '', 204
        
        finally:
            db.close()
    
