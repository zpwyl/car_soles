# !/usr/bin/env python3
# _*_ utf-8 _*_
# @Time    : 2018/12/25/025 12:53
# @File    : function.py
# @Software: PyCharm
# @author = zp

import hashlib
import re
from .models import MainNav, MainOneNav, MainTwoNav, SlideshowWrapper, CarType, CarInfo,\
    CarSystem, Distributor, Province, City, CarTypeBaseName, CarTypeBaseInfo, BuyCar,\
    CarInfoDetailName, CarDetailInfoName, CarInfoDetail, CarDetailInfo, OrderDrive,\
    InventoryManagement, User


ErrorNum = 0
important_name = ''


def calc_md5(password):
    md5 = hashlib.md5()
    key = 'zp'
    pwds = key + password
    md5.update(pwds.encode('utf-8'))
    pwd = md5.hexdigest()
    return pwd


# 验证邮箱
def is_valid_email(email):
    try:
        m = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', email).group()
    except:
        m = None
    else:
        return m


# 获取公用信息
def get_index_info():
    main_navs = MainNav.objects.all()
    # 汽车总览
    car_type = main_navs[0]
    car_type_detail = CarSystem.objects.all()
    # 品牌天地
    car_brand = main_navs[1]
    car_brand_detail_first = MainOneNav.objects.filter(belong_to_id=car_brand.main_nav_id)[0]
    car_brand_detail = MainOneNav.objects.filter(belong_to_id=car_brand.main_nav_id)[1:]
    # 客户服务
    customer_service = main_navs[2]
    customer_service_detail_first = MainOneNav.objects.filter(belong_to_id=customer_service.main_nav_id)[0]
    customer_service_detail = MainOneNav.objects.filter(belong_to_id=customer_service.main_nav_id)[1:]
    # 新闻资讯
    news_information = main_navs[3]
    news_information_detail = MainOneNav.objects.filter(belong_to_id=news_information.main_nav_id)
    # 我的收藏
    my_collection = main_navs[4]
    my_collection_detail = MainOneNav.objects.filter(belong_to_id=my_collection.main_nav_id)
    # 查询经销商
    inquire_dealer = main_navs[5]
    # 预约试驾
    test_drive = main_navs[6]
    content = {
        'car_types': car_type,
        'car_type_details': car_type_detail,
        'car_brands': car_brand,
        'car_brand_details_first': car_brand_detail_first,
        'car_brand_details': car_brand_detail,
        'customer_services': customer_service,
        'customer_service_detail_first': customer_service_detail_first,
        'customer_service_details': customer_service_detail,
        'news_informations': news_information,
        'news_information_details': news_information_detail,
        'my_collections': my_collection,
        'my_collection_details': my_collection_detail,
        'inquire_dealers': inquire_dealer,
        'test_drives': test_drive,
    }
    return content


# 将省市经销商转化成相应的格式
def get_dealer_info():
    province = []
    city = []
    company = []
    derlars = {}
    provinces = Province.objects.all()
    citys = City.objects.all()
    derlar = Distributor.objects.all()
    for i in provinces:
        province.append(i.province_name)
    for i in range(len(provinces)):
        city.append([])
        company.append([])
    for i in citys:
        city[i.belong_to_id - 1].append(i.city_name)
        company[i.belong_to_id - 1].append(i.city_name)
    for i in citys:
        derlars.setdefault(i.city_name, [])
    for i in derlar:
        derlars[i.belong_to.city_name].append(i.distributor_name)
    for n, i in enumerate(company):
        for m, j in enumerate(i):
            if j in company[n]:
                company[n][m] = derlars[j]
    return province, city, company


# 根据title的长度改变显示样式（品牌界面）
def get_brand_info(n):
    main_one_nav_id = MainOneNav.objects.filter(main_one_nav=n)[0].main_one_nav
    main_one_nav_name = MainOneNav.objects.filter(main_one_nav=n)[0].main_one_nav_name
    historys = MainTwoNav.objects.filter(belong_to_id=main_one_nav_id)
    image_text = []
    top = []
    for i in historys:
        if len(i.content) < 50:
            top.append(i)
        else:
            image_text.append(i)
    if len(image_text) == 0:
        Null = False
    else:
        Null = True
    add = {
        'Null': Null,
        'main_one_nav_name': main_one_nav_name,
        'image_texts': image_text,
        'tops': top,
    }
    return add


