var origin = {
    api_home: location.origin
};
// finanical_service
function getJsonLength(jsonData) {
    var length=0;
    for(var ever in jsonData) {
        length++;
    }
    return length;
}

function car(e) {
    var car_type = document.getElementsByClassName('select_type')[0];
    var price = document.getElementsByClassName('all_price')[0];
    if(car_type){
        car_type.className = ''
    }
    if(price){
        price.className = ''
    }
    var p = e.getElementsByTagName('p');
    p[0].className = 'select_type';
    p[1].className = 'all_price';
    var all_price = parseInt(document.getElementsByClassName('all_price')[0].innerHTML);
    var percentage = document.getElementById('percentage');
    var first_payments = document.getElementById('first_payments');
    var interest_rate = document.getElementById('interest_rate');
    var monthly_payment = document.getElementById('monthly_payment');
    var time = document.getElementById('time');
    try{
        first_payments.innerHTML = all_price * parseInt(percentage.value) * 0.01;
        percentage_show.innerHTML = percentage.value + '%';
        monthly_payment.innerHTML = Math.ceil(all_price*(1-parseInt(percentage.value)*0.01)*(1+0.0199)/time.value);
        if(interest_rate.innerHTML === ''){
            interest_rate.innerHTML = 1.99 + '%'
        }
    }catch (e) {

    }
    function change_product(n, m) {
        if(parseInt(time.value)===n){
            first_payments.innerHTML = all_price * parseInt(percentage.value) * 0.01;
            percentage_show.innerHTML = percentage.value + '%';
            monthly_payment.innerHTML = Math.ceil(all_price*(1-parseInt(percentage.value)*0.01)*(1+m*0.01)/time.value);
            interest_rate.innerHTML = m + '%';
        }
    }
    try{
        time.onchange = function () {
            change_product(12, 1.99);
            change_product(24, 2.99);
            change_product(36, 3.99);
        };

        percentage.onchange = function () {
            var percentage_show = document.getElementById('percentage_show');
            percentage_show.innerHTML = percentage.value + '%';
            var n = parseInt(time.value);
            var m = parseFloat(interest_rate.innerHTML);
            change_product(n, m);
        };

    }catch (err) {
        console.log(err);
    }
    try{
        var info_form = document.getElementsByClassName('info_form')[0];
        var url = origin.api_home+'/order_drive/' + document.getElementsByClassName('select_type')[0].innerHTML + '/';
        info_form.setAttribute('action', url);
    }catch (err) {
        console.log(err);
    }

}

function car_sys(e){
    var type_car = document.getElementById('type_car');
    type_car.innerHTML = '';
    var car_info = e.getElementsByTagName('p')[0].innerText;
    $.ajax({
        url: origin.api_home+'/test_car_info/'+car_info+'/',
        type:"get",
        data: {},
        datatype:'json',
        error: function () {
            console.log("error")
        },
        success: function (data) {
            var length = getJsonLength(data);
            var Heml = '';
            for(var i=0; i<length;i++){
                 var str = "<li onclick='car(this)'><a><div class='car'><p>"+data[i][0]+"</p><p>"+data[i][1]+"</p></div></a></li>";
                 Heml += str
            }
            type_car.innerHTML = Heml;
        }
    });

}


