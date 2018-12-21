# -*- coding: utf-8 -*-
"""

Version: 1.0
Author: LC
DateTime: 2018年12月21日14:16:07
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html


Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。


Python爬虫利器二之Beautiful Soup的用法 | 静觅
https://cuiqingcai.com/1319.html

LC 2018-12-20 14:54:33
"""

from bs4 import BeautifulSoup
from bs4 import element


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)

# soup = BeautifulSoup(open('index.html'))

print("---------------------------------------------------------------------------------------------------------")
# 格式化输出
print(soup.prettify())

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#
# Tag
# NavigableString
# BeautifulSoup
# Comment

print("---------------------------------------------------------------------------------------------------------")
# （1）Tag
# Tag 是什么？通俗点讲就是 HTML 中的一个个标签，例如


# <title>The Dormouse's story</title>
#
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 上面的 title a 等等 HTML 标签加上里面包括的内容就是 Tag，下面我们来感受一下怎样用 Beautiful Soup 来方便地获取 Tags
#
# 下面每一段代码中注释部分即为运行结果

print(soup.title)
# <title>The Dormouse's story</title>

print(soup.head)
# <head><title>The Dormouse's story</title></head>

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print(soup.p)
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

# <title>The Dormouse's story</title>
# <head><title>The Dormouse's story</title></head>
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

# 我们可以验证一下这些对象的类型
print(type(soup.a))
# <class 'bs4.element.Tag'>

# 对于 Tag，它有两个重要的属性，是 name 和 attrs，下面我们分别来感受一下
print(soup.name)
print(soup.head.name)
# [document]
# head

# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。
print(soup.p.attrs)
# {'class': ['title'], 'name': 'dromouse'}

# 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
#
# 如果我们想要单独获取某个属性，可以这样，例如我们获取它的 class 叫什么
print(soup.p['class'])
# ['title']

# 还可以这样，利用get方法，传入属性的名称，二者是等价的
print(soup.p.get('class'))
# ['title']

# 我们可以对这些属性和内容等等进行修改，例如
soup.p['class']="newClass"
print(soup.p)
# <p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

# 还可以对这个属性进行删除，例如
del soup.p['class']
print(soup.p)
# <p name="dromouse"><b>The Dormouse's story</b></p>

print("---------------------------------------------------------------------------------------------------------")
# （2）NavigableString
# 既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用 .string 即可，例如
print(soup.p.string)
# The Dormouse's story

# 这样我们就轻松获取到了标签里面的内容，想想如果用正则表达式要多麻烦。它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串，不过我们最好还是称它英文名字吧。
#
# 来检查一下它的类型
print(type(soup.p.string))
# <class 'bs4.element.NavigableString'>

print("---------------------------------------------------------------------------------------------------------")
# 3）BeautifulSoup
# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下


print(type(soup.name))
# <type 'unicode'>
print(soup.name)
# [document]
print(soup.attrs)
# {} 空字典

print(type(soup.name))
# <type 'unicode'>
print(soup.name)
# [document]
print(soup.attrs)
#{} 空字典

print("---------------------------------------------------------------------------------------------------------")
# （4）Comment
# Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。
#
# 我们找一个带注释的标签

print(soup.a)
print(soup.a.string)
print(type(soup.a.string))

# 运行结果如下

# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie
# <class 'bs4.element.Comment'>
# 1
# 2
# 3
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
#  Elsie
# <class 'bs4.element.Comment'>

# a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。
#
# 另外我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下

# bs4.element.Comment
if type(soup.a.string) == element.Comment:
    print(soup.a.string)

# 上面的代码中，我们首先判断了它的类型，是否为 Comment 类型，然后再进行其他操作，如打印输出。


# 遍历文档树

print("---------------------------------------------------------------------------------------------------------")
# （1）直接子节点
# 要点：.contents.children
# 属性
#
# .contents
#
# tag
# 的.content
# 属性可以将tag的子节点以列表的方式输出

print(soup.head.contents)

# [<title>The Dormouse's story</title>]

# 输出方式为列表，我们可以用列表索引来获取它的某一个元素


print(soup.head.contents[0])

# <title>The Dormouse's story</title>
# .children
# 它返回的不是一个
# list，不过我们可以通过遍历获取所有子节点。
#
# 我们打印输出.children
# 看一下，可以发现它是一个
# list
# 生成器对象

print(soup.head.children)
# <listiterator object at 0x7f71457f5710>

# 我们怎样获得里面的内容呢？很简单，遍历一下就好了，代码及结果如下

for child in soup.body.children:
    print(child)

"""
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


<p class="story">...</p>
"""


print("---------------------------------------------------------------------------------------------------------")
# （2）所有子孙节点
# 知识点：.descendants
# 属性
#
# .descendants
#
# .contents
# 和.children
# 属性仅包含tag的直接子节点，.descendants
# 属性可以对所有tag的子孙节点进行递归循环，和
# children类似，我们也需要遍历获取其中的内容。


for child in soup.descendants:
    print(child)


# 运行结果如下，可以发现，所有的节点都被打印出来了，先生最外层的
# HTML标签，其次从
# head
# 标签一个个剥离，以此类推。


"""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
<head><title>The Dormouse's story</title></head>
<title>The Dormouse's story</title>
The Dormouse's story


<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>


<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<b>The Dormouse's story</b>
The Dormouse's story


<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
Once upon a time there were three little sisters; and their names were

<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
 Elsie 
,

<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
Lacie
 and

<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
Tillie
;
and they lived at the bottom of a well.


<p class="story">...</p>
...
"""


