# encoding:utf8

import os
import sys
import unittest
import time

api_auto_test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
member_path = api_auto_test_path + '/test_case/member'
dir_test_case = api_auto_test_path + '/test_case'
dir_test_report = api_auto_test_path + '/report'
sys.path.insert(0, api_auto_test_path)
sys.path.insert(0, member_path)


def run_dir(start_dir, pattern='test*.py', top_level_dir=None):
    cases =unittest.defaultTestLoader.discover(start_dir, pattern,top_level_dir)
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(cases)

def run_cases(names):
    if isinstance(names,tuple) or isinstance(names,list):
        cases = unittest.defaultTestLoader.loadTestsFromNames(names)
        runner = unittest.TextTestRunner(verbosity=2)
        return runner.run(cases)
    else:
        raise TypeError('names must be list or tuple')