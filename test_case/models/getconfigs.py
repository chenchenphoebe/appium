# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from ConfigParser import ConfigParser
import os
import sys


class Getconfigs(object):
    """get value from common.ini"""
    app_path = r'C:\Users\yunnex\PycharmProjects\new_day\appium-wechat-tools'
    # app_path = os.path.abspath(os.path.join(os.getcwd()))

    def __init__(self):
        self.commonconfig = ConfigParser()
        self.commonconfig.read(self.app_path+r"\\data\\common.ini")

    def getstr(self, section, option, exc = None):
        config = ConfigParser()
        try:
            config.read(self.app_path+r"\\data\\common.ini")
            return config.get(section, option)
        except Exception, err:
            return err


if __name__ == "__main__":
    print sys.path
    project_path = os.path.dirname(sys.path[0])
    print project_path
    print os.getcwd()
    app_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    print app_path

