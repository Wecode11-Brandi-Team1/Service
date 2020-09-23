# 작성자: 김기욱
# 수정일: 2020.09.23.수
# ServiceClass 판매량 높은 상품과 할인상품들로 분류 후 10개씩 리스트 패킹하는 로직구현
# 작성일: 2020.09.22.화
# Product와 연결된 ServiceClass 구현


class ProductService:
    def __init__(self, product_dao, config):
        self.product_dao = product_dao
        self.config = config
    
    def get_products(self):
        try :
            #100개 이상 상품을 판매량이 높은 상품으로 규정하고 그 중 10개를 리스트에 넣음 
            products_data = self.product_dao.get_products()
            products = {
            'most_sold_products' : [{
                'id'               : product['id'],
                'image_url'        : product['image_path'], 
                'seller_name'      : product['korean_name'], 
                'product_name'     : product['name'], 
                'discount_rate'    : product['discount_rate'],
                'origin_price'     : product['sale_price'], 
                'discounted_price' : (lambda x,y : int(x*((100-y)/100)))(product['sale_price'],product['discount_rate']),
                'sale_amount'      : product['sale_amount']
            } for product in products_data[:10] if product.get('sale_amount') > 100], 
            #할인이 존재하는 상품 10개를 리스트에 넣음
            'discounted_products' : [{
                'id'               : product['id'],
                'image_url'        : product['image_path'], 
                'seller_name'      : product['korean_name'], 
                'product_name'     : product['name'], 
                'discount_rate'    : product['discount_rate'],
                'origin_price'     : product['sale_price'], 
                'discounted_price' : (lambda x,y : int(x*((100-y)/100)))(product['sale_price'],product['discount_rate']),
                'sale_amount'      : product['sale_amount']
            } for product in products_data[:10] if product.get('discount_rate') > 0]
            }

        except :
            pass

        else :
            return products