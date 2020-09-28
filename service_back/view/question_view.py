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
        Param('limit', GET, int, default = 5, required = False),
        Param('user_id', GET, str, required = False)
    )
    def get(self, *args):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
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
                'limit'     : args[1],
                'user_id'   : args[2]
            }
            questions = self.service.get_questions(params, db)
        
        except :
            traceback.print_exc()
        
        else:
            return jsonify(questions), 200
        
        finally:
            db.close() 
    
    def post(self, product_id):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
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
            q_info = request.json
            self.service.insert_question(product_id, q_info, db)
        
        except :
            traceback.print_exc()
            db.rollback
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        
        finally:
            db.close()
    
    def delete(self, product_id):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
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
            q = int(request.args.get("q"))
            self.service.delete_question(product_id, q, db)
        
        except :
            traceback.print_exc()
            db.rollback
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        
        finally:
            db.close()
    
