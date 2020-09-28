import pymysql
import traceback

class ProductDao:
    def get_most_sold_products(self, db):
        """
        Args :
            db : 데이터베이스 연결 객체
        Returns :
            판매량 100개 이상 상품 리스트(10개)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-28 : None값 예외처리 추가
            2020-09-22 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT DISTINCT
                    si.korean_name as seller_name,
                    p.id as product_id,
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
                    sellers s,
                    seller_informations si
                WHERE 
                    p.seller_id = s.id
                    AND si.seller_id = s.id
                    AND pi.product_id = p.id
                    AND pd.product_id = p.id
                    AND pi.ordering = 1
                    AND p.is_deleted = 0 
                    AND p.sale_amount > 100
                LIMIT
                    10;
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                if not result:
                    raise Exception('Query failed')
        
        except :
            traceback.print_exc()
        
        else :
            return result

    def get_discounted_products(self, db):
        """
        Args :
            db : 데이터베이스 연결 객체
        Returns :
            할인률 존재하는 상품 리스트(10개)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-28 : None값 예외처리 추가
            2020-09-22 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """  
                SELECT DISTINCT
                    si.korean_name as seller_name,
                    p.id as product_id,
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
                    sellers s,
                    seller_informations si
                WHERE 
                    p.seller_id = s.id
                    AND si.seller_id = s.id
                    AND pi.product_id = p.id
                    AND pd.product_id = p.id
                    AND pi.ordering = 1
                    AND p.is_deleted = 0 
                    AND pd.discount_rate > 0
                LIMIT
                    10;
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                if not result:
                    raise Exception('Query failed') 
        
        except :
            traceback.print_exc()
        
        else :
            return result

    def get_cateogory_set(self, q, db):
        """
        Args :
            db : 데이터베이스 연결 객체
            q  : 쿼리파라미터(셀러속성 아이디)
        Returns :
            셀러속성에 매칭되는 퍼스트/세컨드카테고리 리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-28 : None값 예외처리 추가
            2020-09-26 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
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
                cursor.execute(sql, q)
                result = cursor.fetchall()
                
                if not result:
                    raise Exception('Query failed') 

        except :
             traceback.print_exc()
        
        else :
            return result

    def get_products(self, params, db):
        """
        Args :
            db      : 데이터베이스 연결 객체
            params  : 딕셔너리 패킹된 쿼리파라미터
        Returns :
            필터링 적용된 전체 상품리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-28 : None값 예외처리 추가
            2020-09-27 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT DISTINCT
                    si.korean_name as seller_name,
                    p.id as product_id,
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
                    seller_informations si,
                    seller_properties sp,
                    first_category_second_categories as fcsc
                WHERE 
                    p.seller_id = s.id
                    AND si.seller_id = s.id
                    AND si.seller_property_id = sp.id
                    AND p.id = pi.product_id
                    AND p.id = pd.product_id
                    AND p.categories_id = fcsc.id
                    AND pi.ordering = 1
                    AND p.is_deleted = 0
                """

                # seller property
                if params['sp_id']:
                    sql += f" AND sp.id = {params['sp_id']}"

                # first category
                if params['fc_id']:
                    sql += f" AND fcsc.first_category_id = {params['fc_id']}"

                # second category
                if params['sc_id']:
                    sql += f" AND fcsc.second_category_id = {params['sc_id']}"

                # discounted(세일상품)
                if params['is_discounted']:
                    sql += " AND pd.discount_rate > 0"

                # order by popularity(인기순정렬) 
                if params['is_popular']:
                    sql += " ORDER BY p.sale_amount DESC"   

                # order by brand new(최신순정렬)
                if params['is_new']:
                    sql += " ORDER BY p.register_date DESC"  
                
                # order by cheapest(가격순정렬)
                if params['is_cheap']:
                    sql += " ORDER BY pd.sale_price ASC"  

                # Pagination
                if params['limit']:
                    sql += f" LIMIT {params['limit']}"

                if params['offset']:
                    sql += f" OFFSET {params['offset']}"

                cursor.execute(sql+";", params)
                result = cursor.fetchall()

                if not result:
                    raise Exception('Query failed')
            
        except :
             traceback.print_exc()
        
        else :
            return result
    
    def get_product(self, product_id, db):
        """
        Args :
            db          : 데이터베이스 연결 객체
            product_id  : 상품아이디
        Returns :
            상품아이디와 매칭되는 상품데이터
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-09-29 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                product = """
                SELECT 
                    si.korean_name as seller_name,
                    p.id as product_id,
                    p.sale_amount,
                    pd.name as product_name,
                    pd.discount_rate,
                    pd.sale_price,
                    pd.description,
                    pd.sale_price*((100-pd.discount_rate)/100) as discounted_price
                FROM 
                    products p,
                    product_details pd,
                    sellers s,
                    seller_informations si
                WHERE 
                    p.seller_id = s.id
                    AND si.seller_id = s.id
                    AND p.id = pd.product_id
                    AND p.is_deleted = 0
                    AND p.id = %s; 
                """

                image = """
                SELECT 
                    pi.image_path
                FROM 
                    product_images pi,
                    products p
                WHERE
                    pi.product_id = p.id
                    AND p.id = %s;
                """
                
                options = """
                SELECT 
                    colors.name as color,
                    sizes.name as size,
                    opt.stock,
                    opt.id as option_id
                FROM
                    products p,
                    options opt,
                    colors,
                    sizes
                WHERE
                    p.id = opt.product_id
                    AND colors.id = opt.color_id 
                    AND sizes.id = opt.size_id
                    AND p.id = %s;
                """
                product = cursor.execute(product, product_id)
                product = cursor.fetchone()

                images = cursor.execute(image, product_id)
                images = cursor.fetchall()
                images = [image["image_path"] for image in images]

                options = cursor.execute(options, product_id)
                options = cursor.fetchall()
            
                product["image_path"] = images
                product["option"] = options
                product["discounted_price"] = int(product["discounted_price"])
               
        except :
             traceback.print_exc()
        
        else :
            return product
