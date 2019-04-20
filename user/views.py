from django.shortcuts import render, redirect, HttpResponse, render_to_response, resolve_url
from django.views.decorators.csrf import csrf_exempt
from .form import OrderForm, LoginForm, BuyForm
from django.http import JsonResponse
from .function import *
# Create your views here.


# 主页
def index(request):
    # 轮播图
    slideshow_wrapper = SlideshowWrapper.objects.all()
    add = {
        'slideshow_wrappers': slideshow_wrapper,
    }
    content = dict(info, **add)
    return render(request, 'user/index.html', content)


# 车型总览
def overview(request):
    # T系列
    car_system_T = CarSystem.objects.all()[0]
    car_type_name_T = CarType.objects.filter(car_system_id=car_system_T.car_system_id)
    # S系列
    car_system_S = CarSystem.objects.all()[1]
    car_type_name_S = CarType.objects.filter(car_system_id=car_system_S.car_system_id)
    # X系列
    car_system_X = CarSystem.objects.all()[2]
    car_type_name_X = CarType.objects.filter(car_system_id=car_system_X.car_system_id)
    # C系列
    car_system_C = CarSystem.objects.all()[3]
    car_type_name_C = CarType.objects.filter(car_system_id=car_system_C.car_system_id)
    add = {
        'car_system_T': car_system_T,
        'car_type_name_T': car_type_name_T,
        'car_system_S': car_system_S,
        'car_type_name_S': car_type_name_S,
        'car_system_X': car_system_X,
        'car_type_name_X': car_type_name_X,
        'car_system_C': car_system_C,
        'car_type_name_C': car_type_name_C,
    }
    content = dict(info, **add)
    return render(request, 'user/overview.html', content)


# 品牌天地
def brand(request):
    main_navs = MainNav.objects.all()
    car_brand = main_navs[1]
    detail = MainOneNav.objects.filter(belong_to_id=car_brand.main_nav_id)
    detail_title = car_brand.main_nav_name
    url_name = 'brand'
    add = {
        'url_name': url_name,
        'details': detail,
        'detail_title': detail_title
    }
    content = dict(info, **add)
    return render(request, 'user/nav.html', content)


# 客户服务
def service(request):
    main_navs = MainNav.objects.all()
    customer_service = main_navs[2]
    detail = MainOneNav.objects.filter(belong_to_id=customer_service.main_nav_id)
    detail_title = customer_service.main_nav_name
    url_name = 'service'
    add = {
        'url_name': url_name,
        'details': detail,
        'detail_title': detail_title
    }
    content = dict(info, **add)
    return render(request, 'user/nav.html', content)


# 新闻资讯
def news(request):
    main_one_nav_id = MainOneNav.objects.filter(main_one_nav=9)[0].main_one_nav
    news = MainTwoNav.objects.filter(belong_to_id=main_one_nav_id)
    add = {
        'news': news,
        'dealer': dealer,
    }
    content = dict(info, **add)
    return render(request, 'user/news.html', content)


# 查询经销商
def dealer(request):
    return render(request, 'user/dealer.html', info)


# 预约试驾
@csrf_exempt
def test_drive(request):
    all_car_type = CarType.objects.all()
    all_car_info = CarInfo.objects.all()
    add = {
        'all_car_types': all_car_type,
        'all_car_infos': all_car_info
    }
    content = dict(info, **add)
    return render(request, 'user/test_drive.html', content)


# 点击车系后请求的车型信息
def test_car_info(request, car_info):
    car_type_id = CarType.objects.filter(car_type_name=car_info)[0].car_type_id
    car_infos = CarInfo.objects.filter(car_type=car_type_id)
    content = {}
    for n, i in enumerate(car_infos):
        content[n] = [i.car_name, i.car_price]
    return JsonResponse(content, safe=False)


# dealer,ajax请求数据（省份城市公司）
@csrf_exempt
def dealer_info(request):
    deader_data = {
        'province': provinces,
        'city': citys,
        'company': companys
    }
    return JsonResponse(deader_data, safe=False)


