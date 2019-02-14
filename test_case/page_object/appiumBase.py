# -*- coding:utf-8 -*-
# _author_ = 'phoebe'


class AppiumPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, model, value):
        try:
            if model == 'id':
                elem = self.driver.find_element_by_id(value)
            if model == 'name':
                elem = self.driver.find_element_by_name(value)
            if model == 'xpath':
                elem = self.driver.find_element_by_xpath(value)
            if model == 'accessibility':
                elem = self.driver.find_element_by_accessibility_id(value)
        except Exception:
            raise ValueError("No such element found" + str(value))
        return elem

    def find_contact_elements(self, model, value):
        try:
            if model == 'id':
                elems = self.driver.find_elements_by_id(value)
            if model == 'name':
                elems = self.driver.find_elemenst_by_name(value)
            if model == 'xpath':
                elems = self.driver.find_elements_by_xpath(value)
        except Exception:
            raise ValueError("No such element found" + str(value))
        return elems

    def find_item(self, el):
        source = self.driver.page_source
        if el in source:
            return True
        else:
            return False




