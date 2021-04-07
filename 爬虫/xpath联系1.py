import  requests
from lxml import etree
# req =requests.get("http://192.168.1.9/xpath.html")
#
# req.encoding=req.apparent_encoding
# html=etree.HTML(req.text)
# html=html.xpath('//div[@id="testid"]/ul/li/text()')#1.查找id=testid标签中ul下所有文本
# html=html.xpath('//div[@id="testid"]/ol/li/text()')#2.定位ol的子节点下所有节点
# html=html.xpath('//div/@id')#3.查找所有div的id属性值
# html=html.xpath('//div[@id="testid"]/../@price')#4.查找id=testid父辈div的prince属性值
# html=html.xpath('//div[@id="testid"]/following::*[1]/h3/ul/li[1]/text()')#5.获取id为testid的div之后的标签，不包含ID属性的div标签下所有li中第一个li的text内容
# html=html.xpath('//li[@data="one"]/../li[last()]/text()')#6.定位属性data值是one标签的父节点中ol的子节点下所有li中最后一个li标签的text内容
# html=html.xpath('//div[@id="testid"]/../div[1]/ul/li[1]/text()')#7.定位id位testid的div同级标签的上一个div标签中ul下第一个li的text属性
# html=html.xpath('//div[@id="testid"]/ol/li[2]/text()')#8.获取所有id为testid标签中ol下第二个li的文本内容
# html=html.xpath('//h2[text()="这里是个小标题"]/text()')#9.查找文本内容为"这里是个小标题"标签的文本内容

# html=html.xpath('//div[@id="testid"]/h2/text()')#10.统计有data属性的节点个数
# html=html.xpath('//div[@id="testid"]/h2/text()')#11.查找并连接属性data=one和data=three的文本内容  使用concat()函数
#
# print(html)
# [not(@qq)]

text="""

<!DOCTYPE html>
<html>
<head>
    <title>xpath test</title>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta charset="utf-8">
</head>
<body>
<div price="99.8">
    <div>
        <ul>
            <li>时间</li>
            <li>地点</li>
            <li>任务</li>
        </ul>
    </div>
    <div id='testid' data-h="first">
        <h2>这里是个小标题</h2>
        <ol>
            <li data="one">1</li>
            <li data="two">2</li>
            <li data="three">3</li>
        </ol>
        <ul>
            <li code="84">84</li>
            <li code="104">104</li>
            <li code="223">223</li>
        </ul>
    </div>
    <div>
        <h3>这里是H3的内容
            <a href="http://www.baidu.com">百度一下</a>
            <ul>
                <li>test1</li>
                <li>test2</li>
            </ul>
        </h3>
    </div>
    <div id="go">
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
            <li>6</li>
            <li>7</li>
            <li>8</li>
            <li>9</li>
            <li>10</li>
        </ul>
    </div>
</div>
</body>
</html>
  """

html=etree.HTML(text)#自动补全 解析
# html=html.xpath('//div[@id="testid"]/ul/li/text()')#1.查找id=testid标签中ul下所有文本
# html=html.xpath('//div[@id="testid"]/ol/li/text()')#2.定位ol的子节点下所有节点
# html=html.xpath('//div/@id')#3.查找所有div的id属性值
# html=html.xpath('//div[@id="testid"]/../@price')#4.查找id=testid父辈div的prince属性值
# html=html.xpath('//div[@id="testid"]/following::*[1]/h3/ul/li[1]/text()')#5.获取id为testid的div之后的标签，不包含ID属性的div标签下所有li中第一个li的text内容
# html=html.xpath('//li[@data="one"]/../li[last()]/text()')#6.定位属性data值是one标签的父节点中ol的子节点下所有li中最后一个li标签的text内容
# html=html.xpath('//div[@id="testid"]/preceding::div[1]/ul/li[1]/text()')#7.定位id位testid的div同级标签的上一个div标签中ul下第一个li的text属性
# html=html.xpath('//div[@id="testid"]/ol/li[2]/text()')#8.获取所有id为testid标签中ol下第二个li的文本内容
# html=html.xpath('//h2[text()="这里是个小标题"]/text()')#9.查找文本内容为"这里是个小标题"标签的文本内容

# result=html.xpath('count(//*[@data])')#10.统计有data属性的节点个数
# result=html.xpath('concat(//li[@data="one"]/text(),//li[@data="three"]/text())')#11.查找并连接属性data=one和data=three的文本内容  使用concat()函数
result=html.xpath('//h3[contains(text(),"H3")]/a/text()')#12.获取文本内容包含H3下a标签的文本内容 contains()

# result=html.xpath('//a[@href]/ancestor::div/preceding::div/ul/li[contains(text(),"务")]/text()')#13.查询所有包含href的a标签的祖先节点中div节点同级之前的div标签下ul中内容包含“务”的li标签中的文本内容（复杂）

# result=html.xpath('//li[@data="one" or @code="84"]/text()')#14.查询data属性=one或者code属性=84的文本内容  or和|
# result=html.xpath('//li[starts-with(@code,"8")]/text()')#15.查询属性code以8开头的li元素
#result=html.xpath('//li[@code>100]/text()')#16.获取属性code值大于100的li
# result=html.xpath('//ul[count(li)>5]/li/text()')#17.获取所有ul下li节点数大于5的ul节点中文本
print(html)

'''
ancestor::div 选取非当节点所有祖先
preceding::div  选取文档中当前节点的开始标签之前的所有节点。 兄弟节点
contains(text(),"务") 如果 text()中 包含 务，则返回 true，否则返回 false。

'''

#17.获取所有ul下li节点数大于5的ul节点中文本
print (result)