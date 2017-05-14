
function handleFiles() {
    var filesToUpload = document.getElementById('id_image').files;
    var file = filesToUpload[0];
    EXIF.getData(file, function() {
        var allMetaData = EXIF.getAllTags(this);
        var allMetaDataSpan = document.getElementById("allMetaDataSpan");
        //console.log(JSON.stringify(allMetaData, null, "\t"));
        //allMetaDataSpan.innerHTML = JSON.stringify(allMetaData, null, "\t");
        var long=allMetaData.GPSLongitude;
        var lat=allMetaData.GPSLatitude;
        console.log(long);
    });
}
document.getElementById('send').addEventListener('click',function () {
    
})