### selenium 总结

#### 声明浏览器对象

- 支持Chrome、Firefox、Edge、Safari等浏览器
- 初始化浏览器对象后，可以让其执行动作，模拟浏览器操作
    ```python
    from selenium import webdriver
    broswer = webdriver.Chrome()
    ```

#### 访问界面

- 使用get()方法来请求界面，参数传入链接URL
  ```python
  url = "......"
  broswer.get(url)
  ```
- 使用page_source属性获取网页源代码
  ```python
  page_source = broswer.page_source
  ```

#### 查找结点

- 查找单个结点(返回WebElement类型结点)\
  find_element_by_id\
  find_element_by_name\
  find_element_by_xpath\
  find_element_by_link_text\
  find_element_by_partial_link_text\
  find_element_by_tag_name\
  find_element_by_class_name\
  find_element_by_css_selector
- 查找多个结点(返回列表，列表内每个结点都是WebElement类型)\
  find_elements_by_id\
  find_elements_by_name\
  find_elements_by_xpath\
  find_elements_by_link_text\
  find_elements_by_partial_link_text\
  find_elements_by_tag_name\
  find_elements_by_class_name\
  find_elements_by_css_selector

#### 结点交互

- send_keys()方法，输入文字
- clear()方法，清空文字
- click()方法，点击按钮

#### 动作链

- 没有特定执行对象的动作使用动作链进行执行
  ```python
  from selenium import webdirver
  from selenium.webdriver import ActionChains

  broswer = webdriver.Chrome()
  url = "......"
  broswer.get(url)
  broswer.switch_to_frame('iframeResult')
  source = broswer.find_element_by_css_selector('#draggable')
  target = broswer.find_element_by_css_selector('#droppable')
  actions = ActionChains(broswer)
  actions.drag_and_drop(source, target)
  actions.perform()
  ```

#### 获取节点信息

- 获取节点信息的前提是要选中节点
- 使用get_attribute()方法获取节点属性
- 使用text属性可以获取节点内部的文本信息(类似于pyquery的text()方法)
- 使用id属性可以获取节点id
- 使用location属性可以获取该节点在界面中相对位置
- 使用tag_name属性可以获取标签名称
- 使用size属性可以获取节点的大小，也就是宽高

#### 切换Frame

- 网页中有一种节点叫做iframe，也就是子Frame，相当于界面的子页面
- selenium打开界面后，默认在父级Frame里面操作，无法获取到子Frame里面的节点，使用switch_to_fram()方法来切换Frame


#### 演示等待
- 在selenium中，get()方法会在网页框架加载结束后结束执行，为了保证获取到完全加载的页面，需要延时等待一定时间。
- 隐式等待\
  implicity_wait()方法\
  当查找节点而节点没有立刻出现的时候，隐式等待讲等待一段时间在查找DOM，默认时间是0
- 显式等待\
  指定要查找的节点，然后指定一个最长等待时间。如果在规定时间加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点则抛出异常