import json, jwt
import connection

from flask import jsonify, request
from functools  import wraps
from config import SECRET_KEY, ALGORITHM, database
from model.user_dao import UserDao
from pymysql import err
# 작성자: 김태하
# 작성일: 2020.09.27.일
# 기능: 데토레이터 함수로 로그인 인증을 확인함
def login_confirm(original_function):
    def wrapper(self):
        try:
            access_token = request.headers.get("Authorization", None)
            if access_token:
                db = connection.get_connection(database)
                token_paylod = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                user_info = UserDao.user_data(token_paylod, db)
                return original_function(self, user_info, db)
            return jsonify({'message':'LOGIN_REQUIRED'}), 401
                    
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

    return wrapper