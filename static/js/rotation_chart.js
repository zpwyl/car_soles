
var img_num = document.getElementsByClassName('pic').length;
var curIndex= img_num;//初始换显示第一张
function slideTo (index) {
    var indexs = parseInt(index);
    if (indexs === img_num+1) {
        indexs = 1;
    }
    if (indexs === 0) {
        indexs = img_num;
    }
    var pic = document.getElementById("slideshow_photo").childNodes;
    for(var i=0;i<pic.length;i++){//改变zIndex属性
        if(pic[i].attributes && pic[i].attributes['index'] && parseInt(pic[i].attributes['index'].value)===indexs){
            pic[i].style.zIndex=2;
            curIndex=indexs;
        }
        else if(pic[i].attributes && pic[i].attributes['index']) {
            pic[i].style.zIndex=1;
        }
    }
    var bts = document.getElementsByClassName("slideshow-bt");
    for(var i=0;i<bts.length;i++){//改变显示的效果
        if(parseInt(bts[i].attributes['index'].value)===indexs){
            bts[i].className="slideshow-bt bt-on";
        }
        else bts[i].className = "slideshow-bt";
    }
}

var bts = document.getElementsByClassName("slideshow-bt");
for(var i=0;i<bts.length;i++){
    bts[i].onclick = function  () {
        slideTo(this.attributes['index'].value);
    }
}
var start = true;
setInterval(function  () {
    if(start === true){
        if(curIndex+1>5) curIndex=0;
        slideTo(curIndex);
    }
},5000);

var pic = document.getElementById('slideshow_wrapper');
var leftBut = document.getElementById('left');
var rightBut = document.getElementById('right');
pic.addEventListener("mouseover", func1, false);
function func1(){
        leftBut.style.display = 'block';
        rightBut.style.display = 'block';
        start = false;
}
pic.addEventListener("mouseout", func2, false);
function func2() {
    leftBut.style.display = 'none';
    rightBut.style.display = 'none';
    start = true;
}

leftBut.addEventListener("click", func3, false);
function func3(){
    // console.log(curIndex);
    curIndex--;
    slideTo(curIndex);
}
rightBut.addEventListener("click", func4, false);
function func4(){
    // console.log(curIndex);
    curIndex++;
    slideTo(curIndex);
}

document.getElementById('right').click();