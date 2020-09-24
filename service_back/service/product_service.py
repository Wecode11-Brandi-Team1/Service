# 작성자: 김기욱
# 수정일: 2020.09.26 토
# 셀러속성에 기반한 1차,2차 카테고리를 가져오는 서비스로직 구현
# 수정일: 2020.09.23.수
# ServiceClass 판매량 높은 상품과 할인상품들로 분류 후 10개씩 리스트 패킹하는 로직구현
# 작성일: 2020.09.22.화
# Product와 연결된 ServiceClass 구현
import pandas

class ProductService:
    def __init__(self, product_dao):
        self.product_dao = product_dao
    
    def get_main_products(self, db):
        try :
            mostsold_products   = self.product_dao.get_most_sold_products(db)
            discounted_products = self.product_dao.get_discounted_products(db)
            products = {
            #100개 이상 상품을 판매량이 높은 상품으로 규정하고 그 중 10개를 리스트에 넣음 
            'most_sold_products' : [{
                'id'               : product['id'],
                'image_url'        : product['image_path'], 
                'seller_name'      : product['seller_name'], 
                'product_name'     : product['product_name'], 
                'discount_rate'    : product['discount_rate'],
                'origin_price'     : product['sale_price'], 
                'discounted_price' : (lambda x,y : int(x*((100-y)/100)))(product['sale_price'],product['discount_rate']),
                'sale_amount'      : product['sale_amount']
            } for product in mostsold_products], 
            #할인이 존재하는 상품 10개를 리스트에 넣음
            'discounted_products' : [{
                'id'               : product['id'],
                'image_url'        : product['image_path'], 
                'seller_name'      : product['seller_name'], 
                'product_name'     : product['product_name'], 
                'discount_rate'    : product['discount_rate'],
                'origin_price'     : product['sale_price'], 
                'discounted_price' : (lambda x,y : int(x*((100-y)/100)))(product['sale_price'],product['discount_rate']),
                'sale_amount'      : product['sale_amount']
            } for product in discounted_products]
            }

        except Exception as e:
            print(f'Service Problem{e}')

        else :
            return products
        
    def get_category_set(self, Q, db):
        try:
            categories      = self.product_dao.get_cateogory_set(Q, db)
            seller_property = categories[0]['sp_name'] 
            # Pandas 중복제거 기능을 통해 first_cateogory의 이름을 모아놓은 리스트패킹
            fc_names  = pandas.unique([category['fc_name'] for category in categories]).tolist()
            # 쿼리스트링에 따라 매칭되는 first_category_id값 변환
            if Q == 1 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+1]} 
                    for i, fc_name in enumerate(fc_names)]
                }
            if Q == 4 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+12]} 
                    for i, fc_name in enumerate(fc_names)]
                }
            if Q == 7 :
                category_set = { 
                seller_property : [
                    {fc_name : [category['sc_name'] for category in categories if category['fc_id'] == i+22]} 
                    for i, fc_name in enumerate(fc_names)]
                }

        except Exception as e:
            print(f'Service Problem{e}')
       
        else:
            return category_set
    
    def get_products(self, params, db):
        try:
            products = self.product_dao.get_products(params, db)

        except Exception as e:
            print(f'Service Problem{e}')
       
        else:
            return products
    