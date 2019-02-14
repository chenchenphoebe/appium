# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from time import sleep
from models import Myunit
import random
from selenium.common.exceptions import NoSuchElementException
from models import function
from models.log import Log
from models.getconfigs import Getconfigs


class WechatTools(Myunit.MyUnit):
    logger = Log()

    def test_add_contacts(self):
        getconfig = Getconfigs()
        name1 = getconfig.getstr('Login', 'world1', exc=None)
        self.logger.debug(u"输出日志切记print，无报错无无法执行")
        # print name1
        for i in range(2):
            el = self.driver.find_element_by_id('com.android.contacts:id/menu_add_contact')
            el.click()
            function.insert_img(self.driver, 'ele.png')

            status = self.findItem('com.android.contacts:id/left_button')
            if status:
                el1 = self.driver.find_element_by_id('com.android.contacts:id/left_button')
                el1.click()
            else:
                self.logger.debug("no element finded ")

            text_name = self.driver.find_element_by_xpath("//*[@text='姓名']")
            # name = 'phobe'+str(random.randrange(0, 9))
            text_name.send_keys(name1)

            # text_phone = self.driver.find_element_by_xpath("//*[@text='电话']")
            text_phone = self.driver.find_element_by_xpath("//android.widget.EditText[@text='电话']")
            text_phone.send_keys('13' + str(random.randrange(4, 10))+''.join(str(random.choice(range(10))) for _ in range(8)))

            text_email = self.driver.find_element_by_xpath("//android.widget.EditText[@text='电子邮件']")
            text_email.send_keys(str(random.randrange(4, 10))+'9988@qq.com')

            text_address = self.driver.find_element_by_xpath("//android.widget.EditText[@text='地址']")
            text_address.send_keys('8899')

            complete = self.driver.find_element_by_id('com.android.contacts:id/icon')
            complete.click()

            back = self.driver.find_element_by_id('android:id/up')
            back.click()
            sleep(2)

    def test_add_favorite(self):
        ee = self.driver.find_elements_by_id('com.android.contacts:id/cliv_name_textview')
        ee[0].click()

        # e1 = self.driver.find_element_by_id('android:id/action_bar_title')
        # assert 'phoe' == e1.text
        # self.assertEquals('phoe', e1.txt)

        e2 = self.driver.find_element_by_id('com.android.contacts:id/menu_star')
        e2.click()

    def test_delete_contacts(self):
        ee = self.driver.find_elements_by_id('com.android.contacts:id/cliv_name_textview')
        lenth = len(ee)
        if lenth > 0:
            for i in range(lenth - 1, -1, -1):
                ee[i].click()
                sleep(3)
                try:
                    self.driver.find_element_by_accessibility_id('更多选项').click()
                    self.driver.find_element_by_xpath("//*[@text='删除']").click()
                except NoSuchElementException as err:
                    function.insert_img(self.driver, 'error.png')
                    self.logger.debug(u'查找元素异常'%err)
                # 获取页上的弹框信息
                # alert = self.driver.switch_to.alert()
                # print(alert)
                self.driver.find_element_by_id('android:id/button1').click()
                # 点击返回键
                # self.driver.press_keycode(3)
        else:
            self.logger.debug('there is no contacts')





