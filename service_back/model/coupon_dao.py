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
                    cd.name, 
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
                    cd.discount_price ASC;
                """

                cursor.execute(sql)
                coupons = cursor.fetchall()
                #쿠폰리스트는 None값이 반환 가능하므로 None값 예외처리 해주지 않는다

        except :
            traceback.print_exc()
        
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
            2020-10-07 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                user_get_coupon = """
                INSERT INTO user_coupons(
                    user_id,
                    coupon_id
                ) VALUES (
                    %s,
                    %s
                );
                """
                result = cursor.execute(user_get_coupon, (
                    params['user_id'],
                    params['coupon_id']
                ))

                if result:
                    count_up = """
                    UPDATE coupon_details
                    SET download_count = download_count+1
                    WHERE
                        id = %s
                        AND is_downloadable = 1
                        AND download_started_at <= NOW()
                        AND NOW() < download_expired_at;
                    """
                    count_result = cursor.execute(count_up, (params['coupon_id']))
                    
                else :
                    raise Exception('Query(download_coupons) failed')

        except :
            traceback.print_exc()