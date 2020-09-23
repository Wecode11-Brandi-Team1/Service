# 작성자: 김기욱
# 수정일: 2020.09.23.수
# 스토어 검색 기능 Service

class SearchService:
    def __init__(self, search_dao, config):
        self.search_dao = search_dao
        self.config = config

    def search_stores(self, Q, limit):
        try:
            print(Q)
            search_results = self.search_dao.search_stores(Q, limit)
        except:
            raise
        else:
            return search_results