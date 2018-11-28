from django import forms

# post提交测试类
class AddForm(forms.Form):
    a = forms.IntegerField() #int类型
    b = forms.IntegerField()