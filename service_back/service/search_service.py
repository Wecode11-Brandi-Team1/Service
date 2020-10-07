import traceback

class SearchService:
    def __init__(self, search_dao):
        self.search_dao = search_dao

    def search_stores(self, params, db):
        """
        Args :
            search_dao: 검색 관련 데이터접근객체
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db : 데이터베이스 연결객체
        Returns :
            search_stores_results객체(검색어와 매칭된 셀러 리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-07 : 예외처리 수정
            2020-10-04 : 파라미터 형식 변경
            2020-09-28 : 예외처리 수정(traceback 추가 *모든 함수 공통사항*)
            2020-09-23 : 초기 생성
        """
        try :
            search_stores_results = self.search_dao.search_stores(params, db)
            if search_stores_results is None :
                search_stores_results = "검색된 스토어가 없습니다."
       
        except :
            traceback.print_exc()
       
        else :
            return search_stores_results

    def search_products(self, params, db):
        """
        Args :
            search_dao: 검색 관련 데이터접근객체
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db : 데이터베이스 연결객체
        Returns :
            search_products_results객체(검색어와 매칭된 상품 리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-07 : 예외처리 수정
            2020-10-04 : 파라미터 형식 변경
            2020-10-03 : 할인가 추가 로직 변경
            2020-09-23 : 초기 생성
        """
        try :
            search_products_results = self.search_dao.search_products(params, db)
            if search_products_results is None :
                search_products_results = '검색된 상품이 없습니다.'
            else :
                for product in search_products_results:
                    product['discounted_price'] = round(product['sale_price']*(100-product['discount_rate'])/100)
        
        except :
            traceback.print_exc()
        
        else :
            return search_products_results 