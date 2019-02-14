# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from appiumBase import AppiumPage
import time


class Contacts(AppiumPage):
    menu_add_contact = 'com.android.contacts:id/menu_add_contact'
    left_button = 'com.android.contacts:id/left_button'
    name_xpath = "//*[@text='姓名']"
    telephone_xpath = "//android.widget.EditText[@text='电话']"
    email_xpath = "//android.widget.EditText[@text='电子邮件']"
    address_xpath = "//android.widget.EditText[@text='地址']"
    compelete = 'com.android.contacts:id/icon'
    title = 'android:id/action_bar_title'
    back = 'android:id/up'
    cliv_name_textview = 'com.android.contacts:id/cliv_name_textview'
    menu_star = 'com.android.contacts:id/menu_star'
    # cliv_name_textview = 'com.android.contacts:id/cliv_name_textview'
    accisibilty = '更多选项'
    delete_xpath = "//*[@text='删除']"
    button1 = 'android:id/button1'

    def click_element(self, model='id', loc=''):
        self.find_element(model, loc).click()
        time.sleep(2)

    def input_element(self, model='id', loc='', name=''):
        self.find_element(model, loc).send_keys(name)

    def count_elements(self, model='id', loc=''):
        counts = self.find_elements(model, loc)
        lenth = len(counts)
        return lenth

    def do_or_not_clickbutton(self, model, loc):
        status = self.find_item(self.left_button)
        if status:
            self.click_element(model, loc)
        else:
            pass

    def get_text(self):
        title = self.find_element('id', self.title)
        return title

    def add_contacts(self, name, telephone, email, address):
        self.click_element('id', self.menu_add_contact)
        self.do_or_not_clickbutton('id', self.left_button)
        self.input_element('xpath', self.name_xpath, name)
        self.input_element('xpath', self.telephone_xpath, telephone)
        self.input_element('xpath', self.email_xpath, email)
        self.input_element('xpath', self.address_xpath, address)
        self.click_element('id', self.compelete)
        # self.click_element('id', self.back)
        time.sleep(1)

    def add_favorite(self):
        self.find_elements('id', self.cliv_name_textview)[0].click()
        self.click_element('id', self.menu_star)

    def delete_contacts(self):
        ee = self.find_contact_elements('id', self.cliv_name_textview)
        size = len(ee)
        if size > 0:
            for i in range(size-1, -1, -1):
                ee[i].click()
                time.sleep(2)
                self.click_element('accessibility', self.accisibilty)
                self.click_element('xpath', self.delete_xpath)
                time.sleep(1)
                self.click_element('id', self.button1)
        else:
            pass























