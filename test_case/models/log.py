# -*- coding:utf-8 -*-
# _author_ = 'phoebe'
import logging
import os, sys

project_path = os.path.abspath(os.path.join(os.getcwd(), "../../"))
# log_path = project_path+r'\\log\\mylog.log'
log_path = r"C:\Users\yunnex\PycharmProjects\new_day\appium-wechat-tools\log\mylog.log"


class Log:
    # def __init__(self):
    #     self.logname = "mylog"
    #     self.log_path = r"C:\Users\yunnex\PycharmProjects\new_day\appium-wechat-tools\log\mylog.log"

    def setMSG(self, level, msg):
        """
        logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(log_path, mode='a')
        # ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        fh.setFormatter(formater)
        # ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        # logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)
        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        # 移除句柄
        logger.removeHandler(fh)
        # logger.removeHandler(ch)
        fh.close()

        """

        logging.basicConfig(
            level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
            format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
            datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
            filename=log_path,  # log文件名
            filemode='w')  # 写入模式“w”或“a”
        # Define a Handler and set a format which output to console
        console = logging.FileHandler(log_path)  # 定义console handler
        # console1 = logging.StreamHandler()
        console.setLevel(logging.INFO)  # 定义该handler级别
        # console1.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
        console.setFormatter(formatter)
        # console1.setFormatter(formatter)
        # Create an instance
        logging.getLogger().addHandler(console)
        # logging.getLogger().addHandler(console1)
        if level == 'debug':
            logging.debug(msg)
        elif level == 'info':
            logging.info(msg)
        elif level == 'warning':
            logging.warning(msg)
        elif level == 'error':
            logging.error(msg)

    def debug(self, msg):
        self.setMSG('debug', msg)

    def info(self, msg):
        self.setMSG('info', msg)

    def warning(self, msg):
        self.setMSG('warning', msg)

    def error(self, msg):
        self.setMSG('error', msg)



