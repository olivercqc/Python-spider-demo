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