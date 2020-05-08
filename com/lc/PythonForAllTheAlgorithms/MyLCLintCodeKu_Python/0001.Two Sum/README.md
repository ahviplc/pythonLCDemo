# [1. 两数之和](https://leetcode-cn.com/problems/two-sum)

## 题目描述
<!-- 这里写题目描述 -->
<p>给定一个整数数组 <code>nums</code>&nbsp;和一个目标值 <code>target</code>，请你在该数组中找出和为目标值的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回他们的数组下标。</p>

<p>你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。</p>

<p><strong>示例:</strong></p>

<pre>给定 nums = [2, 7, 11, 15], target = 9

因为 nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9
所以返回 [<strong>0, 1</strong>]
</pre>



## 解法
<!-- 这里可写通用的实现逻辑 -->


### Python3
<!-- 这里可写当前语言的特殊实现逻辑 -->

```python

```

### Java
<!-- 这里可写当前语言的特殊实现逻辑 -->

```java

```

### ...
```

```

# 题外小知识 
> python中一个.py文件如何调用另一个.py文件中的类和函数

>  原文链接：https://blog.csdn.net/winycg/java/article/details/78512300

```python
# 在同一个文件夹下
# 调用函数：
# A.py文件：

def add(x,y):
    print('和为：%d'%(x+y))

# B.py文件：
import A
A.add(1,2)

# 或
from A import add
add(1,2)

# 调用类：
# A.py文件:

class A:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def add(self):
        print("x和y的和为：%d"%(self.x+self.y))


# B.py文件：
from A import A
a=A(2,3)
a.add()

# 或
import A
a=A.A(2,3)
a.add()


# 在不同文件夹下
# A.py文件的文件路径：E:\PythonProject\winycg

# B.py文件：
import sys
sys.path.append(r'C:\_developSoftKu\PyCharm 2019.1.3\#CodeKu\pythonLCDemo\com\lc\demo\pianoPlayerDemo')
'''python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中'''
import A
 
a=A.A(2,3)
a.add()
```