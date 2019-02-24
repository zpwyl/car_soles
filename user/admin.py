from django.contrib import admin
from .models import MainNav, MainOneNav, MainTwoNav, CarSystem,\
     CarType, CarInfo, Province, City, SlideshowWrapper, User,\
     Distributor, UserType, CarTypeBaseName, CarTypeBaseInfo,\
     CarDetailInfo, CarInfoDetail, CarDetailInfoName, \
     CarInfoDetailName, OrderDrive, InventoryManagement

# Register your models here.

admin.site.register(MainNav)
admin.site.register(MainOneNav)
admin.site.register(MainTwoNav)
admin.site.register(CarSystem)
admin.site.register(CarType)
admin.site.register(CarDetailInfo)
admin.site.register(CarDetailInfoName)
admin.site.register(CarInfo)
admin.site.register(CarInfoDetail)
admin.site.register(CarInfoDetailName)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Distributor)
admin.site.register(SlideshowWrapper)
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(CarTypeBaseName)
admin.site.register(CarTypeBaseInfo)
admin.site.register(OrderDrive)
admin.site.register(InventoryManagement)
