# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:00:22 2018

@author: zhujihang
"""

__author__ = 'zhujihang'

'send email'

import smtplib, markdown2
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import config_privacy


def _format_address(s):
    name, address = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), address))


from_address = config_privacy.email_address  # 这里大家配置自己的邮箱地址
password = config_privacy.email_password # 这里大家配置自己的密码
# to_address = 'demofamilies@gmail.com'
smtp_server = config_privacy.smtp_server

# msg = MIMEText("hello, send by xujiaji's web.", 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>XXX您好</h1>' +
#                '<p>来自网站<a href="https://www.xujiaji.org">www.xujiaji.com</a>的消息</p>' +
#                '</body></html>', 'html', 'utf-8')
# msg['From'] = _format_address("XuJiaji WEB <%s>" % from_address)
# msg['To'] = _format_address("亲爱的会员 <%s>" % to_address)
# msg['Subject'] = Header('来自xujiaji网站的消息...', 'utf-8').encode()

# server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
# server.login(from_address, password)
# server.sendmail(from_address, [to_address], msg.as_string())
# server.quit()

# _emailServer = smtplib.SMTP_SSL()
# _emailServer.connect(smtp_server, 465)
# # _emailServer.set_debuglevel(1)
# _emailServer.login(from_address, password)


def send_comment_email(email, comment, url):
    msg = MIMEText('<html><body>'
                   '<a href="http://127.0.0.1:9000"><img src="http://127.0.0.1:9000/static/img/awesome.png"></a>'
                   '<h1>亲爱的会员您好！</h1>' +
                   '<p>awesome的网站有您一条新消息：<br>消息地址：<a href="http://127.0.0.1:9000%s">http://127.0.0.1:9000%s</a></p>' % (url, url) +
                   '<p>消息内容：<br>%s</p>' % markdown2.markdown(comment) +
                   '</body></html>', 'html', 'utf-8')

    msg['From'] = _format_address("awesome WEB <%s>" % from_address)
    msg['To'] = _format_address("亲爱的会员 <%s>" % email)
    msg['Subject'] = Header('来自awesome网站的消息...', 'utf-8').encode()

    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465) #非SS协议L端口用25，SSL协议端口用465
    # server.set_debuglevel(1)
    server.login(from_address, password)
    server.sendmail(from_address, [email], msg.as_string())


def send_confirm_account(email, token):
    msg = MIMEText('<html><body>'
                   '<a href="http://127.0.0.1:9000"><img src="http://127.0.0.1:9000/static/img/awesome.png"></a>'
                   '<h1>亲爱的会员您好！</h1>' +
                   '<p>欢迎您的注册！<br>如果是您本人注册请点击认证链接（如无法访问请拷贝到浏览器）：<br>'
                   '<a href="http://127.0.0.1:9000/email_confirm?token=%s">'
                   'http://127.0.0.1:9000/email_confirm?token=%s</a></p>' % (token, token) +
                   '</body></html>', 'html', 'utf-8')

    msg['From'] = _format_address("awesome WEB <%s>" % from_address)
    msg['To'] = _format_address("亲爱的会员 <%s>" % email)
    msg['Subject'] = Header('来自awesome网站的消息...', 'utf-8').encode()

    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)#非SS协议L端口用25，SSL协议端口用465
    # server.set_debuglevel(1)
    server.login(from_address, password)
    server.sendmail(from_address, [email], msg.as_string())

# class SendEmail(object):
#
#     def __init__(self):
#         self.server = smtplib.SMTP_SSL(smtp_server, 465)
#         self.server.set_debuglevel(1)
#         self.server.login(from_address, password)
#
#     def send(self, address, msg):
#
#         print('================', from_address, address)
#         self.server.sendmail(from_address, [address], msg)
#         self.server.quit()
