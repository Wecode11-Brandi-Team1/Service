import pymysql
import traceback

class QuestionDao:
    def get_questions(self, params, db):
        """
        Args :
            product_id : 상품아이디
            db         : 데이터베이스 연결 객체
        Returns :
            상품아이디와 매칭되는 문의글리스트
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-04 : 포매팅형식 변경
            2020-10-03 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                qna_count = """
                SELECT p.qna_count
                FROM products p
                WHERE p.id = %s
                """
                
                sql = """
                SELECT 
                    q.id as question_id,
                    date_format(q.created_at,'%%Y.%%m.%%d') as created_at,
                    q.question_content,
                    q.is_secreted,
                    qt.name as question_type,
                    pd.name as product_name,
                    u.id as user_id,
                    SUBSTR(REGEXP_REPLACE(ui.email, '(?<=.{3}).', '*'), 1, 6) as writer,
                    si.korean_name as seller_name
                FROM 
                    questions q,
                    question_types qt,
                    users u,
                    user_informations ui,
                    products p,
                    product_details pd,
                    sellers s,
                    seller_informations si
                WHERE 
                    q.question_type_id = qt.id
                    AND q.user_id = u.id
                    AND q.product_id = p.id
                    AND ui.user_id = u.id
                    AND pd.product_id = p.id
                    AND p.seller_id = s.id
                    AND si.seller_id = s.id
                    AND p.id = %s
                    AND q.is_deleted = 0
                """
                # 내가 쓴 글 보기 필터링
                if params['u']:
                    sql += f" AND q.user_id = {params['u']}"

                sql += f" ORDER BY q.created_at DESC"
                
                if params['limit']:
                    sql += f" LIMIT {params['limit']}"

                cursor.execute(qna_count, params["product_id"])
                result = cursor.fetchone()

                if not result:
                    raise Exception('Query failed')

                cursor.execute(sql+";", params['product_id'])
                sql = cursor.fetchall()

                if not sql:
                    raise Exception('Query failed')

                result['questions'] = sql
        
        except :
            traceback.print_exc()
        
        else :
            return result
    
    def insert_question(self, params, db):
        """
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db     : 데이터베이스 연결 객체
        Returns :
            None
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-03 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                INSERT INTO questions (
                    product_id,
                    user_id,
                    question_content,
                    question_type_id,
                    updated_at,
                    is_secreted
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    now(),
                    %s  
                );
                """
                q_info = params['q_info']
                sql = cursor.execute(sql, (
                    params["product_id"],
                    q_info["user_id"],
                    q_info["question_content"],
                    q_info["question_type_id"],
                    q_info["is_secreted"]
                ))

                if not sql:
                    raise Exception('Query failed')

                count_up = """
                UPDATE products
                SET qna_count = qna_count+1
                WHERE id = %s;
                """
                count_up = cursor.execute(count_up, params["product_id"])

                if not count_up:
                    raise Exception('Query failed')

        except :
            traceback.print_exc()

    def delete_question(self, params, db):
        """
        Args :
            params : 딕셔너리 패킹된 쿼리파라미터객체
            db     : 데이터베이스 연결 객체
        Returns :
            None
        Authors :
            1218kim23@gmail.com(김기욱)
        History :
            2020-10-05 : 파라미터 형식 변경
            2020-10-04 : 초기생성
        """
        try :
            with db.cursor() as cursor:
                sql = """
                UPDATE questions 
                SET is_deleted = 1
                WHERE 
                    product_id = %s
                    AND id = %s;
                """
                sql = cursor.execute(sql, (params['product_id'], params['q']))
            
                if not sql:
                    raise Exception('Query failed')
                
                count_down = """
                UPDATE products
                SET qna_count = qna_count-1
                WHERE id = %s;
                """
                count_down = cursor.execute(count_down, params['product_id'])

                if not count_down:
                    raise Exception('Query failed')

        except :
            traceback.print_exc()