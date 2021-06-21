# -*- coding: utf-8 -*-
"""

@File    : daily_check.py
@Description :
@Author  : ljw
@Time    : 2021/6/17 20:19

"""
import csv
import numpy as np
from selenium import webdriver
import time
from datetime import datetime

from util.file_util import read_csv_data

RELOGIN_TAG = 'RELOGIN'
ZHUCE_TAG = 'ZHUCE_INFO'


class DailyCheck(object):
    @classmethod
    def check(cls, fpath, act_type, check_username='', check_password=''):
        user_info = read_csv_data(fpath)

        chrome_driver = 'util/chromedriver.exe'
        browser = webdriver.Chrome(executable_path=chrome_driver)
        if act_type is ZHUCE_TAG:
            zhuce_info = DailyCheck().re_login(ZHUCE_TAG, [0, 1], browser, username=check_username,
                                               password=check_password)
            return zhuce_info
        for info in user_info[1:]:
            chrome_driver = 'util/chromedriver.exe'
            browser = webdriver.Chrome(executable_path=chrome_driver)
            DailyCheck().re_login(None, info, browser)

    @staticmethod
    def login(username, password, browser):
        browser.get(
            'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp?_p=YXM7MiZ0PTImZD0xMDEmcD0xJmY9MzAmbT1OJg__&_l=&_t=')
        user_name = browser.find_element_by_id('username')
        user_name.send_keys(str(username))
        user_password = browser.find_element_by_id('password')
        user_password.send_keys(str(password))
        button = browser.find_element_by_class_name('login_btn')
        time.sleep(1)
        try:
            yzm_info = browser.find_element_by_xpath("//*[@id='authcode']")
            yzm_info.send_keys(str('yzm'))  # 输入验证码
        except:
            pass
        button.click()
        try:
            login_info = browser.find_element_by_xpath("//*[@id='msg1']")  # 验证码输入错误
            if login_info.text == '验证码信息无效。':
                print(f"{username}:验证码输入错误")
                return RELOGIN_TAG
            elif login_info.text == '账户不存在。':
                print(f"{username}-->账号不存在!")
                return False
            elif login_info.text == '认证信息无效。':
                print(f"{username}-->密码错误!")
                return False
        except:
            print(f"{username}登录成功")
            return True

    @staticmethod
    def check_mothod(username, ps, browser):
        try:
            tw = browser.find_element_by_id('input_tw')
            tw.send_keys('36.5')
            zwtw = browser.find_element_by_id('input_zwtw')
            zwtw.send_keys('36.6')
            button = browser.find_element_by_id('post')
            button.click()
            print(f'{username}于{datetime.now()}打卡成功！')
        except:
            print(f'今天{username}已经打过卡啦，不需要再重复打卡！')

    def re_login(self, tag, info, browser, username='', password=''):
        _user_relogin = 3
        _begin_relogin = 0
        while _begin_relogin < _user_relogin:
            if tag == ZHUCE_TAG:
                info[0] = username
                info[1] = password
            login_type = self.login(username=info[0], password=info[1], browser=browser)
            if login_type is RELOGIN_TAG:
                _begin_relogin += 1
                print(f'{info[0]}登录第{_begin_relogin}次')
                if _begin_relogin == 3:
                    print(f'{info[0]}尝试登录三次都失败')
                    browser.close()
                    return False
            elif login_type is True:
                if tag == ZHUCE_TAG:
                    browser.close()
                    return login_type
                else:
                    self.check_mothod(username=info[0], ps=info[1], browser=browser)
                    browser.close()
                    break
            else:
                browser.close()
                return login_type


if __name__ == '__main__':
    DailyCheck.check(fpath='data/login_info.csv', act_type=None)
    # chrome_driver = 'util/chromedriver.exe'
    # browser = webdriver.Chrome(executable_path=chrome_driver)
    # info = DailyCheck().re_login(ZHUCE_TAG, [0, 1], browser, username='20900', password='22222')
    # # print(info)
    # f_path = 'data/login_info.csv'
    # user_info = read_csv_data(f_path)
    # for info in user_info[1:]:
    #     chrome_driver = 'util/chromedriver.exe'
    #     browser = webdriver.Chrome(executable_path=chrome_driver)
    #     info = DailyCheck().re_login(None, info, browser)
    #     print(info)
