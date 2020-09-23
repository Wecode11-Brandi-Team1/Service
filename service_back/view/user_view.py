import config, connection

from flask       import jsonify, request
from flask.views import MethodView


# 작성자: 김태하
# 작성일: 2020.09.23.수
# 기능: 회원가입
class SignUp(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            db        = connection.get_connection(config.database)
            user_info = request.json
            sign_up   = self.service.sign_up(user_info, db)
        except:
            db.rollback()
            return jsonify({'message':'UNSUCCESS'}), 400
        else:
            db.commit()
            db.close()
            return jsonify({'message':'SUCCESS'}), 200

# 작성자: 김태하
# 작성일: 2020.09.23.수
# 기능: 로그인
class SignIn(MethodView):
    def __init__(self, service):
        self.service = service

    def post(self):
        try:
            db           = connection.get_connection(config.database)
            user         = request.json
            access_token = self.service.sign_in(user, db)
        except:
            db.rollback()
            return jsonify({'message':'UNSUCCESS'}), 400
        else:
            db.commit()
            db.close()
            return jsonify({'access_token':access_token}), 200