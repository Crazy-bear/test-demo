# encoding:utf8

import os
import sys
from pprint import pprint

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, api_auto_test_path)
print(sys.path)
from common.api_url import *


class OneWayCase(unittest.TestCase):

    def search_domestic_flights(self):
        token = login('13286993500', '123456')
        pars = {'routeType': '1',
                'setTime': '2018-12-12',
                'orgCityCode': 'CAN',
                'arrCityCode': 'SHA',
                'token': token}
        r = requests.post(URL_SEARCH_DOMESTIC_FLIGHTS, pars)
        self.airline_list(r.json())

    def test_search_one_way(self):
        self.search_domestic_flights()

    def airline_list(self, r_json):

        for flightEntity in r_json['data']['flightAndSeatsList']:
            flightEntity = flightEntity['flightEntity']
            print('航司代码airlineCode:', flightEntity['airlineCode'])
            print('航司公司名airlineName:', flightEntity['airlineName'])
            print('航司名airlineShortName:', flightEntity['airlineShortName'])
            print('------')
            print('------')
            print('出发城市三字码orgCityCode:', flightEntity['orgCityCode'])
            print('出发城市名orgCityName:', flightEntity['orgCityName'])
            print('出发机场orgAirportShortName:', flightEntity['orgAirportShortName'])
            print('出发航站楼orgJetquay:', flightEntity['orgJetquay'])

            print('到达城市名dstCityName:', flightEntity['dstCityName'])
            print('到达城市三字码arrCityCode:', flightEntity['arrCityCode'])
            print('到达机场dstAirportShortName:', flightEntity['dstAirportShortName'])
            print('到达航站楼dstJetquay:', flightEntity['dstJetquay'])

            print('------')
            print('------')
            print('出发时间depTime:', flightEntity['depTime'])
            print('航班出发日期date:', flightEntity['date'])
            print('航班到达日期dstDate:', flightEntity['dstDate'])
            print('到达时间arriTime:', flightEntity['arriTime'])
            print('飞行时间timeDifference:', flightEntity['timeDifference'])
            print('------')
            print('------')

            print('距离 km  distance:', flightEntity['distance'])
            print('成人基建费audletAirportTax:', flightEntity['audletAirportTax'])
            print('成人燃油费audletFuelTax:', flightEntity['audletFuelTax'])
            print('航班号flightNo:', flightEntity['flightNo'])
            print('共享航班号shareNum:', flightEntity['shareNum'])
            print('餐饮标识meal:', flightEntity['meal'])
            print('机型planeType:', flightEntity['planeType'])
            print('机型大小planeSize:', flightEntity['planeSize'])

            for seatList in r_json['data']['flightAndSeatsList'][0]['seatList']:
                print('addNoteContent:', seatList['addNoteContent'])
                print('addNoteTitle:', seatList['addNoteTitle'])
                print('adtAgencyFare 返点 :', seatList['adtAgencyFare'])
                print('adtTaxeCn 成人基建费 :', seatList['adtTaxeCn'])
                print('adtTaxeYq 成人燃油费 :', seatList['adtTaxeYq'])
                print('cancelRuleList 退票规则 :', seatList['cancelRuleList'])
                print('changeRule 签转规则 :', seatList['changeRule'])
                print('changeServiceFee:', seatList['changeServiceFee'])
                print('chdTaxeCn 儿童基建费 :', seatList['chdTaxeCn'])
                print('chdTaxeYq 儿童燃油费 :', seatList['chdTaxeYq'])
                print('childCabin 儿童仓位代码 :', seatList['childCabin'])
                print('childCabinName:', seatList['childCabinName'])
                print('childCabinPrice 儿童仓标准价 :', seatList['childCabinPrice'])
                print('discount 折扣 :', seatList['discount'])
                print('encryptString:', seatList['encryptString'])
                print('fareBasis 运价代码 :', seatList['fareBasis'])
                print('memberPrice:', seatList['memberPrice'])
                print('parPrice 票面价 :', seatList['parPrice'])
                print('rebookRuleList 改期规则 :', seatList['rebookRuleList'])
                print('rulePromotion:', seatList['rulePromotion'])
                print('seatCode 仓位代码 :', seatList['seatCode'])
                print('seatLevel 仓位等级 :', seatList['seatLevel'])
                print('seatMsg 仓位等级名字 :', seatList['seatMsg'])
                print('seatStatus 剩余座位数 :', seatList['seatStatus'])
                print('seatType 仓位类型 :', seatList['seatType'])
                print('serviceFee:', seatList['serviceFee'])
                print('settlePrice 结算价 :', seatList['settlePrice'])
                print('subClass 子仓位代码 :', seatList['subClass'])
                print('------------')
                print('------------')
                print('------------')


if __name__ == '__main__':
    unittest.main()
