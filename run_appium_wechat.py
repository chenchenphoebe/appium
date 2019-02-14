# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'm18128866322@163.com'
    msg['To'] = "823974765@qq.com"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("m18128866322@163.com", "cl02125053")
    smtp.sendmail("m18128866322@163.com", "823974765@qq.com", msg.as_string())
    smtp.quit()
    print("email has send out")


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+'\\'+fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


if __name__ == "__main__":
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = "./report/"+now+"result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"环境：android 4.4")
    discover = unittest.defaultTestLoader.discover('./test_case', pattern='wechat_tools2.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./report')
    send_mail(file_path)
