function initMap() {
    var centerLatLng = new google.maps.LatLng(59.2650709, 30.2522799);
    var mapOptions = {
        center: centerLatLng,
        zoom: 11
    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}
google.maps.event.addDomListener(window, "load", initMap);
