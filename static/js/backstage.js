var n = parseInt(window.location.pathname.split('/')[3]);
if (isNaN(n)){
    n = 1
}
var li = document.getElementsByClassName('li');
li[n-1].className = 'red li';
function over(e){
    for(var i=0;i<li.length;i++){
        li[i].className = 'li'
    }
}
function out(e){
    li[n-1].className = 'red li'
}
try{
    var text = document.getElementsByClassName('text')[0];
    text.onfocus = function (e) {
        if(e.path[0].value === '请输入姓名或员工工号'){
            e.path[0].value = '';
        }
    };
    text.onblur = function (e) {
        if(e.path[0].value === ''){
            e.path[0].value = '请输入姓名或员工工号'
        }
    }
}catch (e) {
    console.log(e)
}
try{
    var num = document.getElementsByClassName('num');
    for(var i=0;i<num.length;i++){
        num[i].onfocus = function (e) {
        if(e.path[0].value === '请输入修改后的库存数'){
            e.path[0].value = '';
        }
        };
        num[i].onblur = function (e) {
            if(e.path[0].value === ''){
                e.path[0].value = '请输入修改后的库存数'
            }
        };
    }

}catch (e) {
    console.log(e)
}