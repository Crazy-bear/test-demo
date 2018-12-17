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

class DelProductAirlineCase(unittest.TestCase):

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
        self.del_productairline_url = self.Base_url + '/product/route/delete'
        airlineidlist = []
        productidlist = []
        results = search_airline_returndata()
        number = results.__len__()
        if number > 0:
            for row in results:
                airlineid = row[0]
                productid = row[2]
                airlineidlist.append(airlineid)
                productidlist.append(productid)
            self.productid = productidlist[0]
            self.airlineid = airlineidlist[0]
        else:
            idlist = search_productid()
            number = idlist.__len__()
            if number > 0:
                self.productid = idlist[0]
            else:
                self.productid = create_product_returnid()
            self.airlineid = create_airline_returnid(self.productid)
        self.startdate = datetime.date.today().strftime("%Y-%m-%d-%H")
        endtime = datetime.date.today() + relativedelta(months=6)
        self.enddate = endtime.strftime("%Y-%m-%d-%H")
        self.login()
    def tearDown(self):
        # self.cleardata()
        pass

    def test_deltairline_sucess(self):
        data = {
            'id': self.airlineid
        }
        rs = requests.post(self.del_productairline_url, data)
        pprint(rs)
        pprint(data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])
