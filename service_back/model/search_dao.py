import pymysql
from connection import get_connection

# 작성자: 김기욱
# 작성일: 2020.09.22.화
# Sellers와 연결된 Class
class SearchDao:
    def __init__(self, db):
        self.db = db
    
    def search_stores(self, Q, limit):
        try:
            db     = get_connection(self.db)
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql = """
            SELECT 
                id,
                profile_image,
                korean_name
            FROM
                sellers 
            WHERE
                korean_name LIKE %s
            LIMIT
                %s;
            """
            print(sql)
            cursor.execute(sql, ('%' + Q + '%', int(limit)))
            result = cursor.fetchall()
        
        except:
            db.rollback()
            raise

        else:
            return result
        
        finally:
            cursor.close()
            db.close()