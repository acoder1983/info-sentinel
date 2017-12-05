#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="acoder1983"    #用户名
mail_pass="giszorro1983"   #授权码 
 
 
sender = 'acoder1983@163.com'
receivers = ['acoder1983@163.com',
# 'acodersop@gmail.com',
]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# message = MIMEText('hello mail', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
 

def send_mail(subject,msg):
    message = MIMEText(msg, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    # smtpObj.set_debuglevel(True)
    smtpObj.helo(mail_host)
    smtpObj.ehlo(mail_host)
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()