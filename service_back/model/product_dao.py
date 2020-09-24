import pymysql

# 작성자: 김기욱
# 수정일: 2020.09.23 수
# order_by 삭제, sql limit 추가
# 작성일: 2020.09.22.화
# Product와 연결된 Class
class ProductDao:
    def get_most_sold_products(self, db):
        try :
            cursor = db.cursor()

            sql = """
            SELECT DISTINCT
                s.korean_name as seller_name,
                p.id,
                p.sale_amount,
                pi.image_path,
                pd.name as product_name,
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
                AND pi.ordering = 1
                AND p.sale_amount > 100
            LIMIT
                10;
            """
            cursor.execute(sql)
            result = cursor.fetchall()
        
        except Exception as e:
            print(f'{e}')
        
        else :
            return result
        
        finally :
            cursor.close()

    def get_discounted_products(self, db):
        try :
            cursor = db.cursor()

            sql = """  
            SELECT DISTINCT
                s.korean_name as seller_name,
                p.id,
                p.sale_amount,
                pi.image_path,
                pd.name as product_name,
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
                AND pi.ordering = 1
                AND pd.discount_rate > 0
            LIMIT
                10;
            """
            cursor.execute(sql)
            result = cursor.fetchall()
        
        except Exception as e:
            print(f'{e}')
        
        else :
            return result
        
        finally :
            cursor.close()