print("---------------------------------------------------------------------------------------------------------")
# （3）节点内容
# 知识点：.string
# 属性
#
# 如果tag只有一个
# NavigableString
# 类型子节点, 那么这个tag可以使用.string
# 得到子节点。如果一个tag仅有一个子节点, 那么这个tag也可以使用.string
# 方法, 输出结果与当前唯一子节点的.string
# 结果相同。
#
# 通俗点说就是：如果一个标签里面没有标签了，那么.string
# 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么.string
# 也会返回最里面的内容。例如

print(soup.head.string)
# The Dormouse's story

print(soup.title.string)
# The Dormouse's story


# 如果tag包含了多个子节点, tag就无法确定，string
# 方法应该调用哪个子节点的内容,.string
# 的输出结果是
# None


print(soup.html.string)
# None

print("---------------------------------------------------------------------------------------------------------")
# （4）多个内容
# 知识点：.strings.stripped_strings
# 属性
#
# .strings
#
# 获取多个内容，不过需要遍历获取，比如下面的例子

for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
    # u'Once upon a time there were three little sisters; and their names were\n'
    # u'Elsie'
    # u',\n'
    # u'Lacie'
    # u' and\n'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'\n\n'
    # u'...'
    # u'\n'

# 输出的字符串中可能包含了很多空格或空行, 使用.stripped_strings
# 可以去除多余空白内容

for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
    # u'Once upon a time there were three little sisters; and their names were'
    # u'Elsie'
    # u','
    # u'Lacie'
    # u'and'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'...'

print("---------------------------------------------------------------------------------------------------------")
# （5）父节点
# 知识点：.parent
# 属性

p = soup.p
print(p.parent.name)
# body

content = soup.head.title.string
print(content.parent.name)
# title

print("---------------------------------------------------------------------------------------------------------")
# （6）全部父节点
# 知识点：.parents
# 属性
#
# 通过元素的.parents
# 属性可以递归得到元素的所有父辈节点，例如

content = soup.head.title.string
for parent in content.parents:
    print(parent.name)

# title
# head
# html
# [document]

print("---------------------------------------------------------------------------------------------------------")
# （7）兄弟节点
# 知识点：.next_sibling.previous_sibling
# 属性
#
# 兄弟节点可以理解为和本节点处在统一级的节点，.next_sibling
# 属性获取了该节点的下一个兄弟节点，.previous_sibling
# 则与之相反，如果节点不存在，则返回
# None
#
# 注意：实际文档中的tag的.next_sibling
# 和.previous_sibling
# 属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行

print(soup.p.next_sibling)
#       实际该处为空白
print(soup.p.prev_sibling)
# None   没有前一个兄弟节点，返回 None
print(soup.p.next_sibling.next_sibling)

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>


# 下一个节点的下一个兄弟节点是我们可以看到的节点

print("---------------------------------------------------------------------------------------------------------")
# （8）全部兄弟节点
# 知识点：.next_siblings.previous_siblings
# 属性
#
# 通过.next_siblings
# 和.previous_siblings
# 属性可以对当前节点的兄弟节点迭代输出

for sibling in soup.a.next_siblings:
    print(repr(sibling))
    # u',\n'
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    # u' and\n'
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    # u'; and they lived at the bottom of a well.'
    # None

print("---------------------------------------------------------------------------------------------------------")
# （9）前后节点
# 知识点：.next_element.previous_element
# 属性
#
# 与.next_sibling.previous_sibling
# 不同，它并不是针对于兄弟节点，而是在所有节点，不分层次
#
# 比如
# head
# 节点为
#
# < head > < title > The
# Dormouse
# 's story</title></head>
#
# 那么它的下一个节点便是
# title，它是不分层次关系的


print(soup.head.next_element)
# <title>The Dormouse's story</title>

print("---------------------------------------------------------------------------------------------------------")
# （10）所有前后节点
# 知识点：.next_elements.previous_elements
# 属性
#
# 通过.next_elements
# 和.previous_elements
# 的迭代器就可以向前或向后访问文档的解析内容, 就好像文档正在被解析一样

for element in soup.a.next_elements:
    print(repr(element))

    # ' Elsie '
    # ',\n'
    # < a
    #
    #
    # class ="sister" href="http://example.com/lacie" id="link2" > Lacie < / a >
    #
    #
    # 'Lacie'
    # ' and\n'
    # < a
    #
    #
    # class ="sister" href="http://example.com/tillie" id="link3" > Tillie < / a >
    #
    #
    # 'Tillie'
    # ';\nand they lived at the bottom of a well.'
    # '\n'
    # < p
    #
    #
    # class ="story" >...< / p >
    #
    #
    # '...'
    # '\n'

print("---------------------------------------------------------------------------------------------------------")

# soup.find_all()用法
# find_all()
# 1. 查找标签 soup.find_all('tag')
# 2. 查找文本 soup.find_all(text='text')
# 3. 根据id查找 soup.find_all(id='tag id')
# 4. 使用正则 soup.find_all(text=re.compile('your re')), soup.find_all(id=re.compile('your re'))
# 5. 指定属性查找标签 soup.find_all('tag', {'id': 'tag id', 'class': 'tag class'})


# 以上是遍历文档树的基本用法。

# 搜索文档树

# CSS选择器

# 看网址:
# Python爬虫利器二之Beautiful Soup的用法 | 静觅
# https://cuiqingcai.com/1319.html