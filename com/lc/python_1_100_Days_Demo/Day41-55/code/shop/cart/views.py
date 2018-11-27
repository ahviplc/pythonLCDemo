from django.core import serializers
from django.shortcuts import render, redirect

from cart.models import Goods
from cart.utils.showCartUtil import showCartUtil  # 导入公共函数


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


class CartItem(object):
    """购物车中的商品项"""

    def __init__(self, goods, amount=1):
        self.goods = goods
        self.amount = amount

    @property
    def total(self):
        return self.goods.price * self.amount


class ShoppingCart(object):
    """购物车"""

    def __init__(self):
        self.items = {}
        self.index = 0

    def add_item(self, item):
        if item.goods.id in self.items:
            self.items[item.goods.id].amount += item.amount
        else:
            self.items[item.goods.id] = item

    def remove_item(self, id):
        if id in self.items:
            self.items.remove(id)

    def clear_all_items(self):
        self.items.clear()

    @property
    def cart_items(self):
        return self.items.values()

    @property
    def total(self):
        val = 0
        for item in self.items.values():
            val += item.total
        return val

#添加某个商品到购物车
def add_to_cart(request, id):
    goods = Goods.objects.get(pk=id)
    # 通过request对象的session属性可以获取到session
    # session相当于是服务器端用来保存用户数据的一个字典
    # session利用了Cookie保存sessionid
    # 通过sessionid就可以获取与某个用户对应的会话(也就是用户数据)
    # 如果在浏览器中清除了Cookie那么也就清除了sessionid
    # 再次访问服务器时服务器会重新分配新的sessionid这也就意味着之前的用户数据无法找回
    # 默认情况下Django的session被设定为持久会话而非浏览器续存期会话
    # 通过SESSION_EXPIRE_AT_BROWSER_CLOSE和SESSION_COOKIE_AGE参数可以修改默认设定
    # Django中的session是进行了持久化处理的因此需要设定session的序列化方式
    # 1.6版开始Django默认的session序列化器是JsonSerializer
    # 可以通过SESSION_SERIALIZER来设定其他的序列化器(例如PickleSerializer)
    cart = request.session.get('cart', ShoppingCart())
    cart.add_item(CartItem(goods))
    request.session['cart'] = cart
    print('添加购物车成功-'+goods.name)
    return redirect('/')

#查看购物车
def show_cart(request):

     print(request.session.get('cart'))

     cart = (request.session.get('cart'))
     print(cart)
     print(request.session.items())
     print(request.session.exists('cart'))  # 检查会话session的key在数据库中[表名称为:django_session,注意此表为自动生成的] 是否存在 #django_session中 存在 就为True 不存在 就为False 研究明白了 已测试 是这样的
     print(request.session.get('cart', None))
     print(cart is None)  # 是否为None 为None就是True
     print(cart is not None)  # 是否不为None 不为None就是True
     if (cart!=None):
             cartItems=cart.items  # 这个是dict数组 cartItems
             print(cart.items)
             # print(cartItems[1])  # 这个是dict数组 取出数组1位置的 cartItems[1] 先屏蔽掉

             # cart_2 = serializers.deserialize(request.session.get('cart')) #原写法 不可行 会报错：TypeError: deserialize() missing 1 required positional argument: 'stream_or_string'

             # cart = CartItem()  # LC衍化版本
             # cart = serializers.deserialize(request.session.get('cart'),CartItem())

             # 遍历字典dict三种形式
             cartItemsList2 = []  # 新建一个空的list 用于接收购物项
             for i in cartItems:  # for循环遍历 ，dict.keys() 返回字典dict的键列表， dict默认遍历keys 相当于 for i in cartItems.keys()
                 print('----' + str(i))
                 cartItemsList2.append(cartItems[i])

             cartItemsList3 = []  # 新建一个空的list 用于接收购物项
             for k,v in cartItems.items():  # for循环遍历  ，dict.items()	返回字典dict的(key，value)元组对的列表
                 print(str(k)+'----'+str(v))
                 cartItemsList3.append(cartItems[k])

             cartItemsList4 = []  # 新建一个空的list 用于接收购物项
             for v in cartItems.values():  # for循环遍历，dict.values()	返回字典dict的值列表
                 print('----' + str(v))
                 cartItemsList4.append(v)

             # dict转成list
             # cartItemsList = list(cartItems)  # 这样操作 不可 会直接转成只有 1 2的list 如： [1,2]

             ctx = {
                 'cartItemsList':cartItemsList2,
                 'totalMoeny':cart.total
             }
     else:
         ctx = {
             'cartItemsList': None,
             'totalMoeny': None
         }
     return render(request,  'cart.html',  context=ctx)


