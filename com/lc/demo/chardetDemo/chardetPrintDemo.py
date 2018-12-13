import chardet

"""
字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。

对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。

当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。
"""
print(chardet.detect(b'Hello, world!'))  # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}


data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))  # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}


data_utf8 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data_utf8))  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

data_jp = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data_jp))  # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

# 感觉以下有点bug
data_None = '灰烬之灵'.encode('gbk')
print(chardet.detect(data_None))  # {'encoding': None, 'confidence': 0.0, 'language': None}

data_None_Hello = '你好'.encode('gbk')
print(chardet.detect(data_None_Hello))   # {'encoding': 'TIS-620', 'confidence': 0.3598212120361634, 'language': 'Thai'}

#---------------------------------------------------------------------------------------------------------------------------------
print('---------------------------------------------------------------------------------------------------------------------------------')
def check_char(content):
    return chardet.detect(content)

# 默认只接受byte_str，否则返回TypeError
print("bytes", check_char(b"hello world"))  # bytes {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# print("str", check_char("hello world"))  # TypeError: Expected object of type bytes or bytearray, got: <class 'str'>


# gbk编码：英文是ascii，中文是GB2312(GBK的上一版中文字符集)，language字段指出的语言是'Chinese'
print("str1", check_char("hello world".encode("gbk")))  # str1 {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
print("str2", check_char("老子回来啦".encode("gbk")))  # str2 {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}


# utf-8编码: 英文还是ascii，中文是utf-8了，但是language没有指出，是因为utf-8适用的太多了
print("str3", check_char("hello world".encode("utf-8")))  # str3 {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
print("str4", check_char("老子回来啦".encode("utf-8")))  # str4 {'encoding': 'utf-8', 'confidence': 0.9690625, 'language': ''}