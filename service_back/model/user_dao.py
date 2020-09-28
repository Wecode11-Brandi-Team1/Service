import pymysql

class UserDao:
    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 회원가입
    def sign_up(self, user_info, db):
        cursor = db.cursor()
        QUERY = """
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
        results = cursor.execute(QUERY, 
            (
                user_info['account'],
                '일반가입회원',
                user_info['email'],
                user_info['password'],
                '9999-12-31 12:30:50',
                None,
                None
            )
        )
        cursor.close()
        return results
     
    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 로그인
    def sign_in(self, user_info, db):
        cursor = db.cursor()
        QUERY = """
        SELECT id,password,is_deleted from users where account_id=%s ORDER BY id DESC LIMIT 1;
        """
        cursor.execute(QUERY, (user_info['account']))
        results = cursor.fetchone()
        cursor.close()
        return results

    # 작성자: 김태하
    # 작성일: 2020.09.24.목
    # 기능: 소셜회원가입
    def social_sign_up(self, user_info, db):
        cursor = db.cursor()
        QUERY = """
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
        results = cursor.execute(QUERY, 
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
        cursor.close()
        return results
     
    # 작성자: 김태하
    # 작성일: 2020.09.24.목
    # 기능: 소셜로그인
    def social_sign_in(self, google_user_info, db):
        cursor = db.cursor()
        QUERY = """
        SELECT id,email from users where email=%s ORDER BY id DESC LIMIT 1;
        """
        cursor.execute(QUERY, (google_user_info['email']))
        results = cursor.fetchone()
        cursor.close()
        return results

    # 작성자: 김태하
    # 작성일: 2020.09.27.일
    # 기능: 최신 유저 정보 가져오기
    def user_data(token_paylod, db):
        cursor = db.cursor()
        QUERY = """
        SELECT * from users where id=%s ORDER BY id DESC LIMIT 1;
        """
        cursor.execute(QUERY, (token_paylod['ID']))
        results = cursor.fetchone()
        cursor.close()
        return results

    def shipping_information(user_info, user_request, db):
        cursor = db.cursor()
        QUERY = """
        INSERT INTO shipping_informations (
        name,
        phone_number,
        adrress,
        shipping_memo,
        user_id,
        is_deleted,
        ) VALUES (%s,%s,%s,%s,%s,False,%s,%s,%s)
        """
        results = cursor.execute(QUERY, 
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
        cursor.close()
        return results
