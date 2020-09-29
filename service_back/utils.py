import re
import json, jwt
import connection

from flask import jsonify, request
from functools  import wraps
from config import SECRET_KEY, ALGORITHM, database
from model.user_dao import UserDao
from pymysql import err

def login_confirm(original_function):
    """
        로그인 인증 - Business Layer(service) function
        Args:
            original_function : 로그인 인증이후 사용해야하는 함수
  
        Returns :
            original_function : 유효한 토큰일 경우 로그인한 유저 정보와 DB
            jsonify({'message':'LOGIN_REQUIRED'}), 401 : 유효한 토큰이 아닐경우 메세지와 함께 401 코드를 클라이언트로 전달
            jsonify(message), 400 : 예외가 발생하면 예외코드와 예외명을 400 코드와 함께 클라이언트로 전달
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    def wrapper(self):
        try:
            access_token = request.headers.get("Authorization", None)
            if access_token:
                db = connection.get_connection(database)
                token_paylod = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
                user_info = UserDao.login_data(self, token_paylod, db)
                return original_function(self, user_info, db)
            return jsonify({'message':'LOGIN_REQUIRED'}), 401
                    
        except (err.OperationalError, err.InternalError, err.ProgrammingError, err.IntegrityError) as e:
            message = {"error_number": e.args[0], "err_value": e.args[1]}
            return jsonify(message), 400

        finally:
            db.close()

    return wrapper


class AccountValidattionError(Exception):
    """
        유저 아이디 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    def __init__(self, message):
        super().__init__()
        self.message = message

class PasswordValidattionError(Exception):
    """
        유저 비밀번호 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    def __init__(self, message):
        super().__init__()
        self.message = message
 
class EmailValidattionError(Exception):
    """
        유저 이메일 예외 발생
        Args:
            Exception : 예외 발생시의 메세지
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    def __init__(self, message):
        super().__init__()
        self.message = message


def account_validate(value):
    """
        유저 아이디 유효성 검사 
        Args:
            유저 아이디
        Returns :
            True : 유저 아이디와 정규식이 일치하면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    regex = re.compile(r'^[a-zA-Z0-9]{4,20}$')
    if not regex.match(value):
        return True
        
def password_validate(value):
    """
        유저 비밀번호 유효성 검사 
        Args:
            유저 비밀번호
        Returns :
            True : 유저 비밀번호와 정규식이 일치하면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,20}')
    if not regex.match(value):
        return True

def email_validate(value):
    """
        유저 이메일 유효성 검사 
        Args:
            유저 이메일
        Returns :
            True : 유저 이메일와 정규식이 일치하면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    regex = re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not regex.match(value):
        return True
