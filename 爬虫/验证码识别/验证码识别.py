''''
1.使用爬虫访问验证码页面
2.分析源代码然后找到图片源代码地址
3.下载图片到本地
4.打开图片人工识别
5.模拟提交构造一个请求包含验证码进行提交
6.开始post请求
'''
import requests
import lxml.html

# url = 'http://exercise.kingname.info/exercise_captcha.html'
# Check_url = 'http://exercise.kingname.info/exercise_captcha_check'
# sess = requests.Session()
# html = sess.get(url).content
# # print(html)
# selector = lxml.html.fromstring(html)
# cattcha = selector.xpath("//img/@src")[0]
# # 下载图片
# img = requests.get("http://exercise.kingname.info/" + cattcha).content
# with open('captcha.png', 'wb') as f:
#     f.write(img)  # 下载图片

# captcha = input('请输入你看到的验证码，并输入看到的验证码：')  # 输入看到的验证码
# check = sess.post(Check_url, data={'captcha': captcha})  # 检验验证码是否正确
# print(check.content.decode())  # 查看是否成功


import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd='D:\\tesseract\\tesseract.exe'
image = Image.open("data.png")
code = pytesseract.image_to_string(image=image)
print(code)


def read(url_img):
    image = Image.open(url_img)
    code = pytesseract.image_to_string(image=image)


def clear(url_img, newImage_url):
    '''
    调整图片灰度，亮度，对比度，剪切，旋转
    '''
    image = Image.open(url_img)
    image = image.point(lambda x: 0 if x < 143 else 255)  # 调整阕值为143正常为128 上线为255 image.point提高渐变色
    image.save(newImage_url)
    return image


if __name__ == '__main__':
    clear("data.png", "text.png")
    read("text.png")  # 处理后输出图片的名字
