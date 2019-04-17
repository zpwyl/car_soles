# !/usr/bin/env python3
# _*_ utf-8 _*_
# @Time    : 2018/12/11/011 8:50
# @File    : form.py
# @Software: PyCharm
# @author = zp
from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=10)
    telephone = forms.CharField(label='电话号码', max_length=11)


class LoginForm(forms.Form):
    account = forms.CharField(label='账号', max_length=20)
    password = forms.CharField(label='密码', max_length=20)


class BuyForm(forms.Form):
    name = forms.CharField(label='客户姓名', max_length=20)
    telephone = forms.CharField(label='电话号码', max_length=20)
    address = forms.CharField(label='办理地址', max_length=20)
    month_salary = forms.CharField(label='客户月薪', max_length=20)
    id_card = forms.CharField(label='身份证号', max_length=20)
    bank_card = forms.CharField(label='银行卡号', max_length=20)
    first_pay = forms.CharField(label='首付', max_length=20)
    month_pay = forms.CharField(label='月供', max_length=20)