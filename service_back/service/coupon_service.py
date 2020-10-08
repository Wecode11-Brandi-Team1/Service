import traceback

class CouponService:
    def __init__(self, coupon_dao):
        self.coupon_dao = coupon_dao

    def get_coupons(self, db):
        """
        Args :
            coupons_dao: 쿠폰 관련 데이터접근객체
            db : 데이터베이스 연결객체
        Returns :
            coupons객체(쿠폰 리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-07 : 초기 생성
        """
        try :
            coupons = self.coupon_dao.get_coupons(db)
            if not coupons :
                coupons = "쿠폰이 존재하지 않습니다."
       
        except :
            traceback.print_exc()
       
        else :
            return coupons

    def download_coupons(self, params, db):
        """
        Args :
            coupons_dao : 쿠폰 관련 데이터접근객체
            params      : 딕셔너리 패킹된 쿼리파라미터객체
            db          : 데이터베이스 연결객체
        Returns :
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-07 : 초기 생성
        """
        try :
            self.coupon_dao.download_coupons(params, db)
            
        except :
            traceback.print_exc()
    
    def get_downloaded_coupons(self, user_id, db):
        """
        Args :
            coupons_dao : 쿠폰 관련 데이터접근객체
            user_id     : 현재 접속한 유저아이디
            db          : 데이터베이스 연결객체
        Returns :
            coupons객체(다운로드한 쿠폰 리스트)
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-09 : 초기 생성
        """
        try :
            coupon_list = self.coupon_dao.get_downloaded_coupons(user_id, db)
            if not coupon_list :
                coupons = "쿠폰이 존재하지 않습니다."
            
            else : 
                coupons = {
                "the_number_of_coupons" : len(coupon_list),
                "coupons"               : coupon_list
                }
       
        except :
            traceback.print_exc()
       
        else :
            return coupons
    
    def use_downloaded_coupons(self, params, db):
        """
        Args :
            coupons_dao : 쿠폰 관련 데이터접근객체
            params      : 딕셔너리 패킹된 쿼리파라미터객체
            db          : 데이터베이스 연결객체
        Returns :
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-08 : 초기 생성
        """
        try :
            self.coupon_dao.use_downloaded_coupons(params, db)
            
        except :
            traceback.print_exc()

    def check_downloaded_coupons(self, user_id, db):
        """
        Args :
            coupons_dao : 쿠폰 관련 데이터접근객체
            user_id     : 현재 접속한 유저아이디
            db          : 데이터베이스 연결객체
        Returns :
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-08 : 초기 생성
        """
        try :
            coupons = self.coupon_dao.check_downloaded_coupons(user_id, db)
            result  = [coupon['coupon_id'] for coupon in coupons]
            
        except :
            traceback.print_exc()

        else :
            return result

    