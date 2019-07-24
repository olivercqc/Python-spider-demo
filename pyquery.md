### PyQuery 总结
-----
#### 初始化

- 字符串初始化
  ```python
  from pyquery import PyQuery as pq
  doc = pq(html) # 此处的html是一个字符串
  ```
- URL初始化
  ```python
  from pyquery import PyQuery as **pq**
  doc = pq(url="..........") # 指定参数url 传入一个网页
  ```
  ```python
  import requests
  from pyquery import PyQuery as pq
  doc = pq(requests.get("........").text) # 与上述代码实现相同功能
  ```
- 文件初始化
  ```python
  from pyquery import PyQuery as pq
  doc = pq(filename=".......") # 传递本地文件名，读取本地文件内容
  ```

#### 查找节点

- 子节点\
  find()方法，查找节点的所有子孙节点\
  children()方法，只查找节点的子节点\
  传入CSS选择器可以进行筛选
- 父节点\
  parent()方法，获取节点的直接父节点\
  parents()方法，获取节点的祖先节点\
  传入CSS选择器可以进行筛选
- 兄弟节点\
  siblings()方法，获取节点的兄弟节点\
  传入CSS选择器可以进行筛选

#### 遍历

- PyQuery的选择结果可能是多个节点，也可能是单个节点，都是PyQuery类型
- 对于单个节点，可以直接打印输出，也可以转换成字符串
- 对于多个节点，调用items()方法，得到一个生成器，进行遍历

#### 获取信息

- 获取属性\
  调用attr()方法获取属性值 a.attr('href')\
  调用attr属性获取属性值 a.attr.href\
  当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性
- 获取文本\
  调用text()方法获取节点内部文本\
  调用html()方法获取节点内部的HTML文本\
  选中多个节点时，html()方法返回第一个节点内部的HTML文本，text()返回所有节点内部的纯文本

#### 节点操作

- addclass()和removeclass()可以动态改变节点的class属性
- attr()方法可以修改属性 传入两个参数 第一个参数是属性名 第二个参数是属性值
- text()和html()也可以对应修改节点内部的内容