# encoding=utf8

import unittest
import os
import sys
from pprint import pprint
import datetime
import time
import pymysql
api_autp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_autp_path)
from common.api_url import *
from test_case.ticket.ProductBase import *

class DelProductCase(unittest.TestCase):

    def setUp(self):
        self.Base_url = 'http://yufabu-opapi.tianhangbox.com'
        self.del_product_url = self.Base_url + '/airline/product/delete'
        idlist = search_productid()
        number = idlist.__len__()
        if number > 0:
            id = idlist[0]
            self.productId = id
        else:
            self.productId = create_product_returnid()

    def tearDown(self):
        pass

    def test_delproduct_infonull(self):
        ''' 删除航司产品'''
        # count = self.productId.__len__()
        # if count == 0:
        #     self.productId = create_product_returnid()
        # else:
        #     if self.isexists_airline():
        #         clear_airline()
        # pprint(self.productId)
        clear_airline()
        data = {
            'productId': self.productId
        }
        rs = requests.post(self.del_product_url, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])

    def test_delproduct_info(self):
        ''' 删除航司产品（存在关联航线）'''
        # count = self.productId.__len__()
        # if count == 0:
        #     self.productId = create_product_returnid()
        #     if self.isexists_airline():
        #         pass
        #     else:
        #         create_airline_returnid()
        # else:
        #     if self.isexists_airline():
        #         pass
        #     else:
        #         create_airline_returnid(self.productId[0])
        # pprint(self.productId)
        idlist = search_airlineid()
        number = idlist.__len__()
        if number == 0:
           create_airline_returnid(self.productId)
        data = {
            'productId': self.productId
        }
        rs = requests.post(self.del_product_url, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('999999', result['ret'])
        self.assertEqual('需把关联的航线产品删除后,才能删除', result['msg'])