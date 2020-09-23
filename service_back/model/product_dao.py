import pymysql
from connection import get_connection

# 작성자: 김기욱
# 수정일: 2020.09.23 수
# order_by 삭제, sql limit 추가
# 작성일: 2020.09.22.화
# Product와 연결된 Class
class ProductDao:
    def __init__(self, db):
        self.db = db

    def get_products(self):
        try:
            db     = get_connection(self.db)
            cursor = db.cursor(pymysql.cursors.DictCursor)

            sql = """
            SELECT 
                s.korean_name,
                p.id,
                p.sale_amount,
                pi.image_path,
                pd.name,
                pd.discount_rate,
                pd.sale_price
            FROM 
                products p,
                product_images pi,
                product_details pd,
                sellers s
            WHERE 
                p.seller_id = s.id
                AND p.id = pi.product_id
                AND p.id = pd.product_id
                AND pi.ordering 
            LIMIT
                1000
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            #ORDER BY 적용시 쿼리 실행속도가 저하되므로 따로 ORDER BY하지않고 데이터를 뽑음
            #실제 상품수가 수십만개가 넘어가면 쿼리실행속도 문제 발생이 예측되므로 limit로 1000개만 가져옴
        
        except:
            db.rollback()
            raise
        
        else:
            return result
        
        finally:
            cursor.close()
            db.close()