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
                      FROM users INNER JOIN user_informations 
                      ON users.id=user_informations.user_id 
                      WHERE account_id=%s AND expired_at='9999-12-31 00:00:00'
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
            SELECT user_id,email 
            FROM user_informations 
            WHERE email=%s AND expired_at=%s
            """
            cursor.execute(sql, (
                google_user_info['email'],
                '9999-12-31 00:00:00'
            ))
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
            SELECT * 
            FROM user_informations 
            WHERE (account_id=%s OR email=%s) AND expired_at=%s
            """
            cursor.execute(sql, (
                user_info['account'], 
                user_info['email'], 
                '9999-12-31 00:00:00'
            ))
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
            SELECT * 
            FROM users 
            WHERE id=%s AND expired_at=%s
            """
            cursor.execute(sql, (
                token_paylod['id'],
                '9999-12-31 00:00:00'
            ))
            results = cursor.fetchone()
            return results

    def shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 등록  - Persistence Layer(model)) function
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
        """
            등록된 배송지 정보수 가져오기 - Persistence Layer(model)) function
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
            SELECT COUNT(*) as shipping_information_number 
            FROM shipping_informations 
            WHERE user_id=%s AND is_deleted=%s
            """
            cursor.execute(sql, (token_paylod['id'],0))
            results = cursor.fetchone()
            return results

    def lookup_shipping_information(self, token_paylod, db):
        """
            배송지 정보 가져오기 - Persistence Layer(model)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT * 
            FROM shipping_informations 
            WHERE user_id=%s AND is_deleted=%s
            """
            cursor.execute(sql, (token_paylod['id'],0))
            results = cursor.fetchall()
            return results

    def normal_shipping_information(self, token_paylod, db):
        """
            배송지 정보 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-07 (taeha7b@gmail.com (김태하) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT id
            FROM shipping_informations
            WHERE user_id=%s AND is_deleted=%s AND is_default_address=%s
            """
            cursor.execute(sql, (
                token_paylod['id'],
                0,
                0
            ))
            results = cursor.fetchone()
            return results

    def delete_shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 식제할 배송지 정보에 대한 요청
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            UPDATE shipping_informations 
            SET is_deleted=%s
            WHERE id=%s AND user_id=%s
            """
            results = cursor.execute(sql, (
            1,
            requestion['id'],
            token_paylod['id']
            ))
            return results

    def revise_shipping_information(self, token_paylod, requestion, db):
        """
            배송지 정보 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 수정할 배송지 정보의 요청
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 taeha7b@gmail.com (김태하) : 초기생성
        """
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
        """
            배송지 정보 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
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
    
    def change_default_address(self, token_paylod, requestion, normal_shipping_information, db):
        """
            일반 배송지 정보를 기본 배송지 정보 수정 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 수정할 배송지 정보에 대한 요청
                normal_shipping_information : 일반배송지의 id
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-07 (taeha7b@gmail.com (김태하)) : 쿼리문 수정
                2020-09-28 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            UPDATE shipping_informations SET
            is_default_address=%s
            WHERE id=%s AND user_id=%s AND is_default_address=%s AND is_deleted=%s
            """
            results = cursor.execute(sql, (
                1,
                normal_shipping_information['id'],
                token_paylod['id'],
                0,
                0
            ))
            return results
