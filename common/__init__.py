from sys import argv
import os

if 'Win' in os.environ['os'] and len(argv)==1 :
    api = 'http://test-api.tianhangbox.net'  # 测试环境
elif len(argv) >= 2:
    api = argv[-1]
    if 'http' not in api:
        raise ValueError('命令行最后一个参数需要完整的API地址',',例：python test_login.py http://test-api.tianhangbox.net')
    # print("-----api-----:",api)
else:
    pass