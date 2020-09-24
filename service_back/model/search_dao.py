import pymysql

# 작성자: 김기욱
# 작성일: 2020.09.22.화
# Sellers와 연결된 Class
class SearchDao:
    def search_stores(self, Q, limit, db):
        try:
            cursor = db.cursor()
            QEURY = """
            SELECT DISTINCT
                id,
                profile_image,
                korean_name
            FROM
                sellers 
            WHERE
                korean_name LIKE %s
            LIMIT
                %s;
            """ 
            cursor.execute(QEURY, ('%'+Q+'%', limit))
            result = cursor.fetchall()
        
        except:
            pass

        else:
            return result
        
        finally:
            cursor.close()

    def search_products(self, Q, limit, db):
        try:
            cursor = db.cursor()

            QEURY = """
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
                s.korean_name LIKE %s  
                OR pd.name LIKE %s 
                AND p.seller_id = s.id
                AND p.id = pi.product_id
                AND p.id = pd.product_id
                AND pi.ordering = 1
            LIMIT
                %s;
            """
            cursor.execute(QEURY, ('%'+Q+'%', '%'+Q+'%', limit))
            result = cursor.fetchall()
            #ORDER BY 적용시 쿼리 실행속도가 저하되므로 따로 ORDER BY하지않고 데이터를 뽑음
        
        except:
            pass
        
        else:
            return result
        
        finally:
            cursor.close()