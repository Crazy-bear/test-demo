# encoding:utf8
import pymysql
import configparser
import os
from sys import argv

if 'Win' in os.environ['os'] and len(argv) == 1:
    key_word = 'test'
elif len(argv) >= 2:
    if 'test' in argv[-1]:
        key_word = 'test'

    elif 'yufabu' in argv[-1]:
        key_word = 'yufabu'

    else:
        raise ValueError

dir_database_config_ini = os.path.dirname(os.path.abspath(__file__)) + '/database_config.ini'
f = configparser.ConfigParser()
f.read(dir_database_config_ini)
HOST = f.get(key_word, 'host')
print('DB_HOST:', HOST)
PORT = int(f.get(key_word, 'port'))
USER = f.get(key_word, 'user')
PASSWORD = f.get(key_word, 'password')
DB = f.get(key_word, 'db')


#
class MySqlDatabase():

    def __init__(self):
        self.connect = self.connect_mysql()

    def connect_mysql(self):
        try:
            connect = pymysql.connect(host=HOST,
                                      port=PORT,
                                      user=USER,
                                      password=PASSWORD,
                                      db=DB,
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


    def query_member_info(db, pars):
        sql = "SELECT username , mobile_phone , loginpsw from member where member_level='%s' and credit_employee_id_ ='%s' and create_time >= 1519797350381" % (
            pars)
        return db.query_rows(sql, size=1)


    pars = ('10', '0')
    print(query_member_info(db, pars))
