# encoding:utf8
import os
import sys
import unittest
import pytest

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_test_path)
print(sys.path)
from common.api_url import *


# 定义LoginCase类测试登录接口
class LoginCase(unittest.TestCase):

    @pytest.mark.bvt
    def test_ordinary_member_login_success(self):
        '''冒烟测试：普通会员登陆成功'''
        mobilePhone = 13286998998
        login_pars = {'mobilePhone': mobilePhone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        id = r.json()['data']['id']
        self.assertEqual(200, r.status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(id) > 0)

    @pytest.mark.bvt
    def test_credit_member_login_success(self):
        '''冒烟测试：授信会员登陆成功'''
        mobilePhone = 17876131954
        login_pars = {'mobilePhone': mobilePhone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        id = r.json()['data']['id']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(id) > 0)

    @pytest.mark.bvt
    def test_distributor_member_login_success(self):
        '''冒烟测试：分销商登陆成功'''
        mobilePhone = 13286993500
        login_pars = {'mobilePhone': mobilePhone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        id = r.json()['data']['id']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(id) > 0)

    @pytest.mark.bvt
    def test_city_member_login_success(self):
        '''冒烟测试：城市运营商登陆成功'''
        mobilePhone = 18664818789
        login_pars = {'mobilePhone': mobilePhone, 'loginPsw': 'e10adc3949ba59abbe56e057f20f883e'}
        r = requests.post(login_url, login_pars)
        status_code = r.status_code
        ret = r.json()['ret']
        msg = r.json()['msg']
        id = r.json()['data']['id']
        self.assertEqual(200, status_code)
        self.assertEqual('0', ret)
        self.assertEqual('成功', msg)
        self.assertTrue(int(id) > 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
