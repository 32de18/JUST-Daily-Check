# -*- coding: utf-8 -*-
"""

@File    : config_util.py
@Description :
@Author  : ljw
@Time    : 2021/6/18 19:55

"""
import configparser


class ConfigUtils(object):
    DEFT_CONFIG_PATH = 'data/config.ini'

    KEY_SECS_HTTP = 'Http'
    KEY_HTTP_PORT = 'http_port'
    DEFT_HTTP_PORT = '33060'

    KEY_SECS_FILE = 'File'
    KEY_USER_INFO_ADDRESS = 'user_info_address'
    DEFT_USER_INFO_ADDRESS = 'data/login_info.csv'
    KEY_LOG_ADDRESS = 'log_address'
    DEFT_LOG_ADDRESS = 'nohup.out'

    KEY_SECS_TIME = 'Time'
    KEY_CHECK_HOUR = 'check_hour'
    DEFT_CHECK_HOUR = '6'
    KEY_CHECK_MINUTE = 'check_minute'
    DEFT_CHECK_MINUTE = '0'
    KEY_EMAIL_HOUR = 'email_hour'
    DEFT_EMAIL_HOUR = '6'
    KEY_EMAIL_MINUTE = 'email_minute'
    DEFT_EMAIL_MINUTE = '2'

    KEY_SECS_CONTENT = 'Content'
    KEY_TITLE = 'title'
    DEFT_TITLE = '每日打卡情况'
    KEY_CONTENT = 'content'
    DEFT_CONTENT = '每日打卡情况统计'

    CONFIG = None

    @classmethod
    def build_new_config(cls, cfg_f_path=DEFT_CONFIG_PATH,
                         http_port=DEFT_HTTP_PORT):
        config = configparser.ConfigParser()
        config.add_section(cls.KEY_SECS_HTTP)
        config.set(cls.KEY_SECS_HTTP, cls.KEY_HTTP_PORT, http_port)

        config.add_section(cls.KEY_SECS_FILE)
        config.set(cls.KEY_SECS_FILE, cls.KEY_USER_INFO_ADDRESS, cls.DEFT_USER_INFO_ADDRESS)
        config.set(cls.KEY_SECS_FILE, cls.KEY_LOG_ADDRESS, cls.DEFT_LOG_ADDRESS)

        config.add_section(cls.KEY_SECS_TIME)
        config.set(cls.KEY_SECS_TIME, cls.KEY_CHECK_HOUR, cls.DEFT_CHECK_HOUR)
        config.set(cls.KEY_SECS_TIME, cls.KEY_CHECK_MINUTE, cls.DEFT_CHECK_MINUTE)
        config.set(cls.KEY_SECS_TIME, cls.KEY_EMAIL_HOUR, cls.DEFT_EMAIL_HOUR)

        config.add_section(cls.KEY_SECS_CONTENT)
        config.set(cls.KEY_SECS_CONTENT, cls.KEY_TITLE, cls.DEFT_TITLE)
        config.set(cls.KEY_SECS_CONTENT, cls.KEY_CONTENT, cls.DEFT_CONTENT)

        with open(cfg_f_path, 'w', encoding='utf-8') as fd:
            config.write(fd)

    @classmethod
    def get_config(cls, cfg_path=DEFT_CONFIG_PATH):
        config = configparser.ConfigParser()
        config.read(cfg_path)
        if cls.KEY_SECS_TIME not in config.sections() or cls.KEY_SECS_CONTENT not in config.sections() or cls.KEY_SECS_FILE not in config.sections() or cls.KEY_SECS_HTTP not in config.sections():
            return None

        cls.CONFIG = {
            cls.KEY_HTTP_PORT: config.get(cls.KEY_SECS_HTTP, cls.KEY_HTTP_PORT),
            cls.KEY_USER_INFO_ADDRESS: config.get(cls.KEY_SECS_FILE, cls.KEY_USER_INFO_ADDRESS),
            cls.KEY_LOG_ADDRESS: config.get(cls.KEY_SECS_FILE, cls.KEY_LOG_ADDRESS),
            cls.KEY_TITLE: config.get(cls.KEY_SECS_CONTENT, cls.KEY_TITLE),
            cls.KEY_CHECK_HOUR: config.get(cls.KEY_SECS_TIME, cls.KEY_CHECK_HOUR),
            cls.KEY_CHECK_MINUTE: config.get(cls.KEY_SECS_TIME, cls.KEY_CHECK_MINUTE),
            cls.KEY_EMAIL_HOUR: config.get(cls.KEY_SECS_TIME, cls.KEY_EMAIL_HOUR),
            cls.KEY_EMAIL_MINUTE: config.get(cls.KEY_SECS_TIME, cls.KEY_EMAIL_MINUTE)
        }
        return cls.CONFIG
