import pandas
import traceback

class ProductService:
    def __init__(self, product_dao):
        self.product_dao = product_dao
    
    def get_main_products(self, db):
        """
        메인페이지 상품리스트 - Business Layer(Service) function
        Args :
            product_dao: 상품 관련 데이터접근객체
            db : 데이터베이스 연결객체
        Returns :
            products객체(할인률존재상품 + 판매량높은상품)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-12 : 할인가 추가 로직 삭제(쿼리에서 받음)
            2020-10-03 : 할인가 추가 로직 변경
            2020-09-28 : 예외처리 수정(traceback 추가 *모든 함수 공통사항*)
            2020-09-22 : 초기 생성
        """
        try :
            mostsold_products   = self.product_dao.get_most_sold_products(db)
            discounted_products = self.product_dao.get_discounted_products(db)
            # 쿼리결과가 False일 경우 다음 문구로 대체
            if not mostsold_products :
                mostsold_products = "판매량 높은 상품이 존재하지 않습니다."

            if not discounted_products :
                discounted_products = "할인상품이 존재하지 않습니다."
                

            products = {
            #100개 이상 상품을 판매량이 높은 상품으로 규정하고 그 중 10개를 리스트에 넣음 
            'most_sold_products' : mostsold_products,
            #할인이 존재하는 상품 10개를 리스트에 넣음
            'discounted_products' : discounted_products
            }

        except :
            traceback.print_exc()
            raise 

        else :
            return products
        
    def get_category_set(self, q, db):
        """
        NAV/SIDE_BAR 카테고리리스트 - Business Layer(Service) function
        Args :
            product_dao: 상품 관련 데이터접근객체
            q : 쿼리파라미터(셀러속성 id)
            db : 데이터베이스 연결객체
        Returns :
            category_set객체(셀러속성에 매칭되는 1,2차 카테고리리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-27 : pandas를 사용해 ordering에 영향을 주지않고 중복제거 실행
            2020-09-23 : 초기 생성
        """
        try :
            categories      = self.product_dao.get_cateogory_set(q, db)
            seller_property = categories[0]['sp_name'] 
            # Pandas 중복제거 기능을 통해 first_cateogory의 이름을 모아놓은 리스트패킹
            fc_names  = pandas.unique([category['fc_name'] for category in categories]).tolist()
            # 쿼리스트링에 따라 매칭되는 first_category_id값 변환
            if q == 1 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+1]} 
                    for i, fc_name in enumerate(fc_names)]
                }
            if q == 4 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+12]} 
                    for i, fc_name in enumerate(fc_names)]
                }
            if q == 7 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+23]} 
                    for i, fc_name in enumerate(fc_names)]
                }

        except :
            traceback.print_exc()
            raise 
       
        else:
            return category_set
    
    def get_products(self, params, db):
        """
        전체상품 리스트(필터링있음) - Business Layer(Service) function
        Args :
            product_dao: 상품 관련 데이터접근객체
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db : 데이터베이스 연결객체
        Returns :
            products객체(필터링 적용된 전체 상품리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-12 : 할인가 추가 로직 삭제(쿼리에서 받음)
            2020-10-03 : 할인가 추가 로직 변경
            2020-09-28 : 초기 생성
        """
        try :
            product_data = self.product_dao.get_products(params, db)
            # 쿼리결과가 False일 경우 다음 문구로 대체
            if not product_data :
                product_data = "해당 카테고리에 맞는 상품이 존재하지 않습니다."
                
        except :
            traceback.print_exc()
            raise 
       
        else :
            return product_data

    def get_product(self, product_id, db):
        """
        상품 상세페이지 - Business Layer(Service) function
        Args :
            product_dao: 상품 관련 데이터접근객체
            product_id : 상품아이디
            db : 데이터베이스 연결객체
        Returns :
            product객체(상품아이디에 매칭되는 상품상세정보)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-29 : 초기 생성
        """
        try :
            product = self.product_dao.get_product(product_id, db)
        
        except :
            traceback.print_exc()
            raise 
        
        else :
            return product
    