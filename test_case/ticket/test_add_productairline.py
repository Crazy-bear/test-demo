# encoding=utf8

import unittest
import os
import sys
from pprint import pprint
import pymysql
api_autp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_autp_path)
from common.api_url import *
from common.mysql_database import *
from test_case.ticket.ProductBase import *
from dateutil.relativedelta import relativedelta

m = md5()
m.update(b'123456')
encodeStr = m.hexdigest()

class AddProductAirlineCase(unittest.TestCase):

    def login(self):
        self.login_url = 'http://yufabu-opapi.tianhangbox.com/user/login'
        self.user = 'admin'
        self.pwd = encodeStr
        self.data = {'username': self.user, 'password': self.pwd}
        r = requests.post(self.login_url, self.data)
        pprint(self.data)
        result = r.json()
        self.assertEqual(200, r.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])
        self.token = result['data']['token']

    def setUp(self):
        self.Base_url = 'http://yufabu-opapi.tianhangbox.com'
        self.add_productairline_url = self.Base_url + '/product/route/add_or_update'
        self.startdate = datetime.date.today().strftime("%Y-%m-%d-%H")
        endtime = datetime.date.today() + relativedelta(months=6)
        self.enddate = endtime.strftime("%Y-%m-%d-%H")
        self.productid = search_productid()
        number = self.productid.__len__()
        if number == 0:
           self.productid = create_product_returnid()
        else:
           self.productid = self.productid[0]
        self.login()
        clear_airline()
    def tearDown(self):
        # self.cleardata()
        pass

    def test_addairline_sucess(self):
        data = {
            # 'token': '9ef0ba72-709c-4cd1-b18f-bce6e0a6bb7f',
            'token': self.token,
            'productId': self.productid,  # 航司产品id
            'lineType': 1,  # 航线类型(1 国内 2 国际)
            'tripType': 1,  # 航程类型(1 单程 2 往返程 3 多程)
            'orgCityCode': 'SZX',  # 出发城市三字码
            'arrCityCode': '',  # 到达城市三字码
            'airline': 'CZ',  # 承运二字码
            'flightNo': '',  # 航班号
            'cabinCode': 'C',  # 舱位号
            'startDate': self.startdate,
            'endDate': self.enddate,
            'enable': 1,  # 启用状态(true启用, false未启用)
            'productDesc': '产品简介',  # 产品详情
            'remark': '测试备注'
        }
        rs = requests.post(self.add_productairline_url, data)
        pprint(rs)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])

