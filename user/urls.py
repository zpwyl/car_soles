# !/usr/bin/env python3
# _*_ utf-8 _*_
# @Time    : 2018/11/23/023 17:55
# @File    : urls.py
# @Software: PyCharm
# @author = zp

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('overview/', views.overview, name='overview'),
    path('models/', views.models, name='models'),
    path('models/<str:car_type>/', views.models, name='models'),
    path('models/<str:car_type>/<str:function>/', views.models, name='models'),

    path('brand/', views.brand, name='brand'),
    path('brand/history/', views.history, name='history'),
    path('brand/ads/', views.ads, name='ads'),
    path('brand/l_finesse/', views.l_finesse, name='l_finesse'),
    path('brand/eco_thinking/', views.eco_thinking, name='eco_thinking'),
    path('brand/concept_cars/', views.concept_cars, name='concept_cars'),

    path('service/', views.service, name='service'),
    path('service/club_app/', views.club_app, name='club_app'),
    path('service/g_book/', views.g_book, name='g_book'),
    path('service/mobile_connection/', views.mobile_connection, name='mobile_connection'),

    path('news/', views.news, name='news'),
    path('node/<int:new_id>', views.node, name='node'),

    path('dealer/', views.dealer, name='dealer'),
    path('dealer_info/', views.dealer_info, name='dealer_info'),
    path('info_dealer/<str:dis_name>/', views.info_dealer, name='info_dealer'),

    path('test_drive/', views.test_drive, name='test_drive'),
    path('test_car_info/<str:car_info>/', views.test_car_info, name='test_car_info'),
    path('order_drive/<str:car_name>/', views.order_drive, name='order_drive'),

    path('financial_service/', views.financial_service, name='financial_service'),

    path('skip/<str:message/>', views.skip, name='skip'),

    path('backstage/login/', views.login, name='login'),
    path('backstage/change_password/', views.change_password, name='change_password'),
    path('backstage/confirm/', views.confirm, name='confirm'),
    path('backstage/confirm/<str:account>/', views.confirm, name='confirm'),

    path('backstage/staff/', views.staff, name='staff'),
    path('backstage/staff/<int:num>/', views.staff, name='staff'),
    path('backstage/deal/<int:order_id>/', views.deal, name='deal'),
    path('backstage/finish/<int:order_id>/', views.finish, name='finish'),

    path('backstage/dealer_admin/', views.dealer_admin, name='dealer_admin'),
    path('backstage/dealer_admin/<int:num>/', views.dealer_admin, name='dealer_admin'),
    path('backstage/add/', views.add, name='add'),
    path('backstage/update/<str:account_id>/', views.update, name='update'),
    path('backstage/delete/<str:account_id>/', views.delete, name='delete'),
    path('backstage/inventoryupdate/<int:inventory_id>/', views.inventoryupdate, name='inventoryupdate'),

]