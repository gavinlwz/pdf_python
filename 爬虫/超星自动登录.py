# import time
# from selenium import webdriver
# option=webdriver.ChromeOptions()
# option.add_argument('head')#有头模式及可以看到操作界面需要隐藏可设置‘headless’
# dr=webdriver.Chrome(options=option)#得到操作对象
# dr.get('https://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com')#打开地址
# input_zh=dr.find_element_by_class_name('ipt-tel')#找到账号输入框
# input_zh.send_keys('17634802063')#输入账号
#
# input_zh=dr.find_element_by_class_name('ipt-pwd')#找到密码输入框
# input_zh.send_keys('zxc12350')#输入密码
# btn=dr.find_element_by_id('loginBtn')#找到登录按钮
# btn.click()#执行点击操作
# time.sleep(5)
# # dr.quit()
# # time.sleep(2)
for i  in range (1,200,2):
    print(i)
