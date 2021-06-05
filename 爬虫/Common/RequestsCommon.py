import random
import time
from urllib import request
from lxml import etree
from selenium import webdriver
import requests
import requests_cache as rc
import json
from urllib import request
from bs4 import BeautifulSoup
from lxml import etree


class ReqCommon:
    def make_hook(self, delay=2):
        """
        钩子函数，判断是否存在缓存并延迟请求
        """

        def hook(response, *args, **kwargs):
            # 如果没有缓存，则添加延时
            if not getattr(response, 'from_cache ', False):
                print('delayTime')
                time.sleep(2)
            return response

        return hook

    def AskUrl(self, url, encoding, reqType):
        '''

        请求链接，返回utf-8转码后
        :param url:
        :param encoding:
        :return:
        '''
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"}

        proxies = {
            "http": "http://113.194.48.134:9999",
            "https": "https://60.167.21.211:1113"
        }
        http = ""  # 如果请求为空，期返回空泽粹吊，而西在洲用承方识时为断
        try:
            rc.install_cache()
            # rc.clear()  # 污空清求囫存
            # response = reqUests,get(url, headers=heoders , proxies=proxies)#代理
            res = rc.CachedSession()
            res.hocks = {'response': self.make_hook()}
            result = res.get(url, headers=headers)
            result.encoding = encoding
            if reqType == 1:
                # xpath解析
                http = etree.HTML(result.text)
                http = result
            elif reqType == 2:
                # bs解析
                http = BeautifulSoup(result.text, "lxml")
            else:
                # json解析
                http = result.json()

        except requests.exceptions.Timeout as e:
            print("链接超时")
        except requests.exceptions.ProxyError as e:
            print("代理异常")
        except requests.exceptions.RequestException as e:
            print("请求异常")
        return http
