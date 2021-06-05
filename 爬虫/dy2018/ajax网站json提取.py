import requests

from Common.RequestsCommon import ReqCommon

from lxml import etree
from urllib.parse import urlparse, urlencode

if __name__ == '__main__':
    # # for i in range(0, 100, 10):
    # url = 'https://spa1.scrape.center/api/movie/?limit=10&offset={}'
    # common = ReqCommon()
    #
    # jsonData = common.AskUrl(url, "utf-8",1)
    # response = jsonData.json()  # json初始化
    # # response = jsonData.json()  # json初始化
    # if response.get("results"):  # 判断json中是否有results这个键
    #     for i in response.get("results"):
    #         name = i.get("name")  # 电影名
    #         alias = i.get("alias")  # 别名
    #
    #         print(name, alias)

    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': 0,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',

    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    # print(url)
    common = ReqCommon()
    jsonData = common.AskUrl(url, 'utf-8', 1)
    jsonData = jsonData.json()  # json初始化
    for i in jsonData.get("data"):  # 循环抓到的data列表
        if i.get("title") is not None:  # 判断不为空执行抓取
            name = i.get("title")  #
            image_list = i.get("image_list")
            image_list1 = i.get("media_name")
            print(name, image_list1)
            if image_list is not None:
                for i in image_list:
                    image_url = i.get("url")
                    print(image_url)
                    # res = requests.get(image_url)
                    # # open(filename, 'wb') 进行创建文件
                    # with open("Data/" + str(n) + ".jpg",'wb') as f:
                    #     f.write(res.content)
                    #     n = n + 1
