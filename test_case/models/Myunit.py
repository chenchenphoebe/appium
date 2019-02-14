# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
import unittest
from driver import return_driver


class MyUnit(unittest.TestCase):
    def setUp(self):
        self.driver = return_driver()

    def tearDown(self):
        self.driver.quit()

