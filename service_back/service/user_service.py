import bcrypt, jwt
import requests
from   config import SECRET_KEY, ALGORITHM

class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao
    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 회원가입
    def sign_up(self, user_info, db):
        hashed_password       = bcrypt.hashpw(user_info['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user_info['password'] = hashed_password
        results               = self.user_dao.sign_up(user_info, db)
        return results

    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 로그인
    def sign_in(self, user_info, db):
        user_data    = self.user_dao.sign_in(user_info, db)
        if bcrypt.checkpw(user_info['password'].encode('utf-8'), user_data[1].encode('utf-8')):
            access_token = jwt.encode({'ID' : user_data[0]}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token

    # 작성자: 김태하
    # 작성일: 2020.09.24.목
    # 기능: 소셜로그인
    def social_sign_in(self, google_access_token, db):
        google_validate_token_url = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token="
        google_response           = requests.get(google_validate_token_url + google_access_token)
        google_user_info          = google_response.json()
        user_info                 = self.user_dao.social_sign_in(google_user_info, db)
        if google_user_info['email'] == user_info[1]:
            access_token = jwt.encode({'ID' : user_info[0]}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token

    # 작성자: 김태하
    # 작성일: 2020.09.24.목
    # 기능: 소셜회원가입
    def social_sign_up(self, user_info, google_access_token, db):
        google_validate_token_url   = "https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token="
        google_response             = requests.get(google_validate_token_url + google_access_token)
        google_user_info            = google_response.json()
        google_user_info['account'] = user_info['account']
        results                     = self.user_dao.social_sign_up(google_user_info, db)
        return results