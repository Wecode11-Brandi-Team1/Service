import bcrypt, jwt
import requests
from config import SECRET_KEY, ALGORITHM, SOCIAL_TOKEN_URL
from utils import (
    account_validate, 
    password_validate, 
    email_validate
)

class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def sign_up(self, user_info, db):
        """
            일반 회원가입 - Business Layer(view)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        user_data_check=self.user_dao.user_data(user_info, db)
        if account_validate(user_info['account']):
            return 'account_validate'

        elif password_validate(user_info['password']):
            return 'password_validate'

        elif email_validate(user_info['email']):
            return 'email_validate'

        if user_data_check == None:
            hashed_password = bcrypt.hashpw(user_info['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user_info['password'] = hashed_password
            results = self.user_dao.sign_up(user_info, db)
            return results
        
        if user_data_check['account_id'] == user_info['account']:
            return 'User account already exists'

        elif user_data_check['email'] == user_info['email']:
            return 'User email already exists'

    def sign_in(self, user_info, db):
        """
            일반 로그인 - Business Layer(view)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        user_data = self.user_dao.sign_in(user_info, db)
        if user_data['is_deleted'] == 1:
            access_token = 'is_deleted'
            return access_token

        elif bcrypt.checkpw(user_info['password'].encode('utf-8'), user_data['password'].encode('utf-8')):
            access_token = jwt.encode({'id' : user_data['id']}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token
        
        access_token = 'no_user'
        return access_token

    def social_sign_up(self, user_info, google_access_token, db):
        """
            소셜회원가입 - Business Layer(view)) function
            Args : 
                user_info : 유저 정보
                google_access_token : 구글 access_token
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        google_user_info = requests.get(SOCIAL_TOKEN_URL['google_token_url'] + google_access_token).json()
        google_user_info['account'] = user_info['account']
        results = self.user_dao.social_sign_up(google_user_info, db)
        return results

    def social_sign_in(self, google_access_token, db):
        """
            소셜로그인 - Business Layer(view)) function
            Args : 
                google_access_token : 구글 access_token
                db : DATABASE Connection Instance
            Returns :
        
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        google_user_info = requests.get(SOCIAL_TOKEN_URL['google_token_url'] + google_access_token).json()
        user_info = self.user_dao.social_sign_in(google_user_info, db)
        if google_user_info['email'] == user_info['email']:
            access_token = jwt.encode({'id' : user_info['id']}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token

    def shipping_information(self, user_info, db):
        """
            배송지 정보 - Business Layer(view)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        user_request = requests.get().json()
        results = self.user_dao.shipping_information(user_info, user_request, db)
