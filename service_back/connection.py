import pymysql

def get_connection(db):
    return pymysql.connect(
        host        = db['host'],
        port        = db['port'],
        user        = db['user'],
        passwd      = db['password'],
        db          = db['database'],
        charset     = db['charset'],
        cursorclass = pymysql.cursors.DictCursor,
        autocommit  = False
    )
