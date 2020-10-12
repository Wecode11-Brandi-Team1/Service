import re, traceback
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
            에러코드 401 : 유효한 토큰이 아닐경우 메세지와 함께 401 코드를 클라이언트로 전달
            jsonify(message), 400 : 예외가 발생하면 예외코드와 예외명을 400 코드와 함께 클라이언트로 전달
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-10-07 (taeha7b@gmail.com (김태하)) : 불필요한 코드 삭제 및 파라미터 수정
            2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    def wrapper(self, *args, **kwargs):
        try:
            access_token  = request.headers.get("Authorization", None)
            token_payload = jwt.decode(access_token, SECRET_KEY['secret'], ALGORITHM['algorithm'])
            return original_function(self, token_payload, *args, **kwargs)

        except Exception as e:

            return jsonify({'message':f'{e}'}), 401

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

def phone_num_validate(value):
    """
        유저 전화번호 유효성 검사 
        Args:
            유저 전화번호
        Returns :
            True : 유저 전화번호와 정규식이 일치하면 True를 반환함
        Author :
            taeha7b@gmail.com (김태하)
        History:
            2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
    """
    regex = re.compile(r'(\d{3}).*(\d{4}).*(\d{4})')
    if not regex.match(value):
        return True

def catch_exception(f, *args, **kwargs):
    """
        decorator API
            Args:
                에러들을 받는다.
            Retruns:
                return f(*args, **kwargs) -> 데코레이터를 발행해준다.
                jsonify({"message" : f"INVALID_PARAMETER_{e.args[0]}"}), 400 -> 해당 에러 메시지 내용과 400에러
            Authors:
                wldus9503@gmail.com(이지연)
            History:
                2020-09-29(wldus9503@gmail.com) : 데코레이터 초기 생성
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            if len(e.args)==0:
                return jsonify({"message" : "INVALID_PARAMETER"}), 400
            return jsonify({"message" : f"INVALID_PARAMETER_{e.args[0]}"}), 405
    return wrapper


"""
SQL triggers list

#1 : QNA가 추가되면 qna_count값을 +1하는 트리거
DELIMITER $$

CREATE TRIGGER qna_count_up
AFTER INSERT ON questions FOR EACH ROW
BEGIN
	IF NEW.id IS NOT NULL THEN
		UPDATE products as p SET qna_count = qna_count +1 WHERE p.id = NEW.product_id;
	END IF;
END $$

DELIMITER ;

#2 : QNA가 삭제되면 qna_count값을 -1하는 트리거
DELIMITER $$

CREATE TRIGGER qna_count_down
AFTER UPDATE ON questions FOR EACH ROW
BEGIN
	IF NEW.is_deleted = 1 THEN
		UPDATE products as p SET qna_count = qna_count -1 WHERE p.id = OLD.product_id;
	END IF;
END $$

DELIMITER ;

#3 : 쿠폰을 다운로드하면 download_count값을 +1하는 트리거
DELIMITER $$

CREATE TRIGGER coupon_download_count_up
AFTER INSERT ON user_coupons FOR EACH ROW
BEGIN
	IF NEW.id IS NOT NULL THEN
		UPDATE coupon_details as cd SET download_count = download_count +1 WHERE cd.coupon_id = NEW.coupon_id;
	END IF;
END $$

DELIMITER ;

#4 : 다운로드한 쿠폰을 사용하면 use_count값을 +1하는 트리거
DELIMITER $$

CREATE TRIGGER coupon_use_count_up
AFTER UPDATE ON user_coupons FOR EACH ROW
BEGIN
	IF NEW.is_deleted = 1 THEN
		UPDATE coupon_details SET use_count = use_count +1 WHERE coupon_id = OLD.coupon_id;
	END IF;
END $$

DELIMITER ;
""" 