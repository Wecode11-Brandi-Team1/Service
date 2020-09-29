import pymysql

class UserDao:
    def sign_up(self, user_info, db): 
        """
            일반 회원가입 - Persistence Layer(view)) function
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
            일반로그인 - Persistence Layer(view)) function
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
            소셜 회원가입 - Persistence Layer(view)) function
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
            소셜로그인 - Persistence Layer(view)) function
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
            최신 유저 정보 가져오기 - Persistence Layer(view)) function
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

    def shipping_information(self, user_info, user_request, db):
        """
            배송지 정보 - Persistence Layer(view)) function
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
            sql = """
            INSERT INTO shipping_informations (
            name,
            phone_number,
            adrress,
            shipping_memo,
            user_id,
            is_deleted,
            ) VALUES (%s,%s,%s,%s,%s,False,%s,%s,%s)
            """
            results = cursor.execute(sql, 
                (
                    user_request['name'],
                    user_request['phone_number'],
                    user_request['adrress'],
                    user_request['shipping_memo'],
                    user_request['user_id'],
                    user_request['user_name'],
                    user_request['user_phone_number'],
                    user_request['user_email']
                )
            )
            return results
