# encoding:utf8

import os
import sys
import unittest

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
member_path = api_auto_test_path + '/test_case/'
sys.path.insert(0, api_auto_test_path)
sys.path.insert(0, member_path)

# from test_case.member.test_sign_up import SignCase
from test_case.member.test_login import LoginCase

cases = unittest.defaultTestLoader.loadTestsFromTestCase(LoginCase)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(cases)