#   清空购物车
def remove_all_cart(request):
    # 通过request对象的session属性可以获取到session
    # session相当于是服务器端用来保存用户数据的一个字典
    # session利用了Cookie保存sessionid
    # 通过sessionid就可以获取与某个用户对应的会话(也就是用户数据)
    # 如果在浏览器中清除了Cookie那么也就清除了sessionid
    # 再次访问服务器时服务器会重新分配新的sessionid这也就意味着之前的用户数据无法找回
    # 默认情况下Django的session被设定为持久会话而非浏览器续存期会话
    # 通过SESSION_EXPIRE_AT_BROWSER_CLOSE和SESSION_COOKIE_AGE参数可以修改默认设定
    # Django中的session是进行了持久化处理的因此需要设定session的序列化方式
    # 1.6版开始Django默认的session序列化器是JsonSerializer
    # 可以通过SESSION_SERIALIZER来设定其他的序列化器(例如PickleSerializer)
    cart = (request.session.get('cart')) # 从session中拿出cart相关的session信息
    print(cart)
    del request.session["cart"]   # 删除一组键值对 删除某一个键值对
    # request.session.pop(key)     # 删除某一个键值对
    # request.session.delete()      # 删除所有的session键值对 删除当前会话的所有Session数据
    # request.session.flush()   # 删除所有的session键值对.删除了cookie
    # request.session['msg'] = '清空购物车成功'   # 清空购物车成功提示 放入session中 在页面显示出来 废弃-现在不在页面从session中取值了
    print('清空购物车成功')

    msg = '清空购物车成功'
    ctx = showCartUtil(request, msg)  # 重新组织查看购物车代码-为了回显其数据，再次整理数据,拿到处理好，要回显到页面的字典ctx

    # return redirect('/show_cart')  # 跳转到 查看购物车
    return render(request, 'cart.html', context=ctx)  # 删除之后，带着要回显的数据，跳转到购物车页面


# 从购物车删除单个商品
def remove_one_cart(request, id):
    goods = Goods.objects.get(pk=id)  # 根据id从数据库拿出对应商品的对象信息
    cart = request.session.get('cart')  # 从session中拿出cart相关的session信息
    del cart.items[id]  # 根据id 从购物车删除此商品 备注：这里是操作字典dict
    request.session['cart'] = cart  # 把删除成功之后的session【'cart'】 再次赋值给session 重新赋值 更新session
    # request.session['msg'] = '从购物车删除单个商品成功-'+goods.name  #删除成功提示 放入session中 在页面显示出来 废弃-现在不在页面从session中取值了

    #  判断session中是否还有商品项的判断
    if len(cart.items) == 0:  # 如果为零 则彻底移除'cart'对应seesion
        del request.session["cart"]  # 删除一组键值对 删除某一个键值对

    print('从购物车删除单个商品成功-'+goods.name)

    msg = '从购物车删除单个商品成功-'+goods.name

    ctx = showCartUtil(request, msg)  # 重新组织查看购物车代码-为了回显其数据，再次整理数据,拿到处理好，要回显到页面的字典ctx

    # return redirect('/show_cart')  # 跳转到 查看购物车
    return render(request, 'cart.html', context=ctx) #  删除之后，带着要回显的数据，跳转到购物车页面