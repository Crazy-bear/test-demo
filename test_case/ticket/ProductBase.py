# encoding=utf8

import unittest
import os
import sys
from pprint import pprint
import pymysql
api_autp_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_autp_path)
from common.mysql_database import *
import datetime
import time
from dateutil.relativedelta import relativedelta

Base_url = 'http://yufabu-opapi.tianhangbox.com'
add_product_url = Base_url + '/airline/product/add_or_update'
PRODUCT_ID = []
AIRLINE_ID = []

def db_connect():
    db = pymysql.connect(host='47.104.205.172',
                              port=43309,
                              user='th_box_rw',
                              password='@6m1WrJxqTv3@3VpBhEa!n1qDdGe8UJf',
                              db='th_box',
                              charset='utf8')
    return db

def create_product_returnid():
    db = db_connect()
    cursor = db.cursor()
    try:
        today = datetime.date.today()
        todayArray = time.strptime(str(today), "%Y-%m-%d")
        todayStamp = int(time.mktime(todayArray))
        sqlquery = "INSERT INTO airline_product(product_name, show_terminal, product_desc, remark, last_update_time, price) \
                                  VALUES('%s','%s','%s','%s','%d','%d')" % \
                   ('测试海航Q舱', '测试智选Q舱', '1.优先登机 2.优先选择座位3.退改签手续费优惠', '我是备注', todayStamp, 0)
        rows1 = cursor.execute(sqlquery)
        id = cursor.lastrowid
        db.commit()
        return id
    except:
        db.rollback()
    db.close()

def clearproduct():
    db = db_connect()
    cursor = db.cursor()
    sqlquery = "delete from airline_product where product_name='测试海航Q舱'"
    try:
        rows1 = cursor.execute(sqlquery)
        db.commit()
    except:
        db.rollback()
    db.close()

def search_product_returndata():
    db = db_connect()
    cursor = db.cursor()
    sqlquery = "select * from airline_product where product_name='测试海航Q舱'"
    try:
        rows1 = cursor.execute(sqlquery)
        results = cursor.fetchall()
        db.commit()
        return results
    except:
        db.rollback()
    db.close()

# def isexists_product():
#     results = search_product_returndata()
#     number = results.__len__()
#     if number > 0:
#         for row in results:
#             id = row[0]
#             PRODUCT_ID.append(id)
#             pprint("已存在航司产品")
#     elif number == 0:
#         pprint("不存在航司产品")
#     return PRODUCT_ID

def search_airline_returndata():
    db = db_connect()
    cursor = db.cursor()
    # PRODUCT_ID = isexists_product()
    # sqlquery = "select * from product_route where product_id_='%d'" % PRODUCT_ID[0]
    sqlquery = "select * from product_route where product_name='测试海航Q舱'"
    try:
        rows1 = cursor.execute(sqlquery)
        results = cursor.fetchall()
        db.commit()
        return results
    except:
        db.rollback()
    db.close()

def clear_airline():
    db = db_connect()
    cursor = db.cursor()
    # PRODUCT_ID = isexists_product()
    # sqlquery = "delete from product_route where product_id_='%d'" % PRODUCT_ID[0]
    # sqlquery = "delete from product_route  where id>5"
    sqlquery = "delete from product_route  where product_name='测试海航Q舱'"
    try:
        rows1 = cursor.execute(sqlquery)
        db.commit()
    except:
        db.rollback()
    db.close()

def create_airline_returnid(productid):
    db = db_connect()
    cursor = db.cursor()
    try:
        today = datetime.date.today()
        endday = today + relativedelta(months=6)
        begintime = today.strftime("%Y-%m-%d %H:%M:%S")
        endtime = endday.strftime("%Y-%m-%d %H:%M:%S")
        todayArray = time.strptime(str(begintime), "%Y-%m-%d %H:%M:%S")
        endayArray = time.strptime(str(endtime), "%Y-%m-%d %H:%M:%S")
        startdate = int(time.mktime(todayArray))
        enddate = int(time.mktime(endayArray))
        sql = "INSERT INTO product_route ( product_name, product_id_, line_type, trip_type, org_city_code, arr_city_code, airline, cabin_code, begin_time, end_time, product_desc, create_time, remark )" \
              "VALUES('%s','%d','%s','%s','%s','%s','%s','%s','%d','%d','%s','%d','%s')" % (
                  '测试海航Q舱', productid, 'DOMESTIC', 'SINGLE', 'SZX', '', 'SZ', 'Q', startdate, enddate,
                  '1.优先登机 2.优先选择座位3.退改签手续费优惠', startdate, '我是备注')
        rows1 = cursor.execute(sql)
        id = cursor.lastrowid
        db.commit()
        return id
    except:
        db.rollback()
    db.close()




# def isexists_airline():
#     results = search_airline_returndata()
#     number = results.__len__()
#     if number > 0:
#         for row in results:
#             id = row[0]
#             productid = row[2]
#             AIRLINE_ID.append(id)
#             pprint("已存在对应的航线")
#     elif number == 0:
#         pprint("不存在对应的航线")
#     return AIRLINE_ID

def search_productid():
    results = search_product_returndata()
    number = results.__len__()
    if number > 0:
        for row in results:
            id = row[0]
            PRODUCT_ID.append(id)
    return PRODUCT_ID

def search_airlineid():
    results = search_airline_returndata()
    number = results.__len__()
    if number > 0:
        for row in results:
            id = row[0]
            AIRLINE_ID.append(id)
    return AIRLINE_ID