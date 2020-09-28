import traceback

class QuestionService:
    def __init__(self, question_dao):
        self.question_dao = question_dao
    
    def get_questions(self, params, db):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
        Returns:
            questions객체(상품아이디에 매칭되는 문의글리스트)
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            questions = self.question_dao.get_questions(params, db)

        except :
            traceback.print_exc()
       
        else :
            return questions

    def insert_question(self, product_id, q_info, db):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
            q_info     : jsondata request(추가요청)
        Returns:
            None
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            self.question_dao.insert_question(product_id, q_info, db)
    
        except :
            traceback.print_exc()
    
    def delete_question(self, product_id, q, db):
        """
        Args:
            service    : 서비스 레이어 객체
            product_id : 상품아이디
            q_info     : jsondata request(삭제요청)
        Returns:
            None
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-04(김기욱) : 초기 생성
        """
        try :
            self.question_dao.delete_question(product_id, q, db)
       
        except :
            traceback.print_exc()