# encoding:utf8


def get_msg_code_sql(db, mobile):
    # try :
    get_msg_code_sql = 'select * from verify_code where mobile=%s order BY id DESC' % (mobile)
    return db.query_rows(get_msg_code_sql)
    # except:
    #     db.connect.rollback()
    # finally:
    #     db.connect.close()


if __name__ == '__main__':
    # print(get_msg_code_sql(13286993500)[0]['code'])
    from common.mysql_database import MySqlDatabase
    db = MySqlDatabase()
    print(get_msg_code_sql(db, 13286993500))
