import pymysql
import traceback

class CouponDao:
    def get_coupons(self, db):
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
                    cd.is_limited_minimum_price,
                    cd.use_count,
                    cd.download_started_at,
                    cd.download_expired_at,
                    cd.valid_started_at,
                    cd.valid_expired_at
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
                    AND limit_count > download_count
                    AND cd.download_started_at <= NOW()
                    AND NOW() < cd.download_expired_at
                    AND cd.valid_started_at <= NOW()
                    AND NOW() < cd.valid_expired_at
                ORDER BY
                    cd.discount_price ASC;
                """
