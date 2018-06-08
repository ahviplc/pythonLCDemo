# Filename : ASCIIAndStrDemo.py
# author by : www.oneplusone.top

# 用户输入字符
c = input("请输入一个字符: ")

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))

# 10进制转16进制: hex(16)  ==>  0x10

print( c + " 的ASCII 码为", ord(c),";十六进制的为："+hex(ord(c)))
print( a , " 对应的字符为", chr(a))

# 控制台示例

# 请输入一个字符: h
# 请输入一个ASCII码: 64
# h 的ASCII 码为 104
# 64  对应的字符为 @