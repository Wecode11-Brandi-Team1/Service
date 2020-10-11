import bcrypt, jwt
import requests

from config import SECRET_KEY, ALGORITHM, SOCIAL_TOKEN_URL

class PurchaseService:
    def __init__(self, purchase_dao):
        self.purchase_dao = purchase_dao

    def purchase(self, token_paylod, requestion, db):
        """
            상품구매 - Business Layer(service) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 구매하고자 하는 상품 데이터
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 여러상품 구매와 구매번호 생성 로직 변경
                2020-10-05 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        # 현재 DB 날짜 확인 ex) 20201013
        db_time_cherker = self.purchase_dao.db_time(db)
        today = db_time_cherker['db_today']
        # # 구매한 상품의 개수
        product_count = len(requestion['option_id'])

        # 최근의 주문 번호 가져오기
        recent_order_number = self.purchase_dao.order_number_getter(db)
        # 최근의 주문 상세 번호 가져오기
        recent_order_detail_number =  self.purchase_dao.detail_number_getter(db)
        # 서비스 시작후 처음 주문한 경우나 하루가 지났을 경우 기본 상품 구매번호와 상품 상세 구매번호를 0으로 설정해준다.
        if recent_order_number is None or today > recent_order_number['order_number'][:8]:
            order_number = 0
            order_detail_number = 0
            
        else:
            order_number = int(recent_order_number['order_number'][8:])
            order_detail_number = int(recent_order_detail_number['order_detail_number'][9:])
 
        requestion['order_number'] = today + str(order_number + 1).zfill(9)
        # 주문 자체는 한번 실행 되므로 order_result의 결과로 1이 반환된다. 
        order_result = self.purchase_dao.order(token_paylod, requestion, db)

        # order_result가 제대로 실행되었으면 1이다.
        if order_result == 1:
            for count_number in range(product_count):
                requestion['order_detail_number'] = 'B' + today + str(order_detail_number + count_number+1).zfill(8)
                order_id = self.purchase_dao.order_id_getter(token_paylod, db)
                order_detail_results = self.purchase_dao.order_detail(token_paylod, requestion, count_number, order_id, db)
                order_status_results = self.purchase_dao.order_status(order_id, db)
                if order_detail_results != 1 and order_status_results !=1:
                    return False             
            return True  
        return False
       
    def my_order(self, token_paylod, db):
        """
            마이페이지에 구매 정보 가져오기 - Business Layer(service) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-10 (taeha7b@gmail.com (김태하)) : 초기생성
        """

        # 실제 회원 이름 가져오기
        my_name = self.purchase_dao.my_name(token_paylod, db)

        # 마이페이지에 보여줄 orders테이블의 기본키, 주문번호, 주문날짜가져오기
        my_orders = self.purchase_dao.my_orders(token_paylod, db) 

        # 유저가 여러개의 주문을 데이터를 가지고 있으므로 주문데이터 하나씩 my_orders에 넣어주기 위해서 반복문을 돌린다.
        for order in my_orders:
            order['order_date'] = order['order_date'].strftime('%Y.%m.%d')
            order.update(my_name)
           
            # orders테이블의 기본키로 부터 주문상세 정보 가져오기
            my_order_details = self.purchase_dao.my_order_detail(order['id'], db)
            order['order_details'] = my_order_details

            # 한개의 주문에는 여러 상품을 구매 할 수 있기 때문에 반복문을 돌린다.
            for detail_count, detail in enumerate(my_order_details):

                # 옵션아이디로 부터 색상, 사이즈, 상품id 가져오기
                my_order_options = self.purchase_dao.my_order_options(detail['option_id'], db)

                # 상품 색상 가져오기
                product_color = self.purchase_dao.product_color(my_order_options['color_id'], db)
                order['order_details'][detail_count].update(product_color)

                # 상품 사이즈 가져오기
                product_size = self.purchase_dao.product_size(my_order_options['size_id'], db)
                order['order_details'][detail_count].update(product_size)

                # 상품 이미지 가져오기
                product_images = self.purchase_dao.product_image(my_order_options['product_id'], db)
                order['order_details'][detail_count].update(product_images[0])

                # 상품 이름 가져오기
                product_name = self.purchase_dao.product_name(my_order_options['product_id'], db)
                order['order_details'][detail_count].update(product_name)

                # 셀러 한글명 가져오기
                seller_name = self.purchase_dao.seller_name(my_order_options['product_id'], db)
                order['order_details'][detail_count].update(seller_name)

        return my_orders

    def order_cancellation(self, token_paylod, requestion, db):
        """
            상품 구매 취소하기 - Business Layer(service) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 취소할 상품의 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        # 결재된 상품의 상태를 가져옵니다.
        check_order_status = self.purchase_dao.check_order_status(requestion['order_detail_number'], db)
        """
        check_order_status에서 현재 주문상태를 확인해서 주문 상태가 1(결재완료) 또는 주문 상태가 2(상품준비)면 주문취소가 가능하고 
        주문상태를 주문취소완료(6)로 바꾼다.
        """
        if check_order_status['status'] in (1,2):
            requestion['order_status_id'] = 6

            # 주문 상황 변경으로 인한 주문 상황 내역 변경하기
            revise_status_history = self.purchase_dao.revise_status_history(requestion, db)
            results = self.purchase_dao.order_cancellation(requestion, db)
            return results
        
        return False

    def refund(self, token_paylod, requestion, db):
        """
            환불하기 - Business Layer(service) function
            Args : 
                token_paylod : 유저 엑세스 토큰
                requestion : 환불할 상품의 정보
                db : DATABASE Connection Instance
            Returns :

            Author :
                taeha7b@gmail.com (김태하)
            History:
                2020-10-12 (taeha7b@gmail.com (김태하)) : 초기생성
        """
        # 결재된 상품의 상태를 가져옵니다.
        check_order_status = self.purchase_dao.check_order_status(requestion['order_detail_number'], db)
        """
        check_order_status에서 현재 주문상태를 확인해서 주문 상태가 3(배송중) 또는 주문 상태가 4(배송완료)면 환불요청이 가능하고
        주문 상태를 환불요청(7)으로 바꾼다.
        """
        if check_order_status['status'] in (3,4):
            requestion['order_status_id'] = 7

            # 주문 상황 변경으로 인한 주문 상황 내역 변경하기
            revise_status_history = self.purchase_dao.revise_status_history(requestion, db)
            results = self.purchase_dao.refund(requestion, db)
            return results

        return False