# 点击地图选择后ajax请求经销商地址电话信息
@csrf_exempt
def info_dealer(request, dis_name):
    Distri = {}
    Dis = Distributor.objects.filter(distributor_name=dis_name)
    for i in Dis:
        Distri['address'] = i.address,
        Distri['telephone'] = i.telephone
    return JsonResponse(Distri, safe=False)


# 品牌历史
def history(request):
    add = get_brand_info(1)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 品牌广告
def ads(request):
    add = get_brand_info(2)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 设计理念
def l_finesse(request):
    add = get_brand_info(3)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 环保理念
def eco_thinking(request):
    add = get_brand_info(4)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 概念车
def concept_cars(request):
    add = get_brand_info(11)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# club应用
def club_app(request):
    add = get_brand_info(6)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 手机互联
def mobile_connection(request):
    add = get_brand_info(7)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# g_book应用
def g_book(request):
    add = get_brand_info(8)
    content = dict(info, **add)
    return render(request, 'user/nav_detail.html', content)


# 新闻详情界面
def node(request, new_id):
    new = MainTwoNav.objects.get(main_two_nav=new_id)
    add = {
        'new': new
    }
    content = dict(info, **add)
    return render(request, 'user/new_detail.html', content)


# 车辆详情界面
def models(request, car_type=None, function=None):
    if car_type == 'CT':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'IS':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'ES':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'GS':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'LS':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'NX':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'RX':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'LX':
            if function == None:
                add = get_car_base_info(car_type, 0)
                content = dict(info, **add)
                return render(request, 'user/models.html', content)
            if function == 'exterior':
                add = get_car_base_info(car_type, 1)
                content = dict(info, **add)
                return render(request, 'user/models.html', content)
            if function == 'interior':
                add = get_car_base_info(car_type, 2)
                content = dict(info, **add)
                return render(request, 'user/models.html', content)
            if function == 'power':
                add = get_car_base_info(car_type, 3)
                content = dict(info, **add)
                return render(request, 'user/models.html', content)
            if function == 'safety':
                add = get_car_base_info(car_type, 4)
                content = dict(info, **add)
                return render(request, 'user/models.html', content)
            if function == 'spec':
                add = get_spec(car_type)
                content = dict(info, **add)
                return render(request, 'user/spec.html', content)
            if function == '3D':
                return render(request, 'user/3Dmodel.html')
    if car_type == 'RC':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')
    if car_type == 'LC':
        if function == None:
            add = get_car_base_info(car_type, 0)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'exterior':
            add = get_car_base_info(car_type, 1)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'interior':
            add = get_car_base_info(car_type, 2)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'power':
            add = get_car_base_info(car_type, 3)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'safety':
            add = get_car_base_info(car_type, 4)
            content = dict(info, **add)
            return render(request, 'user/models.html', content)
        if function == 'spec':
            add = get_spec(car_type)
            content = dict(info, **add)
            return render(request, 'user/spec.html', content)
        if function == '3D':
            return render(request, 'user/3Dmodel.html')


# 金融计划
def financial_service(request):
    all_car_type = CarType.objects.all()
    add = {
        'all_car_types': all_car_type,
    }
    content = dict(info, **add)
    return render(request, 'user/financial_service.html', content)


# 预约试驾表单提交
@csrf_exempt
def order_drive(request, car_name):
    if request.method == 'POST':
        of = OrderForm(request.POST)
        url = resolve_url(test_drive)
        if of.is_valid():
            name = of.cleaned_data['name']
            telephone = of.cleaned_data['telephone']
            try:
                sex = request.POST['sex']
            except:
                sex = ''
            province_num = int(request.POST['province'])
            city_num = int(request.POST['city'])
            dealer_num = int(request.POST['dealer'])
            plan_time = request.POST['plan_time']
            feedback_time = request.POST['feedback_time']
            province = provinces[province_num]
            city = citys[province_num][city_num]
            dealer = companys[province_num][city_num][dealer_num]
            OrderDrive.objects.create(user_name=name, car_name=car_name, sex=sex,
                                      telephone=telephone, province=province,
                                      city=city,dealer=dealer, plan_time=plan_time,
                                      feedback_time=feedback_time)
            return render(request, 'user/skip.html', {'message': '成功', 'url': url})
        else:
            return render(request, 'user/skip.html', {'message': '填写错误', 'url': url})
    else:
        url = resolve_url(index)
        return render(request, 'user/skip.html', {'message': '不能直接访问', 'url': url})


