
var likes=document.getElementsByClassName('like');
for(var i=0;i<likes.length;i++){
    likes[i].addEventListener('click',function () {
        var name=this.src.split('/');
        if(name[name.length-1]==='shapesdark.png'){
            this.src='shapes.png';
        }else{
            this.src='shapesdark.png';
        }
    });
}
function initMap() {
    var centerLatLng = new google.maps.LatLng(59.2650709, 30.2522799);
    var mapOptions = {
        center: centerLatLng,
        zoom: 11
    };
    var map = new google.maps.Map(document.getElementById("main-map"), mapOptions);
}
google.maps.event.addDomListener(window, "load", initMap);
