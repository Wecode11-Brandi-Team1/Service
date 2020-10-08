import bcrypt, jwt
import requests
from config import SECRET_KEY, ALGORITHM, SOCIAL_TOKEN_URL
from utils import (
    account_validate, 
    password_validate, 
    email_validate,
    phone_num_validate
)

class UserService:
    def __init__(self, user_dao):
        self.user_dao = user_dao

    def sign_up(self, user_info, db):
        """
            일반 회원가입 - Business Layer(service)) function
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
            일반 로그인 - Business Layer(service)) function
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
            access_token = jwt.encode({'id' : user_data['user_id']}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token
        
        access_token = 'no_user'
        return access_token

    def social_sign_up(self, user_info, google_access_token, db):
        """
            소셜회원가입 - Business Layer(service)) function
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
            소셜로그인 - Business Layer(service)) function
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
        if 'error' in google_user_info:
            return 'error'

        user_info = self.user_dao.social_sign_in(google_user_info, db)
        if google_user_info['email'] == user_info['email']:
            access_token = jwt.encode({'id' : user_info['user_id']}, SECRET_KEY['secret'], ALGORITHM['algorithm']).decode('utf-8')
            return access_token

    def shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 등록 - Business Layer(service)) function
            Args : 
                token_paylod : 유저 정보
                requestion : 유저가 입력한 배송지 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        count_shipping_information = self.user_dao.count_shipping_information(token_paylod, db)
        # 배송지 정보가 5개가 넘으면 등록할수 없다.
        if count_shipping_information['shipping_information_number'] < 5:
            # 처음 등록하는 배송지 정보인지 확인하여 처음 등록하면 기본 배송지로 설정해준다.
            if  count_shipping_information['shipping_information_number'] == 0:
                requestion['is_default_address'] = 1
            else: 
                # 처음 등록하는 배송지 정보가 아니라면 일반 배송지로 등록한다.
                requestion['is_default_address'] = 0
            results = self.user_dao.shipping_information(token_paylod, requestion, db)
            return results
        return False

    def lookup_shipping_information(self, token_paylod, db):
        """
            배송지 정보 가져오기 - Business Layer(service)) function
            Args : 
                token_paylod : 유저 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        results = self.user_dao.lookup_shipping_information(token_paylod, db)
        return results

    def delete_shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 삭제 - Business Layer(service)) function
            Args : 
                token_paylod : 유저 정보
                requestion : 유저가 입력한 배송지 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-08 (taeha7b@gmail.com (김태하)) : 로직 변경 
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        # 요청 받은 배송지 정보를 삭제한다.
        remove_address = self.user_dao.delete_shipping_information(token_paylod, requestion, db)
        # 기본 배송비 정보가 있는지 확인한다.
        check_default_address = self.user_dao.check_default_address(token_paylod, db) 
        # 만약에 기본 배송지가 없다면 최신 배송지 정보를 기본 배송지로 변경한다.
        if check_default_address is None:
            update_default_address = self.user_dao.update_default_address(token_paylod, db)
            return update_default_address

        return remove_address

    def revise_shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 수정 - Business Layer(service)) function
            Args : 
                token_paylod : 유저 정보
                requestion : 유저가 입력한 배송지 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        # 수정 하려는 배송지 정보가 기본 배송지인지 확인하고 기본 배송지이면 다른 배송지를 기본 배송지로 바꿔준다.
        if requestion['is_default_address'] == 1:
            results = self.user_dao.revise_default_address(token_paylod, db)
        results = self.user_dao.revise_shipping_information(token_paylod, requestion, db)
        return results