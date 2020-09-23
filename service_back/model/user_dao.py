import pymysql

from flask      import jsonify

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
        last_name,
        first_name,
        email,
        password,
        created_at,
        expired_at,
        phone_number,
        modifier_id
        ) VALUES (%s,NOW(),%s,%s,%s,%s,%s,NOW(),%s,%s,%s)
        """
        results = cursor.execute(QUERY, 
            (
                user_info['account'],
                False,
                None,
                None,
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
        SELECT id,account_id,password from users where account_id=%s
        """
        cursor.execute(QUERY, (user_info['account']))
        results = cursor.fetchone()
        cursor.close()
        return results