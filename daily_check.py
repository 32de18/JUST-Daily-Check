# -*- coding: utf-8 -*-
"""

@File    : daily_check.py
@Description :
@Author  : ljw
@Time    : 2021/6/17 20:19

"""

from selenium import webdriver
import time
from datetime import datetime

from selenium.webdriver.chrome.options import Options

from util.file_util import read_csv_data
from util.ocr_util import download_yzm, get_yzm_img

RELOGIN_TAG = 'RELOGIN'
ZHUCE_TAG = 'ZHUCE_INFO'


class DailyCheck(object):
    @classmethod
    def check(cls, fpath, act_type, check_username='', check_password=''):
        user_info = read_csv_data(fpath)
        chrome_driver = 'util/chromedriver'
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
        if act_type is ZHUCE_TAG:
            zhuce_info = DailyCheck().re_login(ZHUCE_TAG, [0, 1], browser, username=check_username,
                                               password=check_password)
            return zhuce_info
        for info in user_info[1:]:
            chrome_driver = 'util/chromedriver'
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument("--no-sandbox")
            browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
            DailyCheck().re_login(None, info, browser)

    @staticmethod
    def login(username, password, browser):
        browser.get(
            'http://ehall.just.edu.cn/default/work/jkd/jkxxtb/jkxxcj.jsp?_p=YXM7MiZ0PTImZD0xMDEmcD0xJmY9MzAmbT1OJg__&_l=&_t=')
        user_name = browser.find_element_by_id('username')
        user_name.send_keys(str(username))
        user_password = browser.find_element_by_id('password')
        user_password.send_keys(str(password))
        time.sleep(1)

        try:
            yzm_info = browser.find_element_by_xpath("//*[@id='authcode']")
            get_yzm_img(browser)
            yzm = str(download_yzm())
            yzm_info.send_keys(yzm)
        except Exception as e:
            print(e.__class__.__name__, str(e))
            pass
        button = browser.find_element_by_class_name('login_btn')
        button.click()
        try:
            login_info = browser.find_element_by_xpath("//*[@id='msg1']")  # ?????????????????????
            if login_info.text == '????????????????????????':
                print(f"{username}:?????????????????????")
                return RELOGIN_TAG
            elif login_info.text == '??????????????????':
                print(f"{username}-->???????????????!")
                return False
            elif login_info.text == '?????????????????????':
                print(f"{username}-->????????????!")
                return False
        except:
            print(f"{username}????????????")
            return True

    @staticmethod
    def check_mothod(username, ps, browser):
        try:
            tw = browser.find_element_by_id('input_tw')
            tw.send_keys('36.5')
            zwtw = browser.find_element_by_id('input_zwtw')
            zwtw.send_keys('36.3')
            button = browser.find_element_by_id('post')
            button.click()
            print(f'{username}???{datetime.now()}???????????????')
        except:
            print(f'??????{username}????????????????????????????????????????????????')

    def re_login(self, tag, info, browser, username='', password=''):
        _user_relogin = 5
        _begin_relogin = 0
        while _begin_relogin < _user_relogin:
            if tag == ZHUCE_TAG:
                info[0] = username
                info[1] = password
            login_type = self.login(username=info[0], password=info[1], browser=browser)
            if login_type is RELOGIN_TAG:
                _begin_relogin += 1
                print(f'{info[0]}?????????{_begin_relogin}???')
                if _begin_relogin == 5:
                    print(f'{info[0]}???????????????????????????')
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
