from django.contrib import admin

from hrs.models import Dept, Emp, BlogsPost

import django


class DeptAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('no', 'name', 'location', 'excellent')

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('no', )

    # 搜索字段
    search_fields = ('name', 'no')

    # list_editable 设置默认可编辑字段
    # list_editable = ['name', 'excellent', 'location']
    list_editable = ['excellent', 'location']

 # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('no', 'name')

class EmpAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('no', 'name', 'job', 'sal', 'dept')

    # 搜索字段
    search_fields = ('name', 'job')

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('no','dept')

    # list_editable 设置默认可编辑字段
    #list_editable = ['name', 'job', 'sal', 'dept']
    list_editable = ['job', 'sal', 'dept']

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('no', 'name')

    # fk_fields 设置显示外键字段
    fk_fields = ('dept', )


# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display =('id', 'title', 'body', 'timestamp')

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id', )

    # list_editable 设置默认可编辑字段
    #list_editable = ['title', 'body', 'timestamp']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')

    # 筛选器
    list_filter = ('id', 'title', 'timestamp')  # 过滤器
    search_fields = ('id', 'title', 'timestamp')  # 搜索字段
    date_hierarchy = 'timestamp'  # 详细时间分层筛选　


admin.site.register(Dept, DeptAdmin)
admin.site.register(Emp, EmpAdmin)
admin.site.register(BlogsPost, BlogsPostAdmin)



# 对页面title进行自定义
django.contrib.admin.AdminSite.site_header='LC Python Django 模拟演练系统'    # 此处设置页面显示标题
#django.contrib.admin.AdminSite.index_title='站点管理——LC'    #登录成功之后的首页标题
django.contrib.admin.AdminSite.site_title='LC爱python'    # 此处设置页面头部标题
#django.contrib.admin.AdminSite.site_url='http://www.oneplusone.top' #查看站点 跳转网站地址
django.contrib.admin.AdminSite.name='1'
