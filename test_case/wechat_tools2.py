# # -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from time import sleep
from models import Myunit
import random
from selenium.common.exceptions import NoSuchElementException
from models import function
from models.log import Log
from models.getconfigs import Getconfigs
from page_object import appiumContacts


class WechatTools(Myunit.MyUnit):
    logger = Log()

    def test_add_contacts(self):
        getconfig = Getconfigs()
        name1 = getconfig.getstr('Login', 'world1', exc=None)
        self.logger.debug(u"输出日志切记print，无报错无无法执行")
        try:
            addcon = appiumContacts.Contacts(self.driver)
            addcon.add_contacts(name1, '1111', '1212', '1313')
            self.assertEqual(name1, addcon.get_text(), u'创建成功')
            function.insert_img(self.driver, 'add.jpg')
        except Exception:
            self.logger.debug(u'创建失败')

    def test_add_favorite(self):
        try:
            addcon = appiumContacts.Contacts(self.driver)
            addcon.add_favorite()
            function.insert_img(self.driver, 'favorite.jpg')
        except Exception:
            self.logger.debug(u'添加关注失败')

    def test_delete_contacts(self):
        try:
            addcon = appiumContacts.Contacts(self.driver)
            addcon.delete_contacts()
            function.insert_img(self.driver, 'delete.jpg')
        except Exception:
            self.logger.debug(u'删除失败')


