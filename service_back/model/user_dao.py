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

            sql_1 = """ 
            INSERT INTO users (
                register_date,
                is_deleted
            ) VALUES(NOW(),0)
            """
            results_1 = cursor.execute(sql_1)
            lastrowid = cursor.lastrowid
            sql_2 = """
            INSERT INTO user_informations (
            user_id,
            account_id,
            name,
            email,
            phone_number,
            password,
            modifier_id,
            created_at,
            expired_at
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
            """
            results_2 = cursor.execute(sql_2, 
                (
                    lastrowid,
                    user_info['account'],
                    '일반가입회원',
                    user_info['email'],
                    None,
                    user_info['password'],
                    None,
                    '9999-12-31 00:00:00'
                )
            )
            return results_2
 
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
            sql = """ SELECT user_id, is_deleted, account_id, password 
                      from users INNER JOIN user_informations ON users.id=user_informations.user_id 
                      where account_id=%s AND expired_at='9999-12-31 00:00:00';
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
            sql_1 = """ 
            INSERT INTO users (
                register_date,
                is_deleted
            ) VALUES(NOW(),0)
            """
            results_1 = cursor.execute(sql_1)
            lastrowid = cursor.lastrowid

            sql_2 = """
            INSERT INTO user_informations (
            user_id,
            account_id,
            name,
            email,
            phone_number,
            password,
            modifier_id,
            created_at,
            expired_at
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,NOW(),%s)
            """
            results_2 = cursor.execute(sql_2, 
                (
                    lastrowid,
                    user_info['account'],
                    user_info['name'],
                    user_info['email'],
                    None,
                    None,
                    None,
                    '9999-12-31 00:00:00'
                )
            )
            return results_2

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
            SELECT user_id,email from user_informations where email=%s AND expired_at='9999-12-31 00:00:00';
            """
            cursor.execute(sql, (google_user_info['email']))
            results = cursor.fetchone()
            return results

    def user_data(self, user_info, db):
        """
            최신 유저 정보 가져오기 - Persistence Layer(model)) function
            Args : 
                user_info : 유저 정보(계정 아이디와 이메일)
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-27 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT * from user_informations where (account_id=%s OR email=%s) AND expired_at='9999-12-31 00:00:00';
            """
            cursor.execute(sql, (user_info['account'], user_info['email']))
            results = cursor.fetchone()
            return results

    def authority_check(self, token_paylod, db):
        """
            토큰의 id로 부터 유저 데이터 가져오기 - Persistence Layer(model)) function
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
            SELECT * from users where id=%s AND expired_at='9999-12-31 00:00:00';
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchone()
            return results

    def shipping_information(self, token_paylod, requestion, db):
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
            sql = """
            INSERT INTO shipping_informations (
            name,
            phone_number,
            user_id,
            is_default_address,
            zip_code,
            address,
            detail_address,
            is_deleted
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,False)
            """
            results = cursor.execute(sql, 
                (
                    requestion['name'],
                    requestion['phone_number'],
                    token_paylod['id'],
                    requestion['is_default_address'],
                    requestion['zip_code'],
                    requestion['address'],
                    requestion['detail_address']
                )
            )
            return results

    def count_shipping_information(self, token_paylod, db):
        with db.cursor() as cursor:
            sql = """
            SELECT COUNT(*) from shipping_informations where user_id=%s AND is_deleted=0;
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchone()
            return results

    def lookup_shipping_information(self, token_paylod, db):
        with db.cursor() as cursor:
            sql = """
            select * from shipping_informations where user_id=%s and is_deleted=0;
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchall()
            return results

    def delete_shipping_information(self, token_paylod, requestion, db):
        with db.cursor() as cursor:
            sql = """
            UPDATE shipping_informations SET is_deleted=1 where id=%s AND user_id=%s;
            """
            results = cursor.execute(sql, (requestion, token_paylod['id']))
            return results

    def revise_shipping_information(self, token_paylod, requestion, db):
        with db.cursor() as cursor:
            sql = """
            UPDATE shipping_informations SET
            name=%s,
            phone_number=%s,
            is_default_address=%s,
            zip_code=%s,
            address=%s,
            detail_address=%s
            WHERE id=%s AND user_id=%s 
            """
            results = cursor.execute(sql, (
                requestion['name'],
                requestion['phone_number'],
                requestion['is_default_address'],
                requestion['zip_code'],
                requestion['address'],
                requestion['detail_address'],
                requestion['id'], 
                token_paylod['id'],
            ))
            return results

    def revise_default_address(self, token_paylod, db):
        with db.cursor() as cursor:
            sql = """
            UPDATE shipping_informations SET
            is_default_address=%s
            WHERE user_id=%s AND is_default_address=%s AND is_deleted=%s
            """
            results = cursor.execute(sql, (
                0,
                token_paylod['id'],
                1,
                0
            ))
            return results