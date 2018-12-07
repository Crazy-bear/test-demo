# encoding:utf8
import os
import sys

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_test_path)
from common.mysql_database import *
from common.api_url import *


class SignCase(unittest.TestCase):

    def setUp(self):
        self.db = db

    def tearDown(self):
        # self.db.connect.close()
        pass

    def delect_member(self, db, mobile_phone):
        sql = "DELETE from member where mobile_phone='%s'" % (mobile_phone)
        return db.delete(sql)

    def query_msg_code(self, db, mobile_phone):
        sql = "select * from verify_code where mobile='%s' order BY id DESC" % (mobile_phone)
        return db.query_rows(sql)

    def send_msg_code(self, mobile_phone):
        code_pars = {'mobilePhone': mobile_phone}
        r = requests.post(URL_MSG_CODE, code_pars)
        self.assertEqual(200, r.status_code)

    def sign_up(self, mobile_phone, loginPwd, code):
        sign_up_pars = {'mobilePhone': mobile_phone,
                        'loginPwd': loginPwd,
                        'code': code}
        r = requests.post(URL_SIGN_UP, sign_up_pars)
        return r

    def test_sign_up_success(self):
        '''冒烟测试 注册'''
        mobile_phone = '18000000001'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            self.send_msg_code(mobile_phone)
            code = self.query_msg_code(self.db, mobile_phone)[0]['code']
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('0', r.json()['ret'])
            self.assertEqual('成功', r.json()['msg'])
            self.assertEqual(str(mobile_phone), r.json()['data']['mobilePhone'])
            login(mobile_phone, login_passwd)
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

if __name__ == '__main__':
    unittest.main()
