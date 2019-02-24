var brand = document.getElementById('frame');
//菜单鼠标移入的事件
function showMeum(e){
    var detail = e.getElementsByClassName('detail')[0];
    detail.style.display = 'block';
}
function hideMeum(e){
    var detail = e.getElementsByClassName('detail')[0];
    detail.style.display = 'none';
}

//菜单细节移入事件
function showDetail(e){
    var div = e.getElementsByTagName('div')[0];
    var show = e.parentNode.getElementsByClassName('left_detail_right_show');
    show[0].className = 'left_detail_right';
    // console.log(show[0])
    div.className = 'left_detail_right_show';

}
function hideDetail(e){
    e.getElementsByTagName('div')[0].className = 'left_detail_right';
    var Initialization = e.parentNode.firstElementChild.nextElementSibling.getElementsByTagName('div')[0];
    Initialization.className = 'left_detail_right_show'
}
//页面加载完成后执行
window.onload = function(){
    //图片显示为适应浏览器大小
    try{
        var jsImg = document.getElementById("slideshow_wrapper");
        var jsPic = document.getElementsByClassName("pic")[0];
        var jsPic_height = getComputedStyle(jsPic,null).height;
        var str = 'height:'+ jsPic_height.toString();
        jsImg.setAttribute('style', str);
    }catch (err){
        console.log(err)
    }
    if(document.body.clientWidth<1100){
        var nav = document.getElementById('main_nav');
        nav.style.display = 'none';
    }else{
        var nav = document.getElementById('main_nav');
        nav.style.display = '';
    }
    try{
        var subnav_fixed = document.getElementsByClassName('subnav_fixed')[0];
        console.log(window.pageYOffset);
        if(window.pageYOffset === 0){
            subnav_fixed.style.marginTop =  '0px';
        }else{
            subnav_fixed.style.marginTop =  '-60px';
        }
    }catch (err) {
        console.log(err)
    }
};

//改变窗口时发生
window.onresize = function(){
    try{
        var jsImg = document.getElementById("slideshow_wrapper");
        var jsPic = document.getElementsByClassName("pic")[0];
        var jsPic_height = getComputedStyle(jsPic,null).height;
        var str = 'height:'+ jsPic_height.toString();
        jsImg.setAttribute('style', str);
    }catch (err){
        console.log(err)
    }
    if(document.body.clientWidth<1100){
        var nav = document.getElementById('main_nav');
        nav.style.display = 'none';
    }else{
        var nav = document.getElementById('main_nav');
        nav.style.display = '';
    }
};

