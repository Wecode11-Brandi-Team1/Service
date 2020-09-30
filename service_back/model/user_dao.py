import pymysql

class UserDao:
    def sign_up(self, user_info, db): 
        """
            일반 회원가입 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor: 
            sql = """
            INSERT INTO users (
            account_id,
            register_date,
            is_deleted,
            name,
            email,
            password,
            created_at,
            expired_at,
            phone_number,
            modifier_id
            ) VALUES (%s,NOW(),False,%s,%s,%s,NOW(),%s,%s,%s)
            """
            results = cursor.execute(sql, 
                (
                    user_info['account'],
                    '일반가입회원',
                    user_info['email'],
                    user_info['password'],
                    '9999-12-31 12:59:59',
                    None,
                    None
                )
            )
            return results
 
    def sign_in(self, user_info, db):
        """
            일반로그인 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-23 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor: 
            sql = """
            SELECT id,password,is_deleted from users where account_id=%s AND expired_at='9999-12-31 12:59:59';
            """
            cursor.execute(sql, (user_info['account']))
            results = cursor.fetchone()
            return results

    def social_sign_up(self, user_info, db):
        """
            소셜 회원가입 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :
   
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            INSERT INTO users (
            account_id,
            register_date,
            is_deleted,
            name,
            email,
            password,
            created_at,
            expired_at,
            phone_number,
            modifier_id
            ) VALUES (%s,NOW(),False,%s,%s,%s,NOW(),%s,%s,%s)
            """
            results = cursor.execute(sql, 
                (
                    user_info['account'],
                    user_info['name'],
                    user_info['email'],
                    None,
                    '9999-12-31 12:30:50',
                    None,
                    None
                )
            )
            return results

    def social_sign_in(self, google_user_info, db):
        """
            소셜로그인 - Persistence Layer(model)) function
            Args : 
                google_user_info : 구글 유저 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-24 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT id,email from users where email=%s AND expired_at='9999-12-31 12:59:59';
            """
            cursor.execute(sql, (google_user_info['email']))
            results = cursor.fetchone()
            return results

    def user_data(self, user_info, db):
        """
            최신 유저 정보 가져오기 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT * from users where (account_id=%s OR email=%s) AND expired_at='9999-12-31 12:59:59';
            """
            cursor.execute(sql, (user_info['account'], user_info['email']))
            results = cursor.fetchone()
            return results

    def shipping_information(self, user_info, requestion, db):
        """
            배송지 정보 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보
                user_request : 클라이언트 요청
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            # print(user_info)
            sql = """
            INSERT INTO shipping_informations (
            name,
            phone_number,
            address,
            user_id,
            is_deleted,
            is_default_address
            ) VALUES (%s,%s,%s,%s,False,False)
            """
            results = cursor.execute(sql, 
                (
                    requestion['name'],
                    requestion['phone_number'],
                    requestion['address'],
                    user_info['id']
                )
            )
            return results

    def user_data(self, token_paylod, db):
        """
            유저 데이터 가져오기 - Persistence Layer(model)) function
            Args : 
                token_paylod : {'id': value} 유저 테이블의 id와 value
                db : DATABASE Connection Instance
            Returns :
                해당 유저의 최신데이터 행
            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-29 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT * from users where id=%s AND expired_at='9999-12-31 12:59:59';
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchone()
            return results

