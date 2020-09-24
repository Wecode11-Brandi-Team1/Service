# 작성자: 김기욱
# 작성일: 2020.09.23.수
# 검색 기능 Service

class SearchService:
    def __init__(self, search_dao, product_dao):
        self.search_dao = search_dao
        self.product_dao = product_dao

    def search_stores(self, Q, limit, db):
        try:
            search_stores_results = self.search_dao.search_stores(Q, limit, db)
       
        except:
            raise
       
        else:
            return search_stores_results

    def search_products(self, Q, limit, db):
        try:
            products_data = self.search_dao.search_products(Q, limit, db)
            search_products_results  = [{
                'id'               : product['id'],
                'image_url'        : product['image_path'], 
                'seller_name'      : product['seller_name'], 
                'product_name'     : product['product_name'], 
                'discount_rate'    : product['discount_rate'],
                'origin_price'     : product['sale_price'], 
                'discounted_price' : (lambda x,y : int(x*((100-y)/100)))(product['sale_price'],product['discount_rate']),
                'sale_amount'      : product['sale_amount']
            } for product in products_data] 
        
        except:
            raise
        
        else:
            return search_products_results 
