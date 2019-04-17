from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class CarSystem(models.Model):
    car_system_id = models.AutoField(primary_key=True)
    car_system_name = models.CharField(max_length=10)

    def __str__(self):
        return "<{}>({})".format(self.car_system_id, self.car_system_name)


class CarType(models.Model):
    car_type_id = models.AutoField(primary_key=True)
    car_system_id = models.ForeignKey("CarSystem", on_delete=models.CASCADE, null=True, blank=True)
    car_type_name = models.CharField(max_length=10)
    car_type_all_name = models.CharField(max_length=30)
    car_type_img = models.ImageField(upload_to='Car_type/')

    def __str__(self):
        return "<{}>({})".format(self.car_type_id, self.car_type_name)


class CarTypeBaseName(models.Model):
    car_type_base_id = models.AutoField(primary_key=True)
    car_type_base_name = models.CharField(max_length=10)
    herf = models.CharField(max_length=50, null=True, blank=True)
    belong_to = models.ForeignKey('CarType', on_delete=models.CASCADE)

    def __str__(self):
        return "<{}>({}):{}".format(self.car_type_base_id, self.belong_to, self.car_type_base_name)


class CarTypeBaseInfo(models.Model):
    car_type_base_info_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=255, null=True, blank=True)
    src = models.ImageField(upload_to='CarTypeBaseInfo/')
    belong_to = models.ForeignKey('CarTypeBaseName', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.car_type_base_info_id, self.belong_to)


class CarDetailInfoName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    belong_to = models.ForeignKey('CarType', on_delete=models.CASCADE)

    def __str__(self):
        return "<{}>({})".format(self.id, self.name)


class CarDetailInfo(models.Model):
    car_detail_info_id = models.AutoField(primary_key=True)
    car_detail_info_name = models.CharField(max_length=20)
    car_detail_info = models.CharField(max_length=20)
    belong_to = models.ForeignKey('CarDetailInfoName', on_delete=models.CASCADE)

    def __str__(self):
        return "<{}>({})".format(self.car_detail_info_id, self.car_detail_info_name)


class CarInfo(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=20)
    car_type = models.ForeignKey("CarType", on_delete=models.CASCADE)
    car_price = models.CharField(max_length=10)
    car_3D = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.car_id, self.car_name)


class CarInfoDetailName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    belong_to = models.ForeignKey('CarInfo', on_delete=models.CASCADE)

    def __str__(self):
        return "<{}>({})".format(self.id, self.name)


class CarInfoDetail(models.Model):
    car_info_detail_id = models.AutoField(primary_key=True)
    car_info_detail_name = models.CharField(max_length=20)
    car_info_detail = models.CharField(max_length=20)
    belong_to = models.ForeignKey('CarInfoDetailName', on_delete=models.CASCADE)

    def __str__(self):
        return "<{}>({})".format(self.car_info_detail_id, self.car_info_detail_name)


class UserType(models.Model):
    user_type = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=3)

    def __str__(self):
        return "<{}>({})".format(self.user_type, self.user_type_name)


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=7)

    def __str__(self):
        return "<{}>({})".format(self.province_id, self.province_name)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=10)
    belong_to = models.ForeignKey('Province', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.city_id, self.city_name)


class Distributor(models.Model):
    distributor_id = models.AutoField(primary_key=True)
    distributor_name = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=50, blank=True)
    belong_to = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.distributor_id, self.distributor_name)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_name = models.CharField(max_length=10, null=True, blank=True)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE, null=True, blank=True)
    telephone = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    sex = models.PositiveSmallIntegerField(null=True, blank=True)
    belong_to = models.ForeignKey('Distributor', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.user_id, self.user_name)


class MainNav(models.Model):
    main_nav_id = models.AutoField(primary_key=True)
    main_nav_name = models.CharField(max_length=10)

    def __str__(self):
        return "<{}>({})".format(self.main_nav_id, self.main_nav_name)


class MainOneNav(models.Model):
    main_one_nav = models.AutoField(primary_key=True)
    main_one_nav_name = models.CharField(max_length=10)
    main_one_nav_img = models.ImageField(upload_to='OneNav/', null=True, blank=True)
    main_one_nav_title = models.CharField(max_length=50, null=True, blank=True)
    main_one_nav_brief = models.CharField(max_length=255, null=True, blank=True)
    belong_to = models.ForeignKey('MainNav', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.main_one_nav, self.main_one_nav_name)


class MainTwoNav(models.Model):
    main_two_nav = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    src = models.ImageField(upload_to='detail_layout/', blank=True, null=True)
    content = models.TextField(default='暂无记录', blank=True, null=True)
    belong_to = models.ForeignKey('MainOneNav', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(null=True, blank=True)
    brief = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.main_two_nav, self.title)


class SlideshowWrapper(models.Model):
    slideshow_wrapper_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, blank=True)
    content = models.CharField(max_length=255, blank=True)
    src = models.ImageField(upload_to='rotation_chart/', blank=True)
    href = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "<{}>({})".format(self.slideshow_wrapper_id, self.title)


class OrderDrive(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    car_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=2)
    telephone = models.CharField(max_length=11)
    province = models.CharField(max_length=2)
    city = models.CharField(max_length=10)
    dealer = models.CharField(max_length=30)
    plan_time = models.CharField(max_length=15, default='')
    feedback_time = models.CharField(max_length=15, default='')
    staff_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    confirm = models.CharField(max_length=1, null=True, blank=True)
    order_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<{}>({})".format(self.user_name, self.staff_id)


class BuyCar(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    car_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=2)
    telephone = models.CharField(max_length=11)
    dealer = models.CharField(max_length=30)
    staff_id = models.ForeignKey('User', on_delete=models.CASCADE)
    buy_time = models.DateTimeField(default=timezone.now)
    first_pay = models.CharField(max_length=10)
    month_pay = models.CharField(max_length=10)
    month_salary = models.CharField(max_length=10)
    id_card = models.CharField(max_length=18)
    bank_card = models.CharField(max_length=19)

    def __str__(self):
        return "<{}>({})".format(self.id, self.user_name)


class InventoryManagement(models.Model):
    id = models.AutoField(primary_key=True)
    car_info = models.ForeignKey('CarInfo', on_delete=models.CASCADE)
    distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)
    num = models.IntegerField()