import pymysql
import traceback

class SearchDao:
    def search_stores(self, params, db):
        """
        스토어 검색 - Persistence Layer(Model) function
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db     : 데이터베이스 연결 객체
        Returns :
            쿼리파라미터와 매칭되는 스토어 검색결과 리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-04 : 파라미터 형식 변경
            2020-10-03 : 쿼리문 변경 
            2020-09-28 : 예외처리 수정(traceback 추가 *모든 함수 공통사항*)
            2020-09-22 : 초기 생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT DISTINCT
                    s.id as seller_id,
                    si.profile_image,
                    si.korean_name as seller_name
                FROM
                    sellers s,
                    seller_informations si
                WHERE
                    s.id = si.seller_id
                    AND si.korean_name LIKE %s
                LIMIT
                    %s;
                """ 
                cursor.execute(sql,('%'+params['q']+'%', params['limit']))
                result = cursor.fetchall()
                #검색기능은 None값이 반환 가능하므로 따로 예외처리 해주지 않는다

        except :
            traceback.print_exc()

        else :
            return result

    def search_products(self, params, db):
        """
        상품 검색 - Persistence Layer(Model) function
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db     : 데이터베이스 연결 객체
        Returns :
            쿼리파라미터와 매칭되는 상품 검색결과 리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-04 : 파라미터 형식 변경
            2020-10-03 : 쿼리문 변경
            2020-09-22 : 초기 생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT DISTINCT
                    si.korean_name as seller_name,
                    p.id as product_id,
                    p.sale_amount,
                    pi.image_path,
                    pd.name as product_name,
                    pd.discount_rate,
                    pd.sale_price
                FROM 
                    products p,
                    product_images pi,
                    product_details pd,
                    sellers s,
                    seller_informations si
                WHERE 
                    si.seller_id = s.id
                    AND p.seller_id = s.id
                    AND pi.product_id = p.id
                    AND pd.product_id = p.id
                    AND pi.ordering = 1
                    AND (si.korean_name LIKE %s OR pd.name LIKE %s)
                LIMIT
                    %s;
                """
                cursor.execute(sql,('%'+params['q']+'%', '%'+params['q']+'%', params['limit']))
                result = cursor.fetchall()
                #검색기능은 None값이 반환 가능하므로 따로 예외처리 해주지 않는다
        
        except :
            traceback.print_exc()
        
        else :
            return result