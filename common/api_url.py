# encoding:utf8
from hashlib import md5
import requests

api = 'http://test-api.tianhangbox.net'  # 测试环境

login_url = api + '/login/appNewLogin'  # 登陆
sign_up_url = api + '/register/appRegisterSave'  # 注册接口URL

code_url = api + '/common/sendCode'  # 通用验证码接口URL

search_flights_url = api + '/order/appDomeTicketSearch'  # 国内机票-查询

invoice_save_url = api + '/invoice/save'  # PC发票管理-保存
invoice_delete_url = api + '/invoice/delete'  # PC发票管理-删除
invoice_paging_url = api + '/invoice/paging'  # PC发票管理-分页
invoice_del_url = api + '/invoice/delete'  # PC发票管理-删除
invoice_pag_url = api + '/invoice/paging'  # PC发票管理-分页

search_intFlights_url = api + '/intorder/search'  # 国际机票-查询
change_intFlights_url = api + '/intorder/change'  # 国际机票-改签
intorder_search_url = api + '/intorder/search'  # 国际机票查询接口
ticket_create_order_url = api + '/intorder/book'  # 国际票下单接口
refund_url = api + '/order/AppNewRefundSubmitServlet'  # 退票

travel_request_url = api + '/credit/add_apply_note'  # 差旅申请
employee_list_url = api + '/credit/appcreditemployee'  # 获取企业员工
employee_search_url = api + '/credit/app_all_creditemployee'  # 搜索企业员工

psg_parent_list_url = api + '/new_beneficiary/app_get_parent_beneficiary'  # 获取外部人员
psg_uninfo_list_url = api + '/new_beneficiary/app_list_un_info_beneficiary'  # 获取常用旅客不完整数据
psg_info_list_url = api + '/new_beneficiary/app_list_beneficiary'  # 获取常用旅客完整数据
psg_del_url = api + '/new_beneficiary/app_delete_beneficiary'  # 删除常用旅客
psg_search_url = api + 'new_beneficiary/app_list_find_beneficiary'  # 搜索常用乘机人
psg_list_url = api + '/new_beneficiary/app_list_beneficiary'  # 获取常用乘机人接口URL
psg_add_url = api + '/new_beneficiary/app_add_beneficiary'  # 添加乘机人接口URL


def md5_encryption(string_):
    '''

    :param string_: string
    :return: Md5 encrypted string
    '''
    if isinstance(string_, str):
        m = md5()
        m.update(b'%s' % (string_.encode('utf8')))
        encode_str = m.hexdigest()
        return encode_str
    else:
        raise TypeError('必须传入字符串类型')



def login(mobile_phone, login_psw):
    '''

    :param mobilePhone: string  user's mobile phone
    :param loginPsw:    string  user's password
    :return:            string  user's token
    '''
    login_psw = md5_encryption(login_psw)
    login_pars = {'mobilePhone': mobile_phone, 'loginPsw': login_psw}
    r = requests.post(login_url, login_pars)
    status_code = r.status_code
    ret = r.json()['ret']
    msg = r.json()['msg']
    # id = r.json()['data']['id']
    # print('login',r.json())
    try:
        assert 200 == status_code
        assert '0' == ret
        assert '成功' == msg
        # assert int(id) > 0
    except AssertionError:
        raise AssertionError('登陆失败')
    return r.json()['data']['token']



# 运用main（）方法运行用例
if __name__ == '__main__':
    login('18000000001', '123456')
    print(md5_encryption('123456'))
