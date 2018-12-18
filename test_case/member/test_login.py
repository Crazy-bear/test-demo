# encoding:utf8
import os
import sys

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_test_path)
print(sys.path)
from common.api_url import *
from common.mysql_database import db


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
        r = requests.post(URL_LOGIN, login_pars)
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
        r = requests.post(URL_LOGIN, login_pars)
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
        r = requests.post(URL_LOGIN, login_pars)
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
        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        print(status_code)
        ret = r.json()['ret']
        msg = r.json()['msg']
        # id = r.json()['data']['id']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(r.json()['data']['id']) > 0)

    def test_member_login_all_null(self):
        '''所有参数为空'''
        mobile_phone = ''
        login_psw = ''
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('1001', ret)
        self.assertEqual('手机号码不能为空', msg)

    def test_member_login_mobile_phone_effective(self):
        '''账号 有效；密码 有效'''
        mobile_phone = '13510278155'
        login_psw = '123456'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)

    def test_member_login_mobile_phone_effective_1(self):
        '''账号 有效；密码 无效'''
        mobile_phone = '13510278155'
        login_psw = '145236'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('16164', ret)
        self.assertEqual('密码错误', msg)

    def test_member_login_mobile_phone_effective_2(self):
        '''账号 有效；密码 空'''
        mobile_phone = '13510278155'
        login_psw = ''
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('16164', ret)
        self.assertEqual('密码错误', msg)

    def test_member_login_mobile_phone_ineffective(self):
        '''账号 无效；密码 有效'''
        mobile_phone = '13510284555'
        login_psw = '123456'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('16163', ret)
        self.assertEqual('该账号不存在', msg)

    def test_member_login_mobile_phone_ineffective_1(self):
        '''账号 无效；密码 无效'''
        mobile_phone = '13510284555'
        login_psw = '￥@#中文'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('16163', ret)
        self.assertEqual('该账号不存在', msg)

    def test_member_login_mobile_phone_ineffective_2(self):
        '''账号 无效；密码 空'''
        mobile_phone = '13510284555'
        login_psw = ''
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('16163', ret)
        self.assertEqual('该账号不存在', msg)

    def test_member_login_mobile_phone_null(self):
        '''账号 空；密码 有效'''
        mobile_phone = ''
        login_psw = '123456'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('1001', ret)
        self.assertEqual('手机号码不能为空', msg)

    def test_member_login_mobile_phone_null_1(self):
        '''账号 空；密码 无效'''
        mobile_phone = ''
        login_psw = '中文123'
        login_psw_md5 = md5_encryption(login_psw)
        login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw_md5}

        r = requests.post(URL_LOGIN, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        self.assertEqual(200, status_code)
        self.assertEqual('1001', ret)
        self.assertEqual('手机号码不能为空', msg)


if __name__ == '__main__':
    unittest.main(verbosity=2)