# 页面跳转
def skip(request):
    return render(request, 'user/skip.html')


# 后台登录
@csrf_exempt
def login(request):
    global ErrorNum
    yzm = False
    if ErrorNum > 0:
        yzm = True
    if ErrorNum <= 3:
        if request.method == 'POST':
            lf = LoginForm(request.POST)
            if lf.is_valid():
                account = lf.cleaned_data['account']
                password = lf.cleaned_data['password']
                if password == '123456':
                    user_id_valid = User.objects.filter(account=account, password=password)
                else:
                    pwd = calc_md5(password)
                    user_id_valid = User.objects.filter(account=account, password=pwd)
                if user_id_valid:
                    request.session['account'] = user_id_valid[0].account
                    # 保存时间为一天
                    request.session.set_expiry(86400)
                    if user_id_valid[0].user_type_id == 1:
                        return redirect('/backstage/staff/')
                    else:
                        return redirect('/backstage/dealer_admin/')
                else:
                    ErrorNum += 1
                    return render(request, 'backstage/login.html', {'message': '密码或用户名输入错误', 'yzm': yzm})
            else:
                return render(request, 'backstage/login.html', {'message': '密码或用户名为空', 'yzm': yzm})
        else:
            lf = LoginForm()
            return render(request, 'backstage/login.html', {'lf': lf, 'yzm': yzm})
    else:
        ErrorNum = 0
        url = resolve_url(index)
        return render(request, 'user/skip.html', {'message': '输入密码错误次数过多，稍后页面会跳转', 'url': url})


# 修改密码
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            account = lf.cleaned_data['account']
            password = lf.cleaned_data['password']
            again_password = request.POST.get('again_password')
            if password == again_password:
                if password == '123456':
                    user_id_valid = User.objects.filter(account=account, password=password)
                else:
                    pwd = calc_md5(password)
                    user_id_valid = User.objects.filter(account=account, password=pwd)
                if user_id_valid:
                    url = '/backstage/confirm/'+account+'/'
                    return redirect(url)
                else:
                    return render(request, 'backstage/change_pwd.html', {'message': '密码输入错误'})
            else:
                return render(request, 'backstage/change_pwd.html', {'message': '两次输入密码不同'})
        else:
            return render(request, 'backstage/change_pwd.html', {'message': '密码或用户名为空'})
    else:
        return render(request, 'backstage/change_pwd.html')


# 确认密码
@csrf_exempt
def confirm(request, account):
    user = User.objects.get(account=account)
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            password = lf.cleaned_data['password']
            user.password = calc_md5(password)
            user.save()
            return render(request, 'backstage/login.html')
        else:
            return render(request, 'backstage/confirm.html', {'message': '输入有误，请重新输入'})
    else:
        return render(request, 'backstage/confirm.html', {'account': account})


