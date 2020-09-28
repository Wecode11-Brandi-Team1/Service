from .product_view import (
    MainProductsView, 
    ProductsView,
    CategorySetView)
from .search_view  import SearchView
from .user_view    import SignUp, SignIn, SocialSignUp, SocialSignIn, ShippingInformation

def create_endpoints(app, services):
    
    product_service = services.product_service
    search_service  = services.search_service
    user_service    = services.user_service
    # 작성자: 김기욱
    # 수정일: 2020.09.25 금
    # 카테고리 endpoint 추가

    # 수정일: 2020.09.23 수
    # 검색 endpoint 추가
    
    # 작성일: 2020.09.22.화
    # 상품 리스트 데이터 endpoint 추가
    app.add_url_rule('/home', view_func = MainProductsView.as_view('mainproducts', product_service))
    app.add_url_rule('/products', view_func = ProductsView.as_view('products', product_service))
    app.add_url_rule('/category', view_func=CategorySetView.as_view('category_set', product_service))
    app.add_url_rule('/search', view_func=SearchView.as_view('search', search_service))
    # 작성자: 김태하
    # 작성일: 2020.09.23.수
    # 기능: 회원가입
    app.add_url_rule('/sign-up', view_func = SignUp.as_view('user_sign_up', user_service))
    app.add_url_rule('/sign-in', view_func = SignIn.as_view('user_sign_in', user_service))
    app.add_url_rule('/social-signup', view_func = SocialSignUp.as_view('user_social_sign_up', user_service))    
    app.add_url_rule('/social-signin', view_func = SocialSignIn.as_view('user_social_sign_in', user_service))
    app.add_url_rule('/shipping-information', view_func = ShippingInformation.as_view('shipping_information', user_service))