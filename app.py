from flask import Flask, jsonify
from flask_apscheduler import APScheduler

from daily_check import DailyCheck
import os

from util.config_util import ConfigUtils
from util.email_util import send_email
from util.file_util import save_csv_data
import json
from flask import request, render_template

os.environ['TZ'] = 'Asia/Shanghai'
app = Flask(__name__)
scheduler = APScheduler()


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('number')
        password = request.form.get('password')
        print(username, password)
        if username and password:
            zhuce_info = DailyCheck.check(_user_info_address, act_type='ZHUCE_INFO', check_username=username,
                                          check_password=password)
            if zhuce_info is True:
                save_csv_data(username, password, _user_info_address)
                return_info = f'{username} insert success'
            else:
                return_info = f'{username} or {password} is invalid,Please input again!'
            return render_template('index.html', data=return_info)
        else:
            return render_template('index.html', data='')
    else:
        return render_template('index.html', data='')


# @app.route('/<username>/<password>', methods=['GET', 'POST'])
# def save_info(username, password):
#     zhuce_info = DailyCheck.check(_user_info_address, act_type='ZHUCE_INFO', check_username=username,
#                                   check_password=password)
#     if zhuce_info is True:
#         save_csv_data(username, password, _user_info_address)
#         return_info = f'{username} insert seccess'
#     else:
#         return_info = f'{username} or {password} is invalid,Please input again!'
#     return jsonify(return_info)


if __name__ == '__main__':
    _cfg = ConfigUtils.get_config()
    if _cfg is None:
        ConfigUtils.build_new_config()
        print(f'Please write config to {ConfigUtils.DEFT_CONFIG_PATH}')
        exit()
    _http_port = _cfg.get(ConfigUtils.KEY_HTTP_PORT, ConfigUtils.DEFT_HTTP_PORT)
    _user_info_address = _cfg.get(ConfigUtils.KEY_USER_INFO_ADDRESS, ConfigUtils.DEFT_USER_INFO_ADDRESS)
    _log_address = _cfg.get(ConfigUtils.KEY_LOG_ADDRESS, ConfigUtils.DEFT_LOG_ADDRESS)
    _title = _cfg.get(ConfigUtils.KEY_TITLE, ConfigUtils.DEFT_TITLE)
    _content = _cfg.get(ConfigUtils.KEY_CONTENT, ConfigUtils.DEFT_CONTENT)
    _check_hour = _cfg.get(ConfigUtils.KEY_CHECK_HOUR, ConfigUtils.DEFT_CHECK_HOUR)
    _check_minute = _cfg.get(ConfigUtils.KEY_CHECK_MINUTE, ConfigUtils.DEFT_CHECK_MINUTE)
    _email_hour = _cfg.get(ConfigUtils.KEY_EMAIL_HOUR, ConfigUtils.DEFT_EMAIL_HOUR)
    _email_minute = _cfg.get(ConfigUtils.KEY_EMAIL_MINUTE, ConfigUtils.DEFT_EMAIL_MINUTE)
    scheduler.add_job(func=DailyCheck.check, id='1', trigger='cron', hour=int(_check_hour), minute=int(_check_minute),
                      kwargs={'fpath': _user_info_address, 'act_type': None})
    scheduler.add_job(func=send_email, id='2', trigger='cron', hour=int(_email_hour), minute=int(_email_minute),
                      kwargs={"title": _title, "content": _content,
                              "log_address": _log_address})
    scheduler.init_app(app=app)
    scheduler.start()
    app.run(host='127.0.0.1', port=_http_port)
