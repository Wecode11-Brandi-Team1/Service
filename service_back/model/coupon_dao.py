import pymysql
import traceback

class CouponDao:
    def get_coupons(self, db):
        """
        Args :
            db : 데이터베이스 연결 객체
        Returns :
            쿠폰리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-07 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT 
                    c.id as coupon_id,
                    ct.name as coupon_type,
                    ci.name as coupon_issue,
                    cd.name as coupon_name, 
                    cd.discount_price,
                    cd.minimum_price,
                    cd.use_count,
                    date_format(cd.download_started_at,'%Y.%m.%d') as download_started_at,
                    date_format(cd.download_ended_at,'%Y.%m.%d') as download_ended_at,
                    date_format(cd.valid_started_at,'%Y.%m.%d %H:%m') as valid_started_at,
                    date_format(cd.valid_ended_at,'%Y.%m.%d %H:%m') as valid_ended_at
                FROM 
                    coupons c,
                    coupon_details cd,
                    coupon_types ct,
                    coupon_issues ci
                WHERE
                    cd.coupon_id = c.id
                    AND cd.coupon_type_id = ct.id
                    AND cd.coupon_issue_id = ci.id
                    AND is_downloadable = 1
                    AND (limit_count IS NULL OR limit_count > download_count)
                    AND cd.download_started_at <= NOW()
                    AND NOW() < cd.download_ended_at
                    AND cd.valid_started_at <= NOW()
                    AND NOW() < cd.valid_ended_at
                ORDER BY
                    cd.discount_price DESC;
                """
                cursor.execute(sql)
                coupons = cursor.fetchall()
                #쿠폰리스트는 None값이 반환 가능하므로 None값 예외처리 해주지 않는다

        except :
            traceback.print_exc()
            raise
        
        else :
            return coupons

    def download_coupons(self, params, db):
        """
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체 
            db     : 데이터베이스 연결 객체
        Returns :
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-09 : 다운로드횟수 카운팅 SQL trigger 추가
            2020-10-07 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                INSERT INTO user_coupons(
                    user_id,
                    coupon_id
                ) VALUES (
                    %s,
                    %s
                );
                """
                result = cursor.execute(sql, (
                    params['user_id'],
                    params['coupon_id']
                ))

        except :
            traceback.print_exc()
            raise Exception('INVALID COUPON ID')

    def get_downloaded_coupons(self, user_id, db):
        """
        Args :
            user_id : 유저아이디
            db      : 데이터베이스 연결 객체
        Returns :
            다운로드 받은 쿠폰리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-08 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT 
                    c.id as coupon_id,
                    cd.name as coupon_name, 
                    cd.discount_price,
                    cd.minimum_price,
                    date_format(cd.valid_started_at, '%%Y.%%m.%%d') as valid_started_at,
                    date_format(cd.valid_ended_at, '%%Y.%%m.%%d') as valid_ended_at
                FROM 
                    coupons c,
                    coupon_details cd,
                    user_coupons uc
                WHERE
                    cd.coupon_id = c.id
                    AND uc.coupon_id = c.id
                    AND uc.user_id = %s
                    AND uc.is_deleted = 0
                ORDER BY
                    cd.valid_ended_at ASC,
                    cd.discount_price DESC;
                """

                cursor.execute(sql, user_id)
                coupons = cursor.fetchall()
                #쿠폰리스트는 None값이 반환 가능하므로 None값 예외처리 해주지 않는다

        except :
            traceback.print_exc()
        
        else :
            return coupons

    def use_downloaded_coupons(self, params, db):
        """
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체 
            db     : 데이터베이스 연결 객체
        Returns :
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-09 : 사용횟수 카운팅 SQL trigger 추가
            2020-10-08 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                UPDATE user_coupons 
                SET is_deleted = 1
                WHERE 
                    user_id = %s
                    AND coupon_id = %s;
                """
                sql = cursor.execute(sql, (params['user_id'], params['coupon_id']))
                # None값이 발생하면 ERROR이므로 reraise 실행
                if not sql :
                    raise Exception('INVALID COUPON ID')

        except :
            traceback.print_exc()
            raise 

    def check_downloaded_coupons(self, user_id, db):
        """
        Args :
            user_id : 유저아이디
            db      : 데이터베이스 연결 객체
        Returns :
            다운로드 받은 쿠폰리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-08 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                SELECT 
                    uc.coupon_id 
                FROM 
                    user_coupons uc
                WHERE
                    uc.user_id = %s;
                """
                cursor.execute(sql, user_id)
                result = cursor.fetchall()
                #쿠폰리스트는 None값이 반환 가능하므로 None값 예외처리 해주지 않는다

        except :
            traceback.print_exc()
            raise
        
        else :
            return result