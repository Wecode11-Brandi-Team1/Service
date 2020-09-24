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
        SELECT id,password from users where account_id=%s
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
        SELECT id,email from users where email=%s
        """
        cursor.execute(QUERY, (google_user_info['email']))
        results = cursor.fetchone()
        cursor.close()
        return results