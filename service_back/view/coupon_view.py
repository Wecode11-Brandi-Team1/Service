import traceback

from flask         import jsonify, request
from flask.views   import MethodView
from flask_request_validator import (
    GET,
    PATH,
    Param,
    JSON,
    validate_params
)

from connection import get_connection
from utils      import login_confirm, catch_exception

class CouponView(MethodView):
    def __init__(self, service):
        self.service = service

    def get(self):
        """
        다운로드 가능한 쿠폰조회 - Presentation Layer(View) function
        Args:
            service    : 서비스 레이어 객체
        Returns:
            200:    
                다운로드&사용가능한 모든 쿠폰리스트 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-07(김기욱) : 초기 생성
        """ 
        try :
            db = get_connection()
            coupons = self.service.get_coupons(db)

        except Exception as e:
            return jsonify({'message':f'{e}'}), 400
        
        else:
            return jsonify({'coupons' : coupons}), 200
        
        finally:
            db.close() 

    @catch_exception
    @validate_params(
        Param('c', GET, int, required = True)
    )
    @login_confirm
    def post(self, token_payload, c):
        """
        쿠폰 다운로드 - Presentation Layer(View) function
        Args:
            service       : 서비스 레이어 객체
            c             : 쿼리파라미터(쿠폰아이디)
            token_payload : 로그인데코레이터로 반환된 user_id 
        Returns:
            200:    
                {message : SUCCESS}
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-08(김기욱) : 쿠폰 중복다운로드 방지 로직 추가
            2020-10-07(김기욱) : 초기 생성
        """ 
        try :
            db = get_connection()
            user_id = token_payload['id']
            downloaded_coupon_check = self.service.check_downloaded_coupons(user_id, c, db)
            
            if downloaded_coupon_check:
                return jsonify({'message':'INVALID ACCESS TO DOWNLOAD'}), 400

            self.service.download_coupons(user_id, c, db)
        
        except Exception as e:
            db.rollback()
            return jsonify({'message':f'{e}'}), 400
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        
        finally:
            db.close()

class UserCouponView(MethodView):
    def __init__(self, service):
        self.service = service

    @login_confirm
    def get(self, token_payload):
        """
        다운로드한 쿠폰 조회 - Presentation Layer(View) function
        Args:
            service       : 서비스 레이어 객체
            token_payload : 로그인데코레이터로 반환된 user_id 
        Returns:
            200:    
                접속한 유저가 다운로드한 모든 쿠폰리스트 JSONDATA
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-08(김기욱) : 초기 생성
        """ 
        try :
            db = get_connection()
            user_id = token_payload['id']
            coupons = self.service.get_downloaded_coupons(user_id, db)
        
        except Exception as e:
            db.rollback()
            return jsonify({'message':f'{e}'}), 400
        
        else:
            db.commit()
            return jsonify(coupons), 200
        
        finally:
            db.close()
    
    @catch_exception
    @validate_params(
        Param('c', GET, int, required = True)
    )
    @login_confirm
    def post(self, token_payload, c):
        """
        다운로드한 쿠폰 사용 - Presentation Layer(View) function
        Args:
            service       : 서비스 레이어 객체
            c             : 쿼리파라미터(쿠폰아이디)
            token_payload : 로그인데코레이터로 반환된 user_id 
        Returns:
            200:    
                {message : SUCCESS}
            400:
                {message : 모든 레이어에서 레이즈된 에러메시지}
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-07(김기욱) : 초기 생성
        """ 
        try :
            db = get_connection()
            params = {
                'user_id'   : token_payload['id'],
                'coupon_id' : c
            }
            self.service.use_downloaded_coupons(params, db)
        
        except Exception as e:
            db.rollback()
            return jsonify({'message':f'{e}'}), 400
        
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        
        finally:
            db.close()