import config, connection

from flask import jsonify, request
from flask.views import MethodView

from pymysql import err
from utils import (
    login_confirm, 
    AccountValidattionError, 
    PasswordValidattionError, 
    EmailValidattionError
)

class SignUp(MethodView):

    def __init__(self, service):
        self.service = service

    def post(self):
        """
            일반 회원가입 - Presentation Layer(view)) function
            Returns :
                {'message':'User account already exists'} : 아이디가 중복일 경우 409코드와 함께 반환
                {'message':'User email already exists'} : 이메일이 중복일 경우 409코드와 함께 반환
                {'message': e.message} : 유효성에 문제가 생길시 메시지와 400코드가 함께 반환 
                {'message':'SUCCESS'} : 문제 없이 회원가입시 반환
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = connection.get_connection(config.database)
            user_info = request.json
            sign_up = self.service.sign_up(user_info, db)
            if sign_up == 'User account already exists':
                return jsonify({'message':'User account already exists'}), 409

            elif sign_up == 'User email already exists':
                return jsonify({'message':'User email already exists'}), 409

            elif sign_up == 'account_validate':
                raise AccountValidattionError('영문 소문자, 대문자, 숫자 포함하여 4자리 이상 20자리 이하의 아이디로 만들어 주세요')
            
            elif sign_up == 'password_validate':
                raise PasswordValidattionError('영문 소문자, 대문자, 숫자, 특수문자 포함하여 8자리 이상 20자리 이하의 비밀번호로 만들어 주세요')
            
            elif  sign_up == 'email_validate':
                raise EmailValidattionError('이메일 형식이 올바르지 않습니다.')
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        except AccountValidattionError as e:
            return jsonify({'message': e.message}), 400

        except PasswordValidattionError as e:
            return jsonify({'message': e.message}), 400

        except EmailValidattionError as e:
            return jsonify({'message': e.message}), 400

        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()

class SignIn(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        """
            일반 로그인 - Presentation Layer(view)) function
            Returns :
                {'message':'탈퇴한 회원입니다.'} : 탈퇴한 회원이 로그인 시도를 하면 401코드와 함께 반환
                {'message':'Unauthorized'} : 예외 발생시 401코드와 함께 리턴
                {'access_token':access_token} : 로그인에 문제가 없으면 access_token과 200코드가 함께 반환
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = connection.get_connection(config.database)
            user = request.json
            access_token = self.service.sign_in(user, db)
            if access_token == 'is_deleted':
                return jsonify({'message':'탈퇴한 회원입니다.'}), 401

            if access_token == 'no_user':
                return jsonify({'message':'회원정보가 일치하지 않습니다.'}), 401
        
        except:
            return jsonify({'message':'Unauthorized'}), 401

        else:
            return jsonify({'access_token':access_token}), 200

        finally:
            db.close()

class SocialSignUp(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        """
            소셜 회원가입 - Presentation Layer(view)) function
            Returns :
                {'message': 'UNSUCCESS'} : 소셜 회원가입 문제 발생시 400코드와 함께 리턴
                {'message': 'SUCCESS'} : 소셜 회원 가입에 문제가 없이 가입되면 200코드와 함께 반환
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = connection.get_connection(config.database)
            user_info = request.json
            google_access_token = request.headers.get("Authorization", None)
            sign_up = self.service.social_sign_up(user_info, google_access_token, db)

        except:
            db.rollback()
            return jsonify({'message': 'UNSUCCESS'}), 400

        else:
            db.commit()
            return jsonify({'message': 'SUCCESS'}), 200

        finally:
            db.close()

class SocialSignIn(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        """
            소셜 로그인 - Presentation Layer(view)) function
            Returns :
                {'is_google': True} : 소셜 회원가입이 안되어 있으면 401코드와 함께 반환
                {'access_token': access_token} : 소셜 로그인에 성공하면 access_token이 300코드와 함께 반환
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = connection.get_connection(config.database)
            google_access_token = request.headers.get("Authorization", None)
            access_token = self.service.social_sign_in(google_access_token, db)

        except:
            return jsonify({'is_google': True}), 401

        else:
            return jsonify({'access_token': access_token}), 200

        finally:
            db.close()

class ShippingInformation(MethodView):
    def __init__(self, service):
        self.service = service
    
    @login_confirm
    def post(self, token_paylod):
        """
            배송지 정보 - Presentation Layer(view)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :
                {'message':'UNSUCCESS'} : 회원 정보를 못가져오는 예외 발생시 400코드와 함께 반환
                {'message': 'SUCCESS'} : 배송지 정보를 가지고 오면 200코드와 함께 반환
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        try:
            db = connection.get_connection(config.database)
            requestion = request.json
            shipping_information = self.service.shipping_information(token_paylod, requestion, db)
        except:
            db.rollback()
            return jsonify({'message':'UNSUCCESS'}), 400

        else:
            db.commit()
            return jsonify({'message': 'SUCCESS'}), 200

        finally:
            db.close()