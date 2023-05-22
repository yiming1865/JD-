# -*- codeing = utf-8 -*-
# @time : 2023/5/19 20:54
# @time : 蒋一铭
# @file : jd.py
# @software : PyCharm

import requests
import re
import urllib.parse

def GetNum(keyword,sku):
    # keyword = input('请输入关键词：')
    sku = str(sku)
    encode_keyword = urllib.parse.quote(keyword.encode(('utf-8')))
    i = 0
    mid_list = []
    another_list = []
    # target_list = ['10053519801625', '10071041259659']
    while i < 10:
        url = 'https://search.jd.com/Search?keyword=' + encode_keyword + '&qrst=1&psort=3&wq=' + encode_keyword + '&stock=1&psort=3&pvid=ccc7952b79074bb1be4623cabc734e1a&page=' + str(
            i) + '&s=61&click=0'
        req = requests.get(url=url).text
        s = re.findall(r"wids:'(.*?)'", req)
        for string_num in s:
            mid_list = string_num.split(',')
        another_list.extend(mid_list)
        i += 1
    if sku in another_list:
        index = another_list.index(sku)
        return index + 1
    else:
        return -1





