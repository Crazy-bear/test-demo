# encoding:utf8

from runtest_common import *

from HTMLTestRunner import HTMLTestRunner

# 指定测试用例为当前文件夹下的 test_case 目录
discover = unittest.defaultTestLoader.discover(dir_test_case)
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = os.path.basename(os.path.abspath(__file__)).split('.')[0]
file_abs_path = dir_test_report + '/' + filename + ' '+ now + 'result.html'
fp = open(file_abs_path, 'wb')
runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
runner.run(discover)
