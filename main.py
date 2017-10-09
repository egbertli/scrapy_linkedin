#! /usr/bin/python
# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup


login_url = 'https://www.linkedin.com/uas/login-submit'

headers = {
    'Host': 'www.linkedin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.linkedin.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

login_info = {
    'session_key': '18931890131@189.cn',
    'session_password': 'wkwm1006',
    'isJsEnabled': 'false',
    'loginCsrfParam': 'fc5aa36d-d357-4410-8d2f-6502f671f0a3'
}

s = requests.session()
r = s.post(login_url, data=login_info, headers=headers, verify=False)
if r.status_code == requests.codes.ok:
    print '登录成功'

    my_main_page_url = 'https://www.linkedin.com/in/%E9%87%91%E6%98%8E-%E9%82%B5-a37250142//'
    wb_data = s.get(my_main_page_url)
    print wb_data.text
    #bs = BeautifulSoup(wb_data.text,'lxml')


else:
    print '登录失败'