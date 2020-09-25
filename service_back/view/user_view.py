import config, connection

from flask import jsonify, request
from flask.views import MethodView

from pymysql import err

# 작성자: 김태하
# 작성일: 2020.09.23.수
# 기능: 회원가입
class SignUp(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            db = connection.get_connection(config.database)
            user_info = request.json
            sign_up = self.service.sign_up(user_info, db)
            
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            db.rollback()
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400
        else:
            db.commit()
            return jsonify({'message':'SUCCESS'}), 200
        finally:
            db.close()

# 작성자: 김태하
# 작성일: 2020.09.23.수
# 기능: 로그인
class SignIn(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            db = connection.get_connection(config.database)
            user = request.json
            access_token = self.service.sign_in(user, db)
        except:
            return jsonify({'message':'Unauthorized'}), 401
        else:
            return jsonify({'access_token':access_token}), 200
        finally:
            db.close()

# 작성자: 김태하
# 작성일: 2020.09.24.목
# 기능: 소셜회원가입
class SocialSignUp(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
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

# 작성자: 김태하
# 작성일: 2020.09.24.목
# 기능: 소셜로그인
class SocialSignIn(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            db = connection.get_connection(config.database)
            google_access_token = request.headers.get("Authorization", None)
            access_token = self.service.social_sign_in(google_access_token, db)
        except:
            return jsonify({'is_google': False}), 401
        else:
            return jsonify({'access_token': access_token}), 200
        finally:
            db.close()