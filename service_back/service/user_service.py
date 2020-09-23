import bcrypt, jwt

from local_settings import SECRET_KEY, ALGORITHM

class UserService:
    def __init__(self, user_dao, config):
        self.user_dao = user_dao
        self.config   = config

    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 회원가입
    def sign_up(self, user_info, db):
        password              = user_info['password']
        hashed_password       = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_info['password'] = hashed_password
        results                  = self.user_dao.sign_up(user_info, db)
        return results

    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 로그인
    def sign_in(self, user_info, db):
        user_account = user_info['account']
        user_data    = self.user_dao.sign_in(user_info, db)
        if bcrypt.checkpw(user_info['password'].encode('utf-8'), user_data[2].encode('utf-8')):
            access_token = jwt.encode({'USER_ID' : user_data[1]}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token

           

