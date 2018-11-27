"""
查看购物车 构造数据代码
"""

def showCartUtil(request, msg):
    cart = (request.session.get('cart'))
    if (cart != None):
        cartItems = cart.items  # 这个是dict数组 cartItems
        print(cart.items)

        cartItemsList2 = []  # 新建一个空的list 用于接收购物项
        for i in cartItems:  # for循环遍历 ，dict.keys() 返回字典dict的键列表， dict默认遍历keys 相当于 for i in cartItems.keys()
            cartItemsList2.append(cartItems[i])
        ctx = {
            'cartItemsList': cartItemsList2,
            'totalMoeny': cart.total,
            'msg':msg
        }
    else:
        ctx = {
            'cartItemsList': None,
            'totalMoeny': None,
            'msg': msg
        }
    return ctx
