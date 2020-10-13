import pymysql

class PurchaseDao:
    def order_number_getter(self, db):
        """
            상품구매 - Persistence Layer(model) function
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
            상품구매 - Persistence Layer(model) function
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
            상품구매 - Persistence Layer(model) function
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
            상품구매 - Persistence Layer(model) function
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
            상품구매 - Persistence Layer(model) function
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

    def order_status(self, order_id, db):
        """
            주문이후에 주문상황 내역에 결재완료 추가 - Persistence Layer(model) function
            Args : 
                order_id : 주문 옵션 아이디
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            INSERT INTO order_status_modification_histories (
                order_detail_id,
                updated_at,
                order_status_id
            ) VALUES (
                (SELECT id from order_details WHERE order_id = %s ORDER BY id DESC LIMIT 1),
                NOW(),
                %s
            )
            """
            results = cursor.execute(sql, (
                order_id['id'],
                1
            ))
            return results

    def my_name(self, token_paylod, db):
        """
            마이페이지에 보여줄 유저이름 가져오기 - Persistence Layer(model)) function
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
            SELECT name as user_name FROM user_informations WHERE user_id = %s
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchone()
            return results
    
    def my_orders(self, token_paylod, db):
        """
            마이페이지에 보여줄 orders테이블의 기본키, 주문번호, 주문날짜가져오기 - Persistence Layer(model) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT id, order_number, order_date FROM orders WHERE user_id = %s
            """
            cursor.execute(sql, (token_paylod['id']))
            results = cursor.fetchall()
            return results

    def my_order_detail(self, my_orders, db):
        """
            order_details테이블의 기본키, 주문 상세번호, 주문상태, 옵션id, 주문개수, 결재 금액 가져오기 - Persistence Layer(model) function
            Args :
                my_orders : 주문 번호
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT id AS order_detail_id, order_detail_number, order_detail_statuses_id, option_id, quantity, final_price 
            FROM order_details WHERE order_id = %s
            """
            cursor.execute(sql, (my_orders))
            results = cursor.fetchall()
            return results

    def my_order_options(self, option_id, db):
        """
            옵션아이디로 부터 색상, 사이즈, 상품id 가져오기  - Persistence Layer(model) function
            Args :
                option_id : 주문 옵션 아아디
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT color_id, size_id, product_id FROM options WHERE id = %s
            """
            cursor.execute(sql, (option_id))
            results = cursor.fetchone()
            return results

    def product_color(self, color_id, db):
        """
            상품 아이디로 부터 상품 색상 가져오기  - Persistence Layer(model) function
            Args :
                color_id : 색상 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT name AS color FROM colors WHERE id = %s
            """
            cursor.execute(sql, (color_id))
            results = cursor.fetchone()
            return results

    def product_size(self, size_id, db):
        """
            상품 아이디로 부터 상품 사이즈 가져오기  - Persistence Layer(model) function
            Args :
                size_id :  상품 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT name AS size FROM sizes WHERE id = %s
            """
            cursor.execute(sql, (size_id))
            results = cursor.fetchone()
            return results

    def product_image(self, product_id, db):
        """
            상품 아이디로 부터 상품 이미지 가져오기  - Persistence Layer(model) function
            Args :
                product_id :  상품 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT image_path AS images FROM product_images WHERE product_id = %s
            """
            cursor.execute(sql, (product_id))
            results = cursor.fetchall()
            return results

    def product_name(self, product_id, db):
        """
            상품 아이디로 부터 상품 이름 가져오기  - Persistence Layer(model) function
            Args :
                product_id :  상품 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT name AS product_name FROM product_details WHERE product_id = %s
            """
            cursor.execute(sql, (product_id))
            results = cursor.fetchone()
            return results

    def seller_name(self, product_id, db):
        """
            상품 아이디로 부터 셀러 이름 가져오기  - Persistence Layer(model) function
            Args :
                product_id :  상품 기본키
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-11 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT korean_name as seller_name FROM seller_informations WHERE seller_id = (SELECT seller_id FROM products WHERE id = %s)
            """
            cursor.execute(sql, (product_id))
            results = cursor.fetchone()
            return results

    def check_order_status(self, order_detail_number, db):
        """
            상품 주문 상태 확인하기 - Persistence Layer(model) function
            Args :
                order_detail_number : 주문 상세 번호
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            SELECT order_detail_statuses_id AS status 
            FROM order_details
            WHERE order_detail_number = %s
            """
            cursor.execute(sql, (order_detail_number))
            results = cursor.fetchone()
            return results

    def order_cancellation(self, requestion, db):
        """
            상품 구매 취소하기 - Persistence Layer(model) function
            Args :
                requestion : 구매 취소에 관한 요청
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            UPDATE order_details SET order_detail_statuses_id = %s, 
            order_cancel_reason_id = %s 
            WHERE order_detail_number = %s
            """
            results = cursor.execute(sql, (
                6,
                requestion['order_cancel_reason_id'],
                requestion['order_detail_number']
            ))
            
            return results

    def refund(self, requestion, db):
        """
            환불하기 - Persistence Layer(model) function
            Args :
                requestion : 환불요청에 관한 요청
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        with db.cursor() as cursor:
            sql = """
            UPDATE order_details SET order_detail_statuses_id = %s,
            order_refund_reason_id = %s,
            order_refund_reason_description = %s 
            WHERE order_detail_number = %s;
            """
            results = cursor.execute(sql, (
                7,
                requestion['order_refund_reason_id'],
                requestion['order_refund_reason_description'],
                requestion['order_detail_number']
            ))
            return results

    def revise_status_history(self, requestion, db):
        """
            주문상태 수정 내역 추가 - Persistence Layer(model) function
            Args :
                requestion : 상품 수정에 관한 데이터
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """   
        with db.cursor() as cursor:
            sql = """
            INSERT INTO order_status_modification_histories (
                order_detail_id,
                updated_at,
                order_status_id
            ) VALUES(
                %s,
                NOW(),
                %s
            )
            """
            results = cursor.execute(sql, (
                requestion['order_detail_id'],
                requestion['order_status_id']
            ))
            return results

    def db_time(self, db):
        """
            DB time 확인 - Persistence Layer(model) function
            Args :
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-13 (taeha7b@gmail.com (김태하)) : 초기생성
        """   
        with db.cursor() as cursor:
            sql = """
            SELECT DATE_FORMAT(NOW(), '%Y%m%d') as db_today
            """
            cursor.execute(sql)
            results = cursor.fetchone()
            return results