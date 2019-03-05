from django import forms
from .models import Store

class UserForm(forms.Form):
    username = forms.CharField(label="用户名:", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码:", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名:", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码:", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_pwd = forms.CharField(label="确认密码:", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class OrderForm(forms.Form):
    order_status = (
        (0, "制作"),
        (1, "测试"),
        (2, "退单"),
        (3, "完成"),
    )
    store = Store.objects.values_list('id', 'store_name')
    name = forms.IntegerField(label="商铺:", widget=forms.Select(choices=store, attrs={'class': 'form-control'}))
    num = forms.CharField(label="订单号:", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(label="订单金额:", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # c_time = forms.DateTimeField(label="创建时间:",widget=forms.TextInput(attrs={'class': 'form-control'}))
    customer_ser = forms.CharField(label="客服:",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label="作者:",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    detail = forms.CharField(label="订单详情:", widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.IntegerField(label="订单状况:",widget=forms.Select(choices=order_status, attrs={'class': 'form-control'}))
    # e_time = forms.DateTimeField(label="完成时间:",widget=forms.TextInput(attrs={'class': 'form-control'}))