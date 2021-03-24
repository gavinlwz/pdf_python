# -*- coding: utf-8 -*-

import requests
import re
import os


class LOLSpider:

    def __init__(self):

        """
        定义一个User-Agent，伪装成浏览器
        """

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }


    def getResponse(self, url):

        """
        发送请求，获取响应

        url: 需要请求请求的url
        """

        try:
            response = requests.get(url, headers=self.headers)
            response.encoding = 'utf-8'
            assert response.status_code == 200
            return response
        except:
            return None


    def run(self):

        """
        程序入口，用来启动爬虫
        """

        # 英雄信息的url地址，其中包含了key值即英雄皮肤图片url的重要可变参数
        heroInfo_url = "http://lol.qq.com/biz/hero/champion.js"
        # 获取文本信息
        heroInfoText = self.getResponse(heroInfo_url).text

        # 使用正则匹配到英雄的英文名、key值(英雄皮肤图片url的重要可变参数)、称号、中文名
        hero_info_list = re.findall('"id":"(.*?)","key":"(.*?)","name":"(.*?)","title":"(.*?)",', heroInfoText)

        # 一个是145条数据(145个英雄)

        for hero_info in hero_info_list:
            item = {}
            item["英文名"] = hero_info[0]
            item["key"] = hero_info[1]

            # 需要通过下方方法进行解码，否则得到的中文是 \u6df1\u6e0a\u5de8\u53e3 这种样子
            item["称号"] = hero_info[2].encode().decode("unicode-escape")
            item["中文名"] = hero_info[3].encode().decode("unicode-escape")

            # 存放所有英雄皮肤的文件夹
            base_path = "./heroImgs/"
            if not os.path.exists(base_path):
                os.mkdir(base_path)

            # 单个英雄的文件夹，这里保存此英雄的所有皮肤
            path = base_path + item["中文名"]
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                print("文件夹已存在")
            self.requestSkinURl(path, item["key"])


    def requestSkinURl(self, path, key):

        """
        构造单个英雄每张皮肤图片的url，发送请求，获取图片的二进制数据

        path:    需要保存到的本地路径
        key:     皮肤图片url的重要参数
        """

        num = int(key) * 1000
        oneSkinImgurl = "https://game.gtimg.cn/images/lol/act/img/skin/big{}.jpg"
        for skinPage in range(0, 30):
            imgUrl = oneSkinImgurl.format(num + skinPage)
            img_response = self.getResponse(imgUrl)
            if img_response == None:
                continue
            self.downloadImg(path, img_response.content, skinPage)


    def downloadImg(self, path, bResponse, skinPage):

        """
        下载图片，写入本地文件

        path:    保存图片的本地路径
        bResponse:   二进制数据
        skinPage:    皮肤页数
        """

        path = path + "/" + "{}.jpg".format(skinPage)
        if os.path.exists(path):
            return
        with open(path, "wb") as f:
            f.write(bResponse)
            print("{} 写入成功".format(path))


if __name__ == '__main__':
    lolspider = LOLSpider()
    lolspider.run()