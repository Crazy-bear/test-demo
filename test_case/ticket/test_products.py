# encoding=utf8

import unittest
import os
import sys
from pprint import pprint

api_autp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_autp_path)
from common.api_url import *

class ProductsCase(unittest.TestCase):

    def setUp(self):
        if 'yufabu' in argv[-1]:
            self.base_url = 'http://yufabu-opapi.tianhangbox.com'


    def search_products(self, pars):
        rs = requests.post(PRODUCTS_LIST_URL, pars)
        return rs

    def search_productid(self):
        self.pars = {
            'productName': '测试优享飞'
        }
        productlist = self.search_products(self.pars).json()
        products = productlist['data']['data']
        productid = products[0]['id']
        return productid

    def test_getproducts(self):
        pars = {}
        rs = self.search_products(pars)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])

    def test_addproducts(self):
        ''' 添加航司产品 '''
        data = {
            'productName': '测试优享飞',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(PRODUCTS_ADD_URL, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])

    def test_productName_isnull(self):
        ''' 航司产品名称为空'''
        data = {
            # 'token': tk,
            'productName': '',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(PRODUCTS_ADD_URL, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('999999', result['ret'])
        self.assertEqual('产品名称不能为空', result['msg'])

    def test_productName_isonly(self):
        ''' 航司产品名称不能重复 '''
        data = {
            'productName': '测试优享飞',
            'showTerminal': 'test产品',
            'productDesc': '我是详情',
            'remark': '我是备注'
        }
        rs = requests.post(PRODUCTS_ADD_URL, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('999999', result['ret'])
        self.assertEqual('产品名已存在', result['msg'])

    def test_uptproduct(self):
        ''' 修改航司产品 '''
        productid = self.search_productid()
        data = {
            # 'token': tk,
            'productName': '测试优享飞',
            'showTerminal': '',
            'productDesc': '我是详情',
            'remark': '测试修改',
            'id': productid
        }
        rs = requests.post(PRODUCTS_ADD_URL, data)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])

    def test_delproducts(self):
        ''' 删除航司产品 '''
        productid = self.search_productid()
        data = {
            'productId': productid
        }
        rs = requests.post(PRODUCTS_DEL_URL, data)
        pprint(rs)
        result = rs.json()
        pprint(result)
        self.assertEqual(200, rs.status_code)
        self.assertEqual('0', result['ret'])
        self.assertEqual('成功', result['msg'])


