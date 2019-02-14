# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
import os
from appium import webdriver


def insert_img(driver, file_name):
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # base_dir = str(base_dir)
    # base_dir = base_dir.replace(r'\\', '/')
    # base = base_dir.split('/test_case')[0]
    # file_path = base + 'report/img' + file_name
    # driver.get_screenshot_as_file(file_path)
    file_path = r"C:\Users\yunnex\PycharmProjects\new_day\appium-wechat-tools\report\img\ll"+file_name
    driver.save_screenshot(file_path)


