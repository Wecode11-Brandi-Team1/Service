import pymysql
from config import database as db

def get_connection():
    """
    View Layer에서 Request/Response받을 때 마다 DB연결 해주는 함수
    Returns :
        connection 객체 : config에서 주어진 정보에 맞는 DB랑 연결된 객체
    Authors :
        1218kim23@gmail.com(김기욱)
        taeha7b@gmail.com (김태하)
    History :
        2020-09-23 : 초기 생성
    """
    connection = pymysql.connect(
        host        = db['host'],
        port        = db['port'],
        user        = db['user'],
        password    = db['password'],
        db          = db['database'],
        charset     = db['charset'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit  = False
    )

    return connection