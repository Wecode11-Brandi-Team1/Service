from .product_view import ProductsView
from .search_view  import SearchView

def create_endpoints(app, services):
    product_service = services.product_service
    search_service  = services.search_service

    # 작성자: 김기욱
    # 수정일: 2020.09.23 수
    # 스토어 검색 endpoint 구현
    # 작성일: 2020.09.22.화
    # 상품 전체 데이터 endpoint
    app.add_url_rule('/products', view_func = ProductsView.as_view('products', product_service))
    app.add_url_rule('/search', view_func=SearchView.as_view('search', search_service))