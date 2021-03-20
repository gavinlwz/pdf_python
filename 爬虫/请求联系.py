# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 8:17
# @Author  : wamgmoufei
# @Email   : wangmoufei@live.com
# @File    : 请求联系.py
import requests


header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
url="http://www.baidu.com/"
req=requests.get(url,headers=header)
print(req.text)
