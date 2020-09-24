import pymysql

# 작성자: 김기욱
# 수정일: 2020.09.26
# 전체상품 및 셀러속성별 Category_set을 가져오는 메서드 구현
# 수정일: 2020.09.23 수
# order_by 삭제, sql limit 추가
# 작성일: 2020.09.22.화
# 할인상품 / 고 판매량 상품을 가져오는 메서드 구현
class ProductDao:
    def get_most_sold_products(self, db):
        try :
            cursor = db.cursor()

            QUERY = """
            SELECT DISTINCT
                s.korean_name as seller_name,
                p.id,
                p.is_deleted,
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
                AND p.is_deleted = 0 
                AND p.sale_amount > 100
            LIMIT
                10;
            """
            cursor.execute(QUERY)
            result = cursor.fetchall()
        
        except Exception as e:
            print(f'Dao Problem : {e}')
        
        else :
            return result
        
        finally :
            cursor.close()

    def get_discounted_products(self, db):
        try :
            cursor = db.cursor()

            QUERY = """  
            SELECT DISTINCT
                s.korean_name as seller_name,
                p.id,
                p.is_deleted,
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
                AND p.is_deleted = 0
                AND pd.discount_rate > 0
            LIMIT
                10;
            """
            cursor.execute(QUERY)
            result = cursor.fetchall()
        
        except Exception as e:
            print(f'Dao Problem : {e}')
        
        else :
            return result
        
        finally :
            cursor.close()

    def get_cateogory_set(self, Q, db):
        try :
            cursor = db.cursor()
            QUERY = """
            SELECT
	            fc.id AS fc_id, 
                fc.name AS fc_name, 
                sc.id AS sc_id, 
                sc.name AS sc_name, 
                sp.id AS sp_id,
                sp.name AS sp_name
            FROM 
	            seller_properties AS sp
            LEFT JOIN 
	            first_category_seller_properties AS fcsp
            ON       
	            sp.id = fcsp.seller_property_id
            LEFT JOIN
                first_categories AS fc
            ON
                fcsp.first_category_id = fc.id
            LEFT JOIN
                first_category_second_categories AS fcsc 
            ON 
                fc.id = fcsc.first_category_id
            LEFT JOIN
                second_categories as sc
            ON
                fcsc.second_category_id = sc.id
            WHERE
                sp.id = %s;
            """
            cursor.execute(QUERY, Q)
            result = cursor.fetchall()

        except Exception as e:
            print(f'Dao Problem : {e}')
        
        else :
            return result
        
        finally :
            cursor.close()

    def get_products(self, params, db):
        try :
            cursor = db.cursor()
            QUERY = """
            SELECT DISTINCT
                s.korean_name as seller_name,
                p.id,
                p.register_date,
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
                seller_properties sp,
                first_category_second_categories as fcsc
            WHERE 
                p.seller_id = s.id
                AND s.seller_property_id = sp.id
                AND p.id = pi.product_id
                AND p.id = pd.product_id
                AND p.categories_id = fcsc.id
                AND pi.ordering = 1
                AND p.is_deleted = 0
            """

            # seller property
            sp_id = params.get('sp_id', None)
            if sp_id:
                QUERY += f" AND sp.id = {sp_id}"

            # first category
            fc_id = params.get('fc_id', None)
            if fc_id:
                QUERY += f" AND fcsc.first_category_id = {fc_id}"

            # second category
            sc_id = params.get('sc_id', None)
            if sc_id:
                QUERY += f" AND fcsc.second_category_id = {sc_id}"

            # discounted(세일상품)
            if params.get('is_discounted', None):
                QUERY += " AND pd.discount_rate > 0"

            # order by popularity(인기순정렬) 
            if params.get('is_popular', None):
                QUERY += " ORDER BY p.sale_amount DESC"   

            # order by brand new(최신순정렬)
            if params.get('is_new', None):
                QUERY += " ORDER BY p.register_date DESC"  
            
            # order by cheapest(가격순정렬)
            if params.get('is_cheap', None):
                QUERY += " ORDER BY pd.sale_price ASC"  

            # Pagination
            limit = params.get('limit', None)
            if limit:
                QUERY += f" LIMIT {limit}"

            offset = params.get('offset', None)
            if offset:
                QUERY += f" OFFSET {offset}"
            QUERY += ";"
            cursor.execute(QUERY, params)
            result = cursor.fetchall()
            
        except Exception as e:
            print(f'Dao Problem : {e}')
        
        else :
            return result
        
        finally :
            cursor.close()