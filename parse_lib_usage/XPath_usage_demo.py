from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

# 调用HTML类进行初始化，构造XPath解析对象
html = etree.HTML(text)
# 调用tostring()方法得到修正后的HTML代码，结果为bytes类型
result = etree.tostring(html)
# 调用decode()方法将result转换为str类型
print(result.decode('utf-8'))

print("\n")

# 调用parse()方法直接解析文本文件
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取
result = html.xpath('//*')
print(result)
# 获取指定节点
print(result[0])

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有li节点的所有直接a子节点
result = html.xpath('//li/a')
print(result)

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有ul节点的所有子孙a节点
result = html.xpath('//ul//a')
print(result)

# /用于获取直接子节点，//用于获取所有子孙节点

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 已知子节点，可以通过..选取父节点
# 首先选中href属性为link4.html的a节点，然后获取其父节点，再获取其class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 选取class属性为item-0的li节点
result = html.xpath('//li[@class="item-0"]')
print(result)

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 使用text()方法获取节点中的文本
# 先获取所有class属性为item-0的节点，然后获取所有他的子孙节点的取文本
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 使用text()方法获取节点中的文本
# 获取所有class属性为item-0的节点，然后获取所有他的直接a节点，再获取文本
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

print("\n")

html = etree.parse('./test.html', etree.HTMLParser())
# 获取所有li节点下所有直接a节点的href属性
# @href指的是获取节点的某个属性
# [@href="link1.html"]指的是获取href属性为link1.html的节点
result = html.xpath('//li/a/@href')
print(result)

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# 属性多值匹配
# 某个节点的属性可能有多个值，如text有li和li-first
# 使用contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

print("\n")

text = '''
<li class="li li-first" name="item"><a href=""link.html>first item</a></li>
'''
html = etree.HTML(text)
# 多属性匹配
# 某个节点具有多个属性，如text有class和name
# 使用and来连接，同时匹配多个属性，根据多个属性确定一个节点
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

print("\n")

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)
# 利用中括号传入索引的方法获取特定次序的节点
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

print("\n")

html = etree.HTML(text)
# 调用ancestor轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器
# 使用*匹配所有节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 节点选择器之后是div表示选择所有的div祖先节点
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 调用attribute轴，可以获取所有属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
# 调用child轴，可以获取所有直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 调用descendant轴，可以获取所有子孙节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 调用following轴，可以获取当前节点之后的所有节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 调用following-sibling轴，可以获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)