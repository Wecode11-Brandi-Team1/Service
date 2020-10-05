import pymysql

class PurchaseDao:
    def order_number_getter(self, db):
        """
            상품구매 - Persistence Layer(model)) function
            Args : 
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT order_number 
            FROM orders 
            WHERE id = (SELECT MAX(id) FROM orders)
            FOR UPDATE
            """
            cursor.execute(sql)
            results = cursor.fetchone()
            return results
    
    def detail_number_getter(self, db):
        """
            상품구매 - Persistence Layer(model)) function
            Args : 
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT order_detail_number 
            FROM order_details 
            WHERE id = (SELECT MAX(id) FROM order_details)
            """
            cursor.execute(sql)
            results = cursor.fetchone()
            return results

    def order(self, token_paylod, requestion, db):
        """
            상품구매 - Persistence Layer(model)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 구매하고자 하는 상품 데이터
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            INSERT INTO orders (
                order_number,
                final_price,
                order_date,
                user_id
            ) VALUES (%s,%s,NOW(),%s)
            """
            results = cursor.execute(sql, (
                requestion['order_number'],
                requestion['total_price'],
                token_paylod['id']
            ))
            return results

    def order_id_getter(self, token_paylod, db):
        """
            상품구매 - Persistence Layer(model)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT id FROM orders
            WHERE user_id = %s
            ORDER BY id DESC LIMIT 1
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchone()
            return results

    def order_detail(self, token_paylod, requestion, count_number, order_id, db):
        """
            상품구매 - Persistence Layer(model)) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 구매하고자 하는 상품 데이터
                count_number : 여러개의 상품이 데이터가 있는 리스트의 인덱스 번호 
                order_id : orders테이블의 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            INSERT INTO order_details(
                order_id,
                order_detail_number,
                order_detail_statuses_id,
                option_id,
                quantity,
                price,
                is_comfirmed,
                order_cancel_reason_id,
                order_refund_reason_id,
                order_refund_reason_description,
                coupon_id,
                discount_price,
                final_price,
                name,
                phone_number,
                zip_code,
                address,
                detail_address,
                shipping_memo,
                orderer_name,
                orderer_phone_number,
                orderer_email
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            results = cursor.execute(sql, (
                order_id['id'],
                requestion['order_detail_number'],
                1,
                requestion['option_id'][count_number],
                requestion['quantity'][count_number],
                requestion['price'][count_number],
                0,
                None,
                None,
                None,
                requestion['coupon_id'][count_number],
                requestion['discount_price'][count_number],
                requestion['final_price'][count_number],
                requestion['name'],
                requestion['phone_number'],
                requestion['zip_code'],
                requestion['address'],
                requestion['detail_address'],
                requestion['shipping_memo'],
                requestion['orderer_name'],
                requestion['orderer_phone_number'],
                requestion['orderer_email']
            ))
            return results 