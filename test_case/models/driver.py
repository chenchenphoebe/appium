# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def return_driver():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    # desired_caps['app'] = PATH('../contects.apk')
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver



