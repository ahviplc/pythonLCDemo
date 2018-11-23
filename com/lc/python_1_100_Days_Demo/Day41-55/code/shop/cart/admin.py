from django.contrib import admin

from cart.models import Goods


class GoodsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'image')


    # ordering 设置默认排序字段,负号表示降序排序
    ordering = ('id', 'price')

    # list_editable 设置默认可编辑字段
    # list_editable = ['name', 'price', 'image']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')

    # 筛选器
    list_filter = ('id', 'name', 'price')  # 过滤器
    search_fields = ('id', 'name', 'price')  # 搜索字段
    #date_hierarchy = 'timestamp'  # 详细时间分层筛选


admin.site.register(Goods, GoodsAdmin)
