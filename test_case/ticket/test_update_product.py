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

class UptProductCase(unittest.TestCase):


    # def dbconnect(self):
    #     self.db = pymysql.connect(host='47.104.205.172',
    #                               port=43309,
    #                               user='th_box_rw',
    #                               password='@6m1WrJxqTv3@3VpBhEa!n1qDdGe8UJf',
    #                               db='th_box',
    #                               charset='utf8')
    #     cursor = self.db.cursor()
    #     return self.cursor
    #
    # def createdata(self):
    #     self.cursor = self.dbconnect()
    #     today = datetime.date.today()
    #     todayArray = time.strptime(str(today), "%Y-%m-%d")
    #     todayStamp = int(time.mktime(todayArray))
    #     sqlquery = "INSERT INTO airline_product(product_name, show_terminal, product_desc, remark, last_update_time, price) \
    #                 VALUES('%s','%s','%s','%s','%d','%d')" % \
    #                ('测试海航Q舱', '测试智选Q舱', '1.优先登机 2.优先选择座位3.退改签手续费优惠', '我是备注', todayStamp, 0)
    #     try:
    #         rows1 = self.cursor.execute(sqlquery)
    #         # pprint("sql执行行数：-------")
    #         # pprint(rows1)
    #         id = self.cursor.lastrowid
    #         self.db.commit()
    #         return id
    #     except:
    #         self.db.rollback()
    #     self.db.close()

    # def search_productid(self):
    #     self.cursor = self.dbconnect()
    #     sqlquery = "select * from airline_product where product_name='测试海航Q舱'"
    #     try:
    #         rows1 = self.cursor.execute(sqlquery)
    #         # pprint("sql执行行数：-------")
    #         # pprint(rows1)
    #         results = self.cursor.fetchall()
    #         return results
    #         self.db.commit()
    #     except:
    #         self.db.rollback()
    #     self.db.close()

    # def isexists_product(self):
    #     results = self.search_productid()  #
    #     number = results.__len__()
    #     self.productId = []
    #     if number > 0:
    #         for row in results:
    #             id = row[0]
    #             self.productId.append(id)
    #             pprint("已存在航司产品")
    #             pprint(self.productId)
    #     elif number == 0:
    #         id = self.createdata()
    #         pprint("不存在航司产品")
    #         self.productId.append(id)
    #         pprint(self.productId)
    #     return self.productId

    def setUp(self):
        self.Base_url = 'http://yufabu-opapi.tianhangbox.com'
        self.upt_product_url = self.Base_url + '/airline/product/add_or_update'
        # self.isexists_product()
        idlist = search_productid()
        number = idlist.__len__()
        if number > 0:
                id = idlist[0]
                self.productId = id
        else:
            self.productId = create_product_returnid()

    def tearDown(self):
        pass

    def test_productName_isonly(self):
        ''' 航司产品名称不能重复 '''
        data = {
            'productName': '测试海航Q舱',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(self.upt_product_url, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('999999', result['ret'])
        self.assertEqual('产品名已存在', result['msg'])

    def test_uptproduct(self):
        ''' 修改航司产品 '''
        pprint(self.productId)
        data = {
            # 'token': tk,
            'productName': '测试海航Q舱',
            'showTerminal': '测试智选Q舱',
            'productDesc': '1.优先登机 2.优先选择座位3.退改签手续费优惠',
            'remark': '测试修改',
            'id': self.productId
        }
        rs = requests.post(self.upt_product_url, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])
