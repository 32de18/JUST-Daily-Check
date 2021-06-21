# -*- coding: utf-8 -*-
"""

@File    : email_util.py
@Description :
@Author  : ljw
@Time    : 2021/6/18 19:21

"""
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# QQ邮箱提供的SMTP服务器
mail_host = 'smtp.qq.com'
# 服务器端口
port = 465
send_by = '1481280731@qq.com'
password = ''  # qq邮箱里找，详情谷歌
send_to = '1481280731@qq.com'


def send_email(title, content, log_address):
    message = MIMEMultipart()
    message["From"] = send_by
    message['To'] = send_to
    message['Subject'] = title
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    # 下面是发送附件类
    try:
        with open(log_address, 'r', encoding='utf-8') as f:
            mime = MIMEBase('text', 'txt', filename=log_address)
            mime.add_header('Content-Disposition', '321', filename=log_address)
            mime.set_payload(f.read())
            message.attach(mime)
    except:
        pass

    try:
        smpt = smtplib.SMTP_SSL(mail_host, port, 'utf-8')
        smpt.login(send_by, password)
        smpt.sendmail(send_by, send_to, message.as_string())
        smpt.quit()
        print("发送成功")
    except:
        print("发送失败")


if __name__ == "__main__":
    title = '附件文件测试'
    content = '测试内容'
    # title:标题 ， context:正文 ，第三个参数选填
    send_email(title, content, r"../data/login_info.csv")
