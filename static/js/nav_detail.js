document.addEventListener('mousewheel',function(event){
    // console.log(window.pageYOffset)
    var subnav_fixed = document.getElementsByClassName('subnav_fixed')[0];
    // console.log(event.wheelDelta)
    if(event.wheelDelta<0){
    	// console.log(window.pageYOffset)
    	subnav_fixed.style.marginTop =  '-60px';
    }
    if(event.wheelDelta>0){
    	if(window.pageYOffset <= 60){
    		subnav_fixed.style.marginTop =  '0px';
    	}
    }
});
//休眠
function sleep(n) {
    var start = new Date().getTime();
    //  console.log('休眠前：' + start);
    while (true) {
        if (new Date().getTime() - start > n) {
            break;
        }
    }
    // console.log('休眠后：' + new Date().getTime());
}


// 重新排序
// var oUl1=document.getElementsByClassName('nav_detail')[0];
//
// var aLi=oUl1.getElementsByClassName('move');
// var arr=[];
//
// for(var i=0;i<aLi.length;i++)  //把li用数组表示
// {
//     arr[i]=aLi[i];
// }
// arr.sort(function(li1,li2){
//     var n1=parseInt(li1.id);
//     var n2=parseInt(li2.id);
//     return n1-n2;  //升序排列
// })
// for(var i=0;i<arr.length;i++){
//     oUl1.appendChild(arr[i]);   //排序之后再写入
// }
