# encoding:utf8
import pymysql
from pprint import pprint


# 创建一个MySqlDatebase类
class MySqlDatabase():

    # 打包连接数据库的信息
    def __init__(self):
        self.host = '47.104.109.157'
        self.port = 3309
        self.user = 'test_rw'
        self.password = 'l8@4v2Oet@U47cs'
        self.db = 'th_testdb'
        self.charset = 'utf8'
        self.connect = self.connect_mysql()

    # 利用try...except...抛出异常来判断是否连接成功
    def connect_mysql(self):
        try:
            connect = pymysql.connect(host=self.host,
                                      port=self.port,
                                      user=self.user,
                                      password=self.password,
                                      db=self.db,
                                      charset='utf8',
                                      cursorclass=pymysql.cursors.DictCursor)
            return connect
        except pymysql.err.OperationalError as msg:
            print(msg)

    def query_rows(self, sql, pars=None, size=None):
        result = None
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql, pars)
            if size == None:
                result = cursor.fetchall()
            elif int(size) == 1:
                result = cursor.fetchone()
            elif int(size) > 1:
                result = cursor.fetchmany()
            else:
                print('size参数错误')
        except ValueError as msg:
            raise ValueError('参数异常')
        self.connect.commit()
        return result

    def update(self, sql):
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            self.connect.commit()
        except Exception as msg:
            print(msg)
            self.connect.rollback()

    def delete(self, sql):
        try:
            cursor = self.connect.cursor()
            cursor.execute(sql)
            self.connect.commit()
        except Exception as msg:
            print(msg)
            self.connect.rollback()


if __name__ == '__main__':
    db = MySqlDatabase()
    sql1 = 'select * from member where mobile_phone="13286993500"'
    sql2 = 'select * from member where mobile_phone="13286993501"'
    l = [sql1, sql2]
    for i in l:
        print(db.query_rows(i))
