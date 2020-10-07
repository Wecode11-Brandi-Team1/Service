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
            if coupons is None :
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