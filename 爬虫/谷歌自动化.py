import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(2)
# print(browser.current_url)#获取当前页面url
# print(browser.title)#获取页面标签p
# print()
# browser.maximize_window()#窗口最大化
# browser.fullscreen_window()#窗口全屏
# browser.close()#关闭窗口
# browser.quit()#关闭浏览器
#通过id定位
# browser.find_element_by_id('wd').send_keys('CSDN')
# #通过name方式定位
# browser.find_element_by_name('wd').send_keys('京东')
# #通过tag name方式定位
# browser.find_element_by_tag_name('input').send_keys('京东')
# #通过css方式定位
# browser.find_element_by_css_selector('#kw').send_keys('京东')
# #通过class name 方式定位
# browser.find_element_by_class_name('s_ipt').send_keys('京东')
#通过xpath方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("京东")






browser.find_element_by_id('su').click()#找到按钮su并点击一下
time.sleep(3)
browser.quit()


