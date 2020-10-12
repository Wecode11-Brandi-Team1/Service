import traceback, re

class QuestionService:
    def __init__(self, question_dao):
        self.question_dao = question_dao
    
    def get_questions(self, params, db):
        """
        Args:
            service : 서비스 레이어 객체
            params  : 딕셔너리 패킹된 쿼리파라미터객체
        Returns:
            questions객체(상품아이디에 매칭되는 문의글리스트)
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-12(김기욱) : 예외처리 추가
            2020-10-05(김기욱) : 아이디마스킹 및 비밀글처리 로직 추가
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            questions = self.question_dao.get_questions(params, db)
            if questions :
                for question in questions['questions']:
                    # 현재 로그인한 유저가 아닌 비밀글들 비밀글 처리
                    if question['is_secreted'] != 0 and params['user_id'] != question['user_id']:
                        question['question_content'] = "비밀글입니다."
                    
                    # 아이디 마스킹(문자열에서 3번째 자리 이후로 *표시, 전체 글자수는 6자 제한)
                    question['writer'] = re.sub('(?<=.{3}).', '*', question['writer'])[:6]
            
            else:
                questions = "등록된 상품문의가 없습니다."

        except :
            traceback.print_exc()
            raise 
       
        else :
            return questions

    def insert_question(self, params, db):
        """
        Args:
            service : 서비스 레이어 객체
            params  : 딕셔너리 패킹된 쿼리파라미터객체
        Returns:
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-12(김기욱) : 예외처리 추가
            2020-10-05(김기욱) : 파라미터 형식 변경
            2020-10-03(김기욱) : 초기 생성
        """
        try :
            self.question_dao.insert_question(params, db)
            
        except :
            traceback.print_exc()
            raise 
    
    def delete_question(self, params, db):
        """
        Args:
            service : 서비스 레이어 객체
            params  : 딕셔너리 패킹된 쿼리파라미터객체 
        Returns:
        Author:
            김기욱(1218kim23@gmail.com)
        History:
            2020-10-12(김기욱) : 예외처리 추가
            2020-10-05(김기욱) : 파라미터 형식 변경
            2020-10-04(김기욱) : 초기 생성
        """
        try :
            self.question_dao.delete_question(params, db)
       
        except :
            traceback.print_exc()
            raise 