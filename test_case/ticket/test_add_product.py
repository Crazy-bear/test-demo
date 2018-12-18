# encoding=utf8

import unittest
import os
import sys
from pprint import pprint
import pymysql
import requests
api_auto_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_path)
from test_case.ticket.ProductBase import *

class AddProductCase(unittest.TestCase):


    # def cleardata(self):
    #     self.db = pymysql.connect(host='47.104.205.172',
    #                               port=43309,
    #                               user='th_box_rw',
    #                               password='@6m1WrJxqTv3@3VpBhEa!n1qDdGe8UJf',
    #                               db='th_box',
    #                               charset='utf8')
    #     self.cursor = self.db.cursor()
    #     sqlquery = "delete from airline_product where id>12"
    #     try:
    #         rows1 = self.cursor.execute(sqlquery)
    #         pprint("sql执行行数：-------")
    #         pprint(rows1)
    #         self.db.commit()
    #     except:
    #         self.db.rollback()
    #     self.db.close()

    def setUp(self):
        self.Base_url = 'http://yufabu-opapi.tianhangbox.com'
        self.add_product_url = self.Base_url + '/airline/product/add_or_update'
        # self.cleardata()
        clearproduct()

    def tearDown(self):

        # self.cleardata()
        pass

    def test_productName_isnull(self):
        ''' 航司产品名称为空'''
        data = {
            # 'token': tk,
            'productName': '',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(self.add_product_url, data)
        result = rs.json()
        self.assertEqual(200, rs.status_code)
        self.assertEqual('999999', result['ret'])
        self.assertEqual('产品名称不能为空', result['msg'])

    def test_addproduct_sucess(self):
        ''' 添加航司产品 '''
        data = {
            'productName': '测试海航Q舱',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(self.add_product_url, data)
        result = rs.json()
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])
