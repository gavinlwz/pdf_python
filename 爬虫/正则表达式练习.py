import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
                     {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# for image in images:
#     print(image['src'])
'''
#     re表示表达式
#     模式	            描述
#     ^	        匹配字符串的开头
#     $	        匹配字符串的末尾。   \
#     .	        匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
#     [...]	    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
#     [^...]	    不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
#     re*	        匹配0个或多个的表达式。
#     re+	        匹配1个或多个的表达式。
#     re?	        匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
#     re{n}	    精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
#     re{n,}	    匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
#     re{n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
#     a|b	        匹配a或b
#     (re)	    对正则表达式分组并记住匹配的文本
#     (?imx)	    正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
#     (?-imx)	    正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
#     (?: re)	    类似 (...), 但是不表示一个组
#     (?imx:re)	在括号中使用i, m, 或 x 可选标志
#     (?-imx:re)	在括号中不使用i, m, 或 x 可选标志
#     (?#...)	    注释.
#     (?= re)	    前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
#     (?! re)	    前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
#     (?> re)	    匹配的独立模式，省去回溯。
#     \w	        匹配字母数字及下划线
#     \W	        匹配非字母数字及下划线
#     \s	        匹配任意空白字符，等价于 [\t\n\r\f]。
#     \S	        匹配任意非空字符
#     \d	        匹配任意数字，等价于 [0-9].
#     \D	        匹配任意非数字
#     \A	        匹配字符串开始
#     \Z	        匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
#     \z	        匹配字符串结束
#     \G	        匹配最后匹配完成的位置。
#     \b	        匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
#     \B	        匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
#     \n,\t,等.	匹配一个换行符。匹配一个制表符。
#     \1...\9	    匹配第n个分组的内容。
#     \10	        匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
  '''
con = 'hello 123 4567 World_This is a Regex Demo 1485249556'
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}', con)
print(result)
print(result.group())  # group（）方法可以输出匹配到的内容
print(result.span())  # span（）输出匹配的范围 也即是结果再远政府唱的位置范围
# #【匹配目标】
# #从匹配的目标中提取一部分内容实用()将想提取的子字符串括起来
# #括号其实标记的是表达式的开始和结束位置，被标记的内容会一次对应分组，然后根据group的索引进行获取
# #group(1)会输出第一个匹配()中的内容，如果后面()还有则可以使用(2),(3)来获取
content = 'Hello 1234567 Word_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWord', content)
print(result)
print(result.group())
print(result.group(0), type(result.group(0)))
print(result.group(1))
print(result.span())
# 【贪婪与非贪婪】
# 使用.*匹配时.*会匹配尽可能多的字符，所以数字中只剩下了最后一个7，贪婪匹配
# 非贪婪匹配，.*?匹配尽可能少的字符
# 字符中间匹配尽量使用非贪婪匹配，避免匹配结果有问题
# 非贪婪匹配不能写在最后面，因为后面没东西了，所以啥都不会出来
content = 'Hello 1234567 Word_This is a Regex Demo'
result = re.match('^He.*(\d).*Demo$', content)
# result=re.match('^He.*?(\d).*Demo$',content)
print(result)
print(result.group(1))
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print('result1', result1.group(1))
print('result2', result2.group(1))
# #【通用匹配】
# #如果全都用\s或者\d一直来匹配空格和数字，那工作量是非常大。可以使用一种通用匹配的方式来处理
# #.* （点星,.匹配任意字符，*匹配前面字符无限次），连起来就可以匹配任意字符
content = 'Hello 1234567 Word_This is a Regex Demo'
result = re.match('Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())

# 【修饰符】
# .匹配的是除了换行符之外的任意字符，所以在存在换行符的字符串中就会出问题
# re.I 匹配对大小写不敏感
# re.M 多行匹配，影响^和$
# re.S 使.匹配包括换行在内的所有字符
# re.U 根据Unicode字符集解析字符。影响\w \W \b \B
# re.X 提供更灵活的格式让正则更易于理解
# re.S,re.I在网页匹配中更常用
content = '''Hello 1234567 Word_This
is a Regex Demo
'''
result = re.match('He.*?(\d+).*?Demo$', content)
result = re.match('He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))
# # 【转义匹配】
# #  想要匹配.，需要进行转义匹配
# # 反斜杠 \转义符
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)
print(result.group())
'''
com=' 1756428991 15478933855 1456973581 14789354893'
result=re.match('^1\d{10}',com)
print(result)
print(result.group())
'''
# 提取class为active的li节点中超链接包含的歌手名和歌名，也就是href singer 和
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；match更适合用来检测字符串是否符合正则规则
2. search()
    扫描整个字符串，返回第一个成功匹配的结果。如果没找到，返回None
3. findall()
4. sub()
5. compile()
'''
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；match更适合用来检测字符串是否符合正则规则
2. search()
    扫描整个字符串，返回第一个成功匹配的结果。如果没找到，返回None
3. findall()
4. sub()
5. compile()
'''

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
# 分组记住匹配的文本，匹配第一个 任贤齐
result = re.search('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# active时li属性，查找地一个active属性的li下的歌手内容
result = re.search('<li.*?active.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.s)
# 前两个li都包含了换行符，所以在res修饰时职匹配了第四个，所以尽量都加上re.s
result = re.search('li.*?singe="(.*?)">(.*?)</a>', html)
if result:
    print(result.group(1), result.group(2))

results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(results)
for results in results:
    print(results)
    print(results[0], results[1])

results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(<a/>)?\s*?</li>', html, re.S)
for result in results:
    print(result[1])
# 匹配所有带a节点替换为空只留文本然后findall查找
html = re.sub('<a.*?>|</a>', '', html)
# print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；
    match更适合用来检测字符串是否符合正则规则
2. search()
    search只能匹配找到的第一个元素
3. findall()
    findall返回匹配到的所有内容；
4. sub()
    除了可以匹配，正则表达式还可以修改文本
5. compile()
    将正则字符串编译成正则表达式对象，可以重复使用
'''
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；match更适合用来检测字符串是否符合正则规则
2. search()
    扫描整个字符串，返回第一个成功匹配的结果。如果没找到，返回None
3. findall()
4. sub()
5. compile()
'''
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；
    match更适合用来检测字符串是否符合正则规则
2. search()
    search只能匹配找到的第一个元素
3. findall()
    findall返回匹配到的所有内容；
4. sub()
    除了可以匹配，正则表达式还可以修改文本
5. compile()
'''
'''
re库提供正则表达式的实现
1. match()  
    match是从开头匹配，如果开头不匹配那么整个匹配就会失败；match更适合用来检测字符串是否符合正则规则
2. search()
    扫描整个字符串，返回第一个成功匹配的结果。如果没找到，返回None
3. findall()
4. sub()
5. compile()
'''
# 时间 输出日期不输出时间
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-19 12:59'
# pattern=erre.compile(\d{2}:\d{2})
# 也可以传入修饰符，在后面使用
pattern = re.compile('\d{2}:\d{2}', re.S)
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)

# 替换字符串中的数字为*
# re.sub(匹配规则，替换字符，源字符创)
content = '54123s5d41254f65s654scas54'
content = re.sub('\d+', '*****', content)
print(content)

phone = "2004-123-321 # 这是美国的电话号码"
num = re.sub('#.*$', "", phone)  # 删除字符串中的pythong注释
print("电话号码是：", num)
num = re.sub('\D', "", phone)  # 删除费数组（-）的字符串
print("电话号码是：", num)
