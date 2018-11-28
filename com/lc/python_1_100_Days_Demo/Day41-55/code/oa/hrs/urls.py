from django.urls import path

from hrs import views

urlpatterns = [
    path('depts', views.depts, name='depts'),
    # url('depts/emps/(?P<no>[0-9]+)', views.emps, name='empsindept'),
    path('depts/emps/<int:no>', views.emps, name='empsindept'),
    path('deldept/<int:no>', views.del_dept, name='ddel'),
    path('blog/', views.blog_index),    # 博客
    path('helloLC/', views.helloLC),     # helloLC 测试
    path('to_add_a_plus_b/', views.to_add_a_plus_b), # to_add_a_plus_b 跳转a+b页面
    path('add_a_plus_b/', views.add_a_plus_b) , #a+b 实际操作函数 get提交
    path('toAddFormPage/', views.toAddFormPage) #a+b 页面跳转和操作函数 post提交
]

