# -*- coding: utf-8 -*-
import uuid
import  math
from abstest import my_abs
from abstest import power
from abstest import power2
from abstest import enroll
from abstest import fact

print(1 + 1)

strs = 'HELLO.H'

if strs.endswith('H'):
    print(strs + '你好 LC')
    print(1 + 1 + 3)
else:
    print('不好啊')

print(uuid.uuid1())

# hex()
# n1 = 255
# n2 = 1000

print(hex(255))


# 0xff

print(my_abs(-128))
print(power2(16))
print(power(15,2))
print(power(4,3))

# 输出2的平方根
print(math.sqrt(2))
print(math.sin(math.pi/2))

enroll('LC','LC1')

print(fact(5))

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0],L[1],L[2])

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print(L[0:3])
# 如果第一个索引是0，还可以省略：
print(L[:3])
# 也可以从索引1开始，取出2个元素出来：
print(L[1:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])

# 切片操作十分有用。我们先创建一个0-99的数列：
LL = list(range(100))
print(LL)

# 可以通过切片轻松取出某一段数列。比如前10个数：
print(LL[:10])

# 后10个数：
print(LL[-10:])

# 前11-20个数：
print(LL[10:20])

# 前10个数，每两个取一个：

print(LL[:10:2])

# [0, 2, 4, 6, 8]
# 所有数，每5个取一个：

print(LL[::5])

# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# 甚至什么都不写，只写[:]就可以原样复制一个list：

print(LL[:])
# [0, 1, 2, 3, ..., 99]
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：

print((0, 1, 2, 3, 4, 5)[0:3])
# (0, 1, 2)