# 根据title的长度改变显示样式（车辆信息界面）
def get_car_base_info(car_type, n):
    top = []
    image_text = []
    new_car_type = CarType.objects.filter(car_type_name=car_type)[0].car_type_id
    function_name = CarTypeBaseName.objects.filter(belong_to=new_car_type)
    # 改变的name值
    car_type_base_id = function_name[n].car_type_base_id
    car_type_base_info = CarTypeBaseInfo.objects.filter(belong_to=car_type_base_id)
    for i in car_type_base_info:
        if i.content == None:
            image_text.append(i)
        else:
            if len(i.content) > 30:
                image_text.append(i)
            else:
                top.append(i)
    add = {
        'tops': top,
        'function_name': function_name,
        'car_type': car_type.upper(),
        'image_texts': image_text,
    }
    return add


# 获取车辆不同的信息
def get_devide_info(car_info, car_info_name):
    info = []
    name = []
    for i in car_info:
        for j in CarInfoDetailName.objects.filter(belong_to_id=i.car_id):
            if j.name == car_info_name:
                global important_name
                important_name = j.name
                for k in CarInfoDetail.objects.filter(belong_to_id=j.id):
                    z = {}
                    z['name'] = k.car_info_detail_name
                    if z['name'] in name:
                        for l in info:
                            if l['name'] == z['name']:
                                l['data'].append(k.car_info_detail)
                    else:
                        name.append(k.car_info_detail_name)
                        z['data'] = [k.car_info_detail]
                        info.append(z)
    return info, important_name


def get_spec(car_type):
    new_car_type = CarType.objects.filter(car_type_name=car_type)[0].car_type_id
    function_name = CarTypeBaseName.objects.filter(belong_to=new_car_type)
    # 获取公共信息
    car_type_id = CarType.objects.filter(car_type_name=car_type)[0].car_type_id
    car_info = CarInfo.objects.filter(car_type_id=car_type_id)
    car_detail_info = CarDetailInfoName.objects.filter(belong_to=car_type_id)
    # 车身尺寸和容量
    car_detail_one = car_detail_info[0]
    car_detail_one_des = CarDetailInfo.objects.filter(belong_to=car_detail_one.id)
    # 发动机
    car_detail_two = car_detail_info[1]
    car_detail_two_des = CarDetailInfo.objects.filter(belong_to=car_detail_two.id)
    # 电动机
    car_detail_three = car_detail_info[2]
    car_detail_three_des = CarDetailInfo.objects.filter(belong_to=car_detail_three.id)
    # 综合性能
    try:
        car_detail_four = car_detail_info[3]
        car_detail_four_des = CarDetailInfo.objects.filter(belong_to=car_detail_four.id)
    except:
        car_detail_four = False
        car_detail_four_des = False
    # 地盘和悬架
    try:
        car_detail_five = car_detail_info[4]
        car_detail_five_des = CarDetailInfo.objects.filter(belong_to=car_detail_five.id)
    except:
        car_detail_five = False
        car_detail_five_des = False
    # 获取单独信息
    appearance, appearance_name = get_devide_info(car_info, '外观')
    inner_chamber, inner_chamber_name = get_devide_info(car_info, '内室')
    equipment, equipment_name = get_devide_info(car_info, '便利设备')
    safety_system, safety_system_name = get_devide_info(car_info, '安全系统')
    add = {
        'car_infos': car_info,
        'car_detail_one': car_detail_one,
        'car_detail_two': car_detail_two,
        'car_detail_three': car_detail_three,
        'car_detail_four': car_detail_four,
        'car_detail_five': car_detail_five,
        'car_detail_one_des': car_detail_one_des,
        'car_detail_two_des': car_detail_two_des,
        'car_detail_three_des': car_detail_three_des,
        'car_detail_four_des': car_detail_four_des,
        'car_detail_five_des': car_detail_five_des,
        'appearance': appearance,
        'appearance_name': appearance_name,
        'inner_chamber': inner_chamber,
        'inner_chamber_name': inner_chamber_name,
        'equipment': equipment,
        'equipment_name': equipment_name,
        'safety_system': safety_system,
        'safety_system_name': safety_system_name,
        'car_type': car_type,
        'function_name': function_name
    }
    return add


info = get_index_info()
provinces, citys, companys = get_dealer_info()