# 员工后台
@csrf_exempt
def staff(request, num=None):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        if user.user_type.user_type == 1:
            user_agent = {
                'user': user,
            }
            if num == None:
                order = OrderDrive.objects.filter(dealer=user.belong_to.distributor_name, staff_id=None)
                add = {
                    'name': '所有订单',
                    'orders': order
                }
                content = dict(user_agent, **add)
                return render(request, 'staff/staff.html', content)
            if num == 2:
                order = OrderDrive.objects.filter(dealer=user.belong_to.distributor_name, staff_id=user.user_id, confirm=None)
                add = {
                    'name': '待处理订单',
                    'orders': order
                }
                content = dict(user_agent, **add)
                return render(request, 'staff/deal.html', content)
            if num == 3:
                order = OrderDrive.objects.filter(dealer=user.belong_to.distributor_name, staff_id=user.user_id, confirm=1)
                add = {
                    'name': '已处理订单',
                    'orders': order
                }
                content = dict(user_agent, **add)
                return render(request, 'staff/dealed.html', content)
            if num == 4:
                car_type = CarInfo.objects.all()
                add = {
                    'name': '客户购买填写基本信息',
                    'car_type': car_type,
                }
                content = dict(user_agent, **add)
                return render(request, 'staff/sale_car.html', content)
            if num == 5:
                sale_history = BuyCar.objects.filter(staff_id=user)
                add = {
                    'name': '销售记录',
                    'orders': sale_history,
                }
                content = dict(user_agent, **add)
                return render(request, 'staff/sale_history.html', content)
        else:
            return redirect('/backstage/login/')
    except:
        return redirect('/backstage/login/')


# 处理预约试驾
def deal(request, order_id):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        order = OrderDrive.objects.get(id=order_id)
        order.staff_id = user
        order.save()
        url = resolve_url(staff)
        return render(request, 'user/skip.html', {'message': '操作成功,请及时和客户通信！！', 'url': url})
    except:
        return redirect('/backstage/login/')


# 完成预约试驾的订单
def finish(request, order_id):
    order = OrderDrive.objects.get(id=order_id)
    order.confirm = 1
    order.save()
    url = resolve_url(staff, 2)
    return render(request, 'user/skip.html', {'message': '操作成功,预约完成！！', 'url': url})


# 在线购买
@csrf_exempt
def online_buy(request):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        if user.user_type.user_type == 1:
            if request.method == 'POST':
                bf = BuyForm(request.POST)
                if bf.is_valid():
                    name = bf.cleaned_data['name']
                    telephone = bf.cleaned_data['telephone']
                    address = bf.cleaned_data['address']
                    month_salary = bf.cleaned_data['month_salary']
                    id_card = bf.cleaned_data['id_card']
                    bank_card = bf.cleaned_data['bank_card']
                    first_pay = bf.cleaned_data['first_pay']
                    month_pay = bf.cleaned_data['month_pay']
                    sex = request.POST['sex']
                    car_id = request.POST['car_type']
                    car_info = CarInfo.objects.get(car_id=car_id)
                    car_name = car_info.car_name
                    BuyCar.objects.create(user_name=name, car_name=car_name, sex=sex,
                                          telephone=telephone, dealer=address, month_pay=month_pay,
                                          month_salary=month_salary, id_card=id_card,
                                          bank_card=bank_card, staff_id=user, first_pay=first_pay)
                    inventory = InventoryManagement.objects.get(car_info=car_info)
                    inventory.num -= 1
                    inventory.save()
                    url = resolve_url(staff, 4)
                    return render(request, 'user/skip.html', {'message': '提交购买订单成功', 'url': url})
                return render(request, 'staff/sale_car.html', {'message': '输入错误，请重新输入！！'})
        else:
            return redirect('/backstage/login/')
    except:
        return redirect('/backstage/login/')


# 经销商后台管理界面
@csrf_exempt
def dealer_admin(request, num=None):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        if user.user_type.user_type == 2:
            user_agent = {'user': user}
            if num == None:
                if request.method == 'POST':
                    name = request.POST.get('name')
                    staff1 = User.objects.filter(user_name__exact=name)
                    staff2 = User.objects.filter(account__exact=name)
                    if staff1:
                        staff = staff1
                    else:
                        staff = staff2
                    add = {
                        'name': '员工管理',
                        'staff': staff
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/dealer_admin.html', content)
                else:
                    staff = User.objects.filter(belong_to=user.belong_to, user_type_id=1)
                    add = {
                        'name': '员工管理',
                        'staff': staff
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/dealer_admin.html', content)
            if num == 2:
                inventory = InventoryManagement.objects.filter(distributor=user.belong_to)
                add = {
                    'name': '车辆库存管理',
                    'inventory': inventory
                }
                content = dict(user_agent, **add)
                return render(request, 'dealer/inventory.html', content)
            if num == 3:
                if request.method == 'POST':
                    name = request.POST.get('name')
                    try:
                        staff_id = User.objects.get(account=name)
                        order = OrderDrive.objects.filter(dealer=user.belong_to.distributor_name, staff_id=staff_id, confirm=1)
                    except:
                        order = OrderDrive.objects.filter(user_name=name, confirm=1)
                    add = {
                        'name': '查询预约记录',
                        'orders': order
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/order.html', content)
                else:
                    order = OrderDrive.objects.filter(dealer=user.belong_to.distributor_name, confirm=1)
                    add = {
                        'name': '查询预约记录',
                        'orders': order
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/order.html', content)
            if num == 4:
                if request.method == 'POST':
                    name = request.POST.get('name')
                    try:
                        staff_id = User.objects.get(account=name)
                        buy = BuyCar.objects.filter(dealer=user.belong_to.distributor_name, staff_id=staff_id)
                    except:
                        buy = BuyCar.objects.filter(user_name=name)
                    add = {
                        'name': '查询预约记录',
                        'buys': buy
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/buy.html', content)
                else:
                    buy = BuyCar.objects.filter(dealer=user.belong_to.distributor_name)
                    add = {
                        'name': '查询购买记录',
                        'buys': buy
                    }
                    content = dict(user_agent, **add)
                    return render(request, 'dealer/buy.html', content)
        else:
            return redirect('/backstage/login/')
    except:
        return redirect('/backstage/login/')


# 修改车辆库存
@csrf_exempt
def inventoryupdate(request, inventory_id):
    car_info = InventoryManagement.objects.get(id=inventory_id)
    if request.method == 'POST':
        num = int(request.POST.get(car_info.car_info.car_name))
        car_info.num = num
        car_info.save()
        url = resolve_url(dealer_admin, 2)
        return render(request, 'user/skip.html', {'message': '修改完成', 'url': url})
    return render(request, 'dealer/dealer_admin.html')


# 增加员工
@csrf_exempt
def add(request):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        content = {
            'user': user,
            'name': '增加员工'
        }
        if request.method == 'POST':
            useraccount = request.POST.get('account')
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            tel = request.POST.get('tel')
            email = request.POST.get('email')
            address = request.POST.get('address')
            User.objects.create(account=useraccount, user_name=name, password='123456',
                                sex=sex, telephone=tel, email=email, address=address,
                                belong_to=user.belong_to, user_type_id=1)
            url = resolve_url(dealer_admin)
            return render(request, 'user/skip.html',{'message': '添加成功', 'url': url})
        else:
            return render(request, 'dealer/add.html', content)
    except:
        return redirect('/backstage/login/')


# 修改员工信息
@csrf_exempt
def update(request, account_id):
    try:
        account = request.session['account']
        user = User.objects.get(account=account)
        if user.user_type.user_type == 2:
            user_agent = {
                'user': user,
                'name': '修改信息',
                'display': 1
            }
            staff = User.objects.get(account=account_id)
            if request.method == 'POST':
                staff.user_name = request.POST.get('name')
                staff.sex = request.POST.get('sex')
                staff.address = request.POST.get('address')
                staff.email = request.POST.get('email')
                staff.telephone = request.POST.get('tel')
                staff.save()
                url = resolve_url(dealer_admin)
                return render(request, 'user/skip.html', {'message': '修改完成', 'url': url})
            else:
                add = {
                    'staff': staff
                }
                content = dict(user_agent, **add)
                return render(request, 'dealer/add.html', content)
        else:
            return redirect('/backstage/login/')
    except:
        return redirect('/backstage/login/')


# 删除员工
def delete(request, account_id):
    staff = User.objects.get(account=account_id)
    staff.delete()
    url = resolve_url(dealer_admin)
    return render(request, 'user/skip.html', {'message': '删除成功！！！', 'url': url})


# 页面404
@csrf_exempt
def pagenotfound(request):
    return render_to_response('404.html')


# 页面 500
@csrf_exempt
def page_error(request):
    return render_to_response('404.html')

