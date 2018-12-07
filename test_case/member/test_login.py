# encoding:utf8
import os
import sys

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_test_path)
print(sys.path)
from common.api_url import *
from common.mysql_database import *


class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = db
        cls.login_psw = 'e10adc3949ba59abbe56e057f20f883e'
        cls.update_password(cls, db=cls.db, pars=cls.login_psw)

    @classmethod
    def tearDownClass(cls):
        if 'yufabu' in argv[-1]:
            cls.login_psw = None
            cls.update_password(cls, db=cls.db, pars=cls.login_psw)
        # cls.db.connect.close()

    def update_password(self, db, pars):
        sql = "UPDATE member SET loginpsw='%s'" % (pars)
        return db.update(sql)

    def query_member_info(self, db, pars):
        sql = "SELECT username , mobile_phone , loginpsw from member where \
        member_level='%s' and credit_employee_id_ ='%s' and create_time >= 1541001600000 ORDER BY create_time DESC" % (
            pars)
        return db.query_rows(sql, size=1)

    def test_ordinary_member_login_success(self):
        '''冒烟测试：普通会员登陆'''
        pars = ('10', '0')
        member_info = self.query_member_info(self.db, pars)
        print('member_info:', member_info)
        mobile_phone = member_info['mobile_phone']
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(r.json()['data']['id']) > 0)

    def test_credit_member_login_success(self):
        '''冒烟测试：授信会员登陆'''
        pars = ('70', '0')
        member_info = self.query_member_info(self.db, pars)
        print('member_info:', member_info)
        mobile_phone = member_info['mobile_phone']
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}  # self.login_psw
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(r.json()['data']['id']) > 0)

    def test_distributor_member_login_success(self):
        '''冒烟测试：分销商登陆'''
        pars = ('40', '0')
        member_info = self.query_member_info(self.db, pars)
        print('member_info:', member_info)
        mobile_phone = member_info['mobile_phone']
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(r.json()['data']['id']) > 0)

    def test_city_member_login_success(self):
        '''冒烟测试：城市运营商登陆'''
        pars = ('50', '0')
        member_info = self.query_member_info(self.db, pars)
        print('member_info:', member_info)
        mobile_phone = member_info['mobile_phone']
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        print(status_code)
        ret = r.json()['ret']
        msg = r.json()['msg']
        id = r.json()['data']['id']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(id) > 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
