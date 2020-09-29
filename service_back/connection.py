import pymysql

def get_connection(db):
    return pymysql.connect(
        host        = db['host'],
        port        = db['port'],
        user        = db['user'],
        password    = db['password'],
        db          = db['database'],
        charset     = db['charset'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit  = False
    )