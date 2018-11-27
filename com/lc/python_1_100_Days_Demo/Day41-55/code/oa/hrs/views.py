from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import ObjectDoesNotExist

from json import dumps

from hrs.models import Dept, Emp, BlogsPost
import time


def index(request):
    ctx = {
        'greeting': '你好，世界！'
    }
    return render(request, 'index.html', context=ctx)


def del_dept(request, no='0'):
    try:
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}
    except (ObjectDoesNotExist, ValueError):
        ctx = {'code': 404}
    return HttpResponse(
        dumps(ctx), content_type='application/json; charset=utf-8')
    # 重定向 - 给浏览器一个URL, 让浏览器重新请求指定的页面
    # return redirect(reverse('depts'))
    # return depts(request)


def emps(request, no='0'):
    # no = request.GET['no']
    # dept = Dept.objects.get(no=no)
    # ForeignKey(Dept, on_delete=models.PROTECT, related_name='emps')
    # dept.emps.all()
    # emps_list = dept.emp_set.all()
    # all() / filter() ==> QuerySet
    # QuerySet使用了惰性查询 - 如果不是非得取到数据那么不会发出SQL语句
    # 这样做是为了节省服务器内存的开销 - 延迟加载 - 节省空间势必浪费时间
    emps_list = list(Emp.objects.filter(dept__no=no).select_related('dept'))
    ctx = {'emp_list': emps_list, 'dept_name': emps_list[0].dept.name} \
        if len(emps_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


def depts(request):
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)


# Create your views here.
def blog_index(request):
    blog_list = BlogsPost.objects.all()  # 获取所有数据
    return render(request,'blogs.html', {'blog_list':blog_list})   # 返回blogs.html

# http://127.0.0.1:8000/helloLC/
def helloLC(request):

    dateTimeNow=time.time();
    print(dateTimeNow)

    print((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    dateTimeType=(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    dateTimeFormat=str((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())));

    print(type(dateTimeType)) #打印数据类型 <class 'str'>
    print(type(dateTimeFormat))

    # isinstance()
    a = '字符串'
    print(isinstance(a, str))  # 判断变量a 是否是字符串类型  True
    print(isinstance(a, int))  # 判断变量a 是否是整形 False

    ctx = {
        'greeting': '你好，世界！',
        'dateTimeNow':dateTimeNow,
        'dateTimeFormat':dateTimeType
    }
    return render(request,'helloLC.html', context=ctx)

# 跳转到a+b页面html
def to_add_a_plus_b(request):
    return render(request, 'a_plus_b.html')


# a+b 表单操作
def add_a_plus_b(request):
    a = request.GET['a']
    b = request.GET['b']
    try:
        if is_number(a) == True and is_number(b) == True:

            print(type(a))
            print(type(eval(a)))
            print(type(a) == int)
            print(type(eval(a)) == int)

            if(type(eval(a)) == int):
                a = int(a)
                print('1-int-'+str(a))
            else:
                a = float(a)
                print('2-float-' + str(a))

            if (type(eval(b)) == int):
                b = int(b)
                print('3-int-' +str(b))
            else:
                b = float(b)
                print('4-float-' + str(b))
            return HttpResponse(str(a + b))
        else:
            return HttpResponse(str('a和b都请输入数字，小数和整数均可！'))
    except ValueError and NameError:
        print("Oops!  That was no valid number.  Try again ")


# 是否为数字的方法
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass






