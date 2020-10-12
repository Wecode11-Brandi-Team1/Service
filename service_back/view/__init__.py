from .product_view  import (
    MainProductsView, 
    ProductsView,
    ProductView,
    CategorySetView
    )
from .user_view     import (
    SignUp, 
    SignIn, 
    SocialSignUp, 
    SocialSignIn,
    ShippingInformation,
    )
from .search_view   import SearchView
from .question_view import QuestionView
from .coupon_view   import CouponView, UserCouponView
from .purchase_view import ProductPurchase

def create_endpoints(app, services):
    product_service  = services.product_service
    search_service   = services.search_service
    user_service     = services.user_service
    question_service = services.question_service
    coupon_service   = services.coupon_service
    purchase_service = services.purchase_service

    # 작성자: 김기욱
    # 기능: 상품/카테고리/검색/QNA/쿠폰
    # app.add_url_rule('/', view_func = MainProductsView.as_view('mainproducts', product_service))
    app.add_url_rule('/', view_func = MainProductsView.as_view('mainproducts', product_service))
    app.add_url_rule('/products', view_func = ProductsView.as_view('products', product_service))
    app.add_url_rule('/products/<int:product_id>', view_func = ProductView.as_view('product', product_service))
    app.add_url_rule('/category', view_func=CategorySetView.as_view('category_set', product_service))
    app.add_url_rule('/search', view_func=SearchView.as_view('search', search_service))
    app.add_url_rule('/products/<int:product_id>/questions', view_func=QuestionView.as_view('question', question_service))
    app.add_url_rule('/coupons', view_func=CouponView.as_view('coupon', coupon_service))
    app.add_url_rule('/user/coupons', view_func=UserCouponView.as_view('user_coupon', coupon_service))
    # 작성자: 김태하
    # 기능: 회원가입
    app.add_url_rule('/sign-up', view_func = SignUp.as_view('user_sign_up', user_service))
    app.add_url_rule('/sign-in', view_func = SignIn.as_view('user_sign_in', user_service))
    app.add_url_rule('/social-signup', view_func = SocialSignUp.as_view('user_social_sign_up', user_service))    
    app.add_url_rule('/social-signin', view_func = SocialSignIn.as_view('user_social_sign_in', user_service))
    app.add_url_rule('/shipping-information', view_func = ShippingInformation.as_view('shipping_information', user_service))
    app.add_url_rule('/purchase', view_func = ProductPurchase.as_view('product_purchase', purchase_service))
    # app.add_url_rule('/orders/<int:id>', view_func = MyOrder.as_view('my_order', purchase_service)) 
    # app.add_url_rule('/order-cancellation', view_func = OrderCancellation.as_view('order_cancellation', purchase_service))
    # app.add_url_rule('/refund', view_func = Refund.as_view('refund', purchase_service))