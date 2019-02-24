try{
    var car_info_name = document.getElementsByClassName('car_info_name');
    car_info_name[0].nextElementSibling.style.display = 'block';
    for(var i=0;i<car_info_name.length;i++) {
        car_info_name[i].addEventListener('click', function (e) {
            console.log(e);
            var table;
            var div;
            if(e.path[0].className === 'add'){
                table = e.path[1].nextElementSibling;
                div = e.path[1].getElementsByTagName('span')[0];
            }else{
                table = e.path[0].nextElementSibling;
                div = e.path[0].getElementsByTagName('span')[0];
            }
            console.log(table);
            if (table.style.display === 'none') {
                div.innerHTML = '-';
                table.style.display = 'block'
            } else {
                div.innerHTML = '+';
                table.style.display = 'none'
            }
        }, true)
    }

}catch (err) {
    console.log(err);
}
var length = document.getElementsByClassName('length').length;

var comment_data = document.getElementsByClassName('comment_data');
for(var j=0;j<comment_data.length;j++){
    comment_data[j].style.width = length*13 + '%';
}
