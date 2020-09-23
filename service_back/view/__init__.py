from .user_view import SignUp, SignIn

# 작성자: 김태하
# 작성일: 2020.09.23.수
# 기능: 회원가입
def create_endpoints(app, services):
    user_service = services.user_service

    app.add_url_rule('/sign-up', view_func = SignUp.as_view('user_sign_up', user_service))
    app.add_url_rule('/sign-in', view_func = SignIn.as_view('user_sign_in', user_service))
    
