#LC 2018年8月9日12:00:03

# shelve -- 用来持久化任意的Python对象 - 东西南北风 - 博客园
# https://www.cnblogs.com/frankzs/p/5949645.html

import shelve


# 直接使用shelve.open()就可以创建了
s = shelve.open('#Code/test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
    s['msg']="存储成功"
    print("存储成功")
    print("----------------------------------------------------")
finally:
    s.close()





# 再次打开-如果想要再次访问这个shelf，只需要再次shelve.open()就可以了，然后我们可以像使用字典一样来使用这个shelf

s = shelve.open('#Code/test_shelf.db')
try:
    existing = s['key1']
    msg=s['msg']

finally:
    s.close()

print(existing)
print("打开msg的内容为:"+msg)
print("----------------------------------------------------")


# dbm这个模块有个限制，它不支持多个应用同一时间往同一个DB进行写操作。所以当我们知道我们的应用如果只进行读操作，我们可以让shelve通过只读方式打开DB：
# 当我们的程序试图去修改一个以只读方式打开的DB时，将会抛一个访问错误的异常。异常的具体类型取决于anydbm这个模块在创建DB时所选用的DB。

import shelve

s = shelve.open('#Code/test_shelf.db', flag='r')
try:
    existing = s['key1']
finally:
    s.close()

print(existing)
print("----------------------------------------------------")



# 写回（Write-back）
# 由于shelve在默认情况下是不会记录待持久化对象的任何修改的，所以我们在shelve.open()时候需要修改默认参数，否则对象的修改不会保存。


#不可以写回的版本
# 上面这个例子中，由于一开始我们使用了缺省参数shelve.open()了，因此第61行修改的值即使我们s.close()也不会被保存。

import shelve

s = shelve.open('#Code/test_shelf.db')
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
finally:
    s.close()

s = shelve.open('#Code/test_shelf.db', writeback=True)
try:
    print(s['key1'])
    print("----------------------------------------------------")
finally:
    s.close()





#所以当我们试图让shelve去自动捕获对象的变化，我们应该在打开shelf的时候将writeback设置为True。
# 当我们将writeback这个flag设置为True以后，shelf将会将所有从DB中读取的对象存放到一个内存缓存。当我们close()打开的shelf的时候，
# 缓存中所有的对象会被重新写入DB。


# writeback方式有优点也有缺点。优点是减少了我们出错的概率，并且让对象的持久化对用户更加的透明了；但这种方式并不是所有的情况下都需要，首先，使用writeback以后，shelf在open()的时候会增加额外的内存消耗，
# 并且当DB在close()的时候会将缓存中的每一个对象都写入到DB，这也会带来额外的等待时间。因为shelve没有办法知道缓存中哪些对象修改了，
# 哪些对象没有修改，因此所有的对象都会被写入。

import shelve

s = shelve.open('#Code/test_shelf.db', writeback=True)
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
    print(s['key1'])
finally:
    s.close()

s = shelve.open('#Code/test_shelf.db', writeback=True)
try:
    print(s['key1'])
    print("----------------------------------------------------")
finally:
    s.close()




# 最后再来个复杂一点的例子