var arr_sheng;
var arr_shi;
var arr_xian;
var osheng=document.getElementById("province");
var oshi=document.getElementById("city");
var oxian=document.getElementById("company");
if(osheng){
    $.ajax({
        url: origin.api_home+'/dealer_info/',
        type:"get",
        data: {},
        datatype:'json',
        error: function () {
            console.log("error")
        },
        success: function (data) {
            window.data = data;
            arr_sheng = data.province;
            arr_shi = data.city;
            arr_xian = data.company;
            input_arr(arr_sheng,osheng);//调用,给省下拉栏添元素
        }
    });

    var quanju_arr;//创建一个全局对象，用于存储一个中间数组

    function input_arr(arr,event){//封装一个函数，用于向下拉栏中添加元素
        for(var i=0;i<arr.length;i++){//下拉栏内的元素来源于数组中的元素，遍历数组
            var option=new Option(arr[i],i);//创建Option对象（这个O要大写），存入值
            event.appendChild(option);//把option添加到event对象的末尾
        }
    }

    osheng.onchange= function (e) {//给下拉栏绑定事件（当下拉栏元素改变时执行）
        oshi.options.length=1;//当省下拉栏改变时，清空市的下拉栏内元素
        oxian.options.length=1;//当省下拉栏改变时，清空县的下拉栏内元素
        var index=this.value;//每一个option标签都有一个value值索引，获取索引，用于数组中元素的选择
        var arr_shi_next=arr_shi[index];//获取当前选择省的市元素并赋给一个数组
        quanju_arr=arr_xian[index];//获取当前选择省中市的县元素并赋给定义的中间数组
        input_arr(arr_shi_next,oshi);//调用,给市下拉栏添元素
        var num = parseInt(osheng.value)+ 1;
        var province = e.srcElement[num].innerText;
        get_province(province);
    };

    oshi.onchange= function (e) {
        oxian.options.length=1;
        var index=this.value;
        var arr_xian_next=quanju_arr[index];
        input_arr(arr_xian_next,oxian);//调用,给县下拉栏添元素
        var num = parseInt(oshi.value)+ 1;
        var city = e.srcElement[num].innerText + '市';
        get_province(city);
    };

}

// dealer
try{
    var map = new BMap.Map("container");
    map.centerAndZoom(new BMap.Point(112.220017, 30.33505), 5);
    map.enableScrollWheelZoom(true);
    //开启鼠标滚轮缩放
    map.addControl(new BMap.NavigationControl());
    map.addControl(new BMap.ScaleControl());
    map.addControl(new BMap.OverviewMapControl());
    map.addControl(new BMap.MapTypeControl());

    var myGeo = new BMap.Geocoder();
    // 将地址解析结果显示在地图上，并调整地图视野
    oxian.onchange = function (e){
        var num = parseInt(oxian.value)+ 1;
        var company = e.srcElement[num].innerText;
        get_point(company);
    };
}catch (err) {
    console.log(err);
}

function get_province(space) {
    myGeo.getPoint(space, function(point) {
        if (point) {
            map.centerAndZoom(point, 10);
            map.addOverlay(new BMap.Marker(point));
        }
    })}

function get_point(space){
    $.ajax({
        url: origin.api_home+'/info_dealer/'+space+'/',
        type:"get",
        data: {},
        datatype:'json',
        error: function () {
            console.log("error")
        },
        success: function (data) {
            myGeo.getPoint(space, function(point){
                if (point) {
                    map.centerAndZoom(point, 20);
                    map.addOverlay(new BMap.Marker(point));
                    var opts = {
                        width : 300,     // 信息窗口宽度
                        height: 200,     // 信息窗口高度
                        title : space, // 信息窗口标题
                    };

                    var infoWindow = new BMap.InfoWindow("<p style='margin:20px 0'>电话："+ data.telephone+"</p> \
                        <p>"+data.address+"</p> \
                        </br> \
                        <input type='text'> <a href='http://map.baidu.com'>出发</a> <a href='/test_drive/'>预约试驾</a>", opts);  // 创建信息窗口对象
                    map.openInfoWindow(infoWindow, map.getCenter());      // 打开信息窗口
                }
                else{
                    var opts = {
                        width : 300,     // 信息窗口宽度
                        height: 200,     // 信息窗口高度
                    };

                    var infoWindow = new BMap.InfoWindow("<p style='line-height: 200px;text-align: center'>暂无信息</p>", opts);  // 创建信息窗口对象
                    map.openInfoWindow(infoWindow, map.getCenter());      // 打开信息窗口
                }
            });
        }
    });
}

var tel_error = document.getElementById('tel_error');
// 鼠标进入input框value变化
function fouse(e) {
    tel_error.style.display = 'none';
    if(e.value === '请输入姓名' || e.value === '请输入电话号码'){
        e.value = ''
    }
}
function blue(e) {
    if(e.value === ''){
        if(e.name === 'name'){
            e.value = '请输入姓名'
        }else{
        e.value = '请输入电话号码'
        }
    }else{
        if(e.name === 'telephone'){
            if(e.value.length !== 11){
                e.value = '请输入电话号码';
                tel_error.style.display = 'inline-block';
            }
        }
    }
}