import bcrypt, jwt
import requests

from datetime import datetime
from config import SECRET_KEY, ALGORITHM, SOCIAL_TOKEN_URL

class PurchaseService:
    def __init__(self, purchase_dao):
        self.purchase_dao = purchase_dao

    def purchase(self, token_paylod, requestion, db):
        """
            상품구매 - Business Layer(service)) function
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
        # 현재 날짜 확인
        today = datetime.today().strftime("%Y%m%d")
        # 최근의 주문 번호 가져오기
        recent_order_number = self.purchase_dao.order_number_getter(db)
        # 최근의 주문 상세 번호 가져오기
        recent_order_detail_number =  self.purchase_dao.detail_number_getter(db)
        results = []

        # 서비스 시작후 처음 주문한 경우나 하루가 지났을 경우 기본 상품 구매번호와 상품 상세 구매번호를 0으로 설정해준다.
        if recent_order_number == None or today > recent_order_number['order_number'][:8]:
            order_number = 0
            order_detail_number = 0
        
        else:
            order_number = int(recent_order_number['order_number'][8:])
            order_detail_number = int(recent_order_detail_number['order_detail_number'][9:])
 
        requestion['order_number'] = today + str(order_number + 1).zfill(9)
        order_result = self.purchase_dao.order(token_paylod, requestion, db)

        if order_result == 1:
            for count_number in range(len(requestion['option_id'])):
                requestion['order_detail_number'] = 'B' + today + str(order_detail_number + count_number+1).zfill(8)
                order_id = self.purchase_dao.order_id_getter(token_paylod, db)
                results.append(self.purchase_dao.order_detail(token_paylod, requestion, count_number, order_id, db))      
            return sum(results)

        return False