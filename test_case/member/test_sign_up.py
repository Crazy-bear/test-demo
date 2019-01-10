# encoding:utf8
import os
import sys
import re

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
        return r

    def sign_up(self, mobile_phone, loginPwd, code):
        sign_up_pars = {'mobilePhone': mobile_phone,
                        'loginPwd': loginPwd,
                        'code': code}
        r = requests.post(URL_SIGN_UP, sign_up_pars)
        return r

    @unittest.skipIf(api != 'http://test-api.tianhangbox.net', u'预发布环境跳过')
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

    def test_sign_up_mobile_phone_repeat(self):
        '''账号重复'''
        mobile_phone = '13510278188'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            self.send_msg_code(mobile_phone)
            code = self.query_msg_code(self.db, mobile_phone)[0]['code']
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('1119', r.json()['ret'])
            self.assertEqual('该账号已经存在', r.json()['msg'])
        except AssertionError:
            raise AssertionError

    def test_sign_up_all_null(self):
        '''所有参数为空'''
        mobile_phone = ''
        login_passwd = ''
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_null(self):
        '''注册 手机号为：空'''
        mobile_phone = ''
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_1(self):
        '''注册 手机号长度为：1'''
        mobile_phone = '1'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_5(self):
        '''注册 手机号长度为：5'''
        mobile_phone = '13510'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_11(self):
        '''注册 手机号长度为：11'''
        mobile_phone = '18000000002'
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

    def test_sign_up_mobile_phone_12(self):
        '''注册 手机号长度为：12'''
        mobile_phone = '180000000021'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_chinese(self):
        '''注册 手机号数据类型为：中文'''
        mobile_phone = '手机号'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_english(self):
        '''注册 手机号数据类型为：英文'''
        mobile_phone = 'QRWQER'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_special(self):
        '''注册 手机号数据类型为：特殊符号'''
        mobile_phone = '#$%^&'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            r = self.send_msg_code(mobile_phone)
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('请输入正确手机号', r.json()['msg'])
            # print(r.json())
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_Operator_10(self):
        '''注册 运营商手机号前缀为：10'''
        mobile_phone = '10254865125'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            self.send_msg_code(mobile_phone)
            code = self.query_msg_code(self.db, mobile_phone)[0]['code']
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('手机号格式错误', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_Operator_11(self):
        '''注册 运营商手机号前缀为：11'''
        mobile_phone = '11254865121'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            self.send_msg_code(mobile_phone)
            code = self.query_msg_code(self.db, mobile_phone)[0]['code']
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('手机号格式错误', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_Operator_12(self):
        '''注册 运营商手机号前缀为：12'''
        mobile_phone = '12254865121'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            self.send_msg_code(mobile_phone)
            code = self.query_msg_code(self.db, mobile_phone)[0]['code']
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('999999', r.json()['ret'])
            self.assertEqual('手机号格式错误', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_mobile_phone_Operator_telecom(self):
        '''注册 运营商中国电信号段:
        133
        141/149
        153
        173/174/177
        180/181/189
        191/199
        '''
        mobile_phone = [13323458741,
                        14112545895, 14952124587,
                        15325869521,
                        17325621458, 17452154845, 17752658741,
                        18025147854, 18125416325, 18952421545,
                        19152485214, 19963254124
                        ]
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        for i in mobile_phone:
                try:
                    self.send_msg_code(i)
                    code = self.query_msg_code(self.db, i)[0]['code']
                    r = self.sign_up(i, login_passwd_md5, code)
                    # print('sign',r.json())
                    self.assertEqual(200, r.status_code)
                    self.assertEqual('0', r.json()['ret'])
                    self.assertEqual('成功', r.json()['msg'])
                    self.assertEqual(str(i), r.json()['data']['mobilePhone'])
                    login(i, login_passwd)
                except AssertionError:
                    raise AssertionError('手机号码错误！')
                finally:
                    self.delect_member(self.db, i)

    def test_sign_up_mobile_phone_Operator_cmcc(self):
        '''注册 运营商中国移动号段:
        134/135/136/137/138/139
        144/147/148
        150/151/152/157/158/159
        178
        182/183/184/187/188
        198
        '''
        mobile_phone = [13485252651, 13511475147, 13654874125, 13789456251, 13852416545, 13954154215,
                        14452365214, 14785236951, 14852369512,
                        15023125487, 15125632658, 15236598547, 15784215412, 15854125478, 15936251454,
                        17852145214,
                        18236514587, 18365245464, 18425154862, 18724513557, 18861548535,
                        19865632547,
                        ]
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        for i in mobile_phone:
                try:
                    self.send_msg_code(i)
                    code = self.query_msg_code(self.db, i)[0]['code']
                    # 注册账号
                    r = self.sign_up(i, login_passwd_md5, code)
                    # print('sign',r.json())
                    # 断言判断是否注册成功
                    self.assertEqual(200, r.status_code)
                    self.assertEqual('0', r.json()['ret'])
                    self.assertEqual('成功', r.json()['msg'])
                    self.assertEqual(str(i), r.json()['data']['mobilePhone'])
                    # 登录账号，判断是否可以登录
                    login(i, login_passwd)
                except AssertionError:
                    raise AssertionError
                finally:
                    self.delect_member(self.db, i)

    def test_sign_up_mobile_phone_Operator_unicom(self):
        '''注册 运营商中国联通号段:
        130/131/132
        145/146
        155/156
        166
        175/176
        185/186
        '''
        mobile_phone = [13025896521, 13120254587, 13232365214,
                        14526589512, 14685212547,
                        15524258951, 15623587414,
                        16662521888,
                        17525859664, 17632584785,
                        18521478523, 18625415784
                        ]
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        for i in mobile_phone:
                try:
                    self.send_msg_code(i)
                    code = self.query_msg_code(self.db, i)[0]['code']
                    # 注册账号
                    r = self.sign_up(i, login_passwd_md5, code)
                    # print('sign',r.json())
                    # 断言判断是否注册成功
                    self.assertEqual(200, r.status_code)
                    self.assertEqual('0', r.json()['ret'])
                    self.assertEqual('成功', r.json()['msg'])
                    self.assertEqual(str(i), r.json()['data']['mobilePhone'])
                    # 登录账号，判断是否可以登录
                    login(i, login_passwd)
                except AssertionError:
                    raise AssertionError
                finally:
                    self.delect_member(self.db, i)

    def test_sign_up_login_passwd_null(self):
        '''注册 密码为：空'''
        mobile_phone = '13542158655'
        login_passwd = ''
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

    def test_sign_up_login_passwd_5(self):
        '''注册 密码数据长度为：5'''
        mobile_phone = '13542158655'
        login_passwd = '12345'
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

    def test_sign_up_login_passwd_6(self):
        '''注册 密码数据长度为：6'''
        mobile_phone = '13542158655'
        login_passwd = 'a12345'
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

    def test_sign_up_login_passwd_10(self):
        '''注册 密码数据长度为：10'''
        mobile_phone = '13542158655'
        login_passwd = 'asd1234567'
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

    def test_sign_up_login_passwd_16(self):
        '''注册 密码数据长度为：16'''
        mobile_phone = '13542158655'
        login_passwd = 'asd123456789ASD6'
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

    def test_sign_up_login_passwd_17(self):
        '''注册 密码数据长度为：17'''
        mobile_phone = '13542158655'
        login_passwd = 'asd123456789ASD67'
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

    def test_sign_up_login_passwd_chinese(self):
        '''注册 密码数据类型为：中文'''
        mobile_phone = '13542158655'
        login_passwd = '这是密码'
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

    def test_sign_up_login_passwd_english(self):
        '''注册 密码数据类型为：英文字母'''
        mobile_phone = '13542158655'
        login_passwd = 'english'
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

    def test_sign_up_login_passwd_special(self):
        '''注册 密码数据类型为：特殊字符'''
        mobile_phone = '13542158655'
        login_passwd = '￥%&&#'
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

    def test_sign_up_verification_Code_null(self):
        '''注册 验证码为：空'''
        mobile_phone = '13542158655'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            code = ''
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('1018', r.json()['ret'])
            self.assertEqual('验证码输入错误', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)

    def test_sign_up_verification_Code_error(self):
        '''注册 错误验证码'''
        mobile_phone = '13542158655'
        login_passwd = '123456'
        login_passwd_md5 = md5_encryption(login_passwd)
        try:
            code = '121212'
            r = self.sign_up(mobile_phone, login_passwd_md5, code)
            # print('sign',r.json())
            self.assertEqual(200, r.status_code)
            self.assertEqual('1018', r.json()['ret'])
            self.assertEqual('验证码输入错误', r.json()['msg'])
        except AssertionError:
            raise AssertionError
        finally:
            self.delect_member(self.db, mobile_phone)


if __name__ == '__main__':
    unittest.main()
