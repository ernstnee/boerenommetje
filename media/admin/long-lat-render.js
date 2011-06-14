$(document).ready(function() {

    $('#id_address').parent().append("<div id='map_canvas' style='width:380px; height:200px; margin: 20px; margin-left: 105px;' ></div>");

    var latlng = new google.maps.LatLng(52.3, -5.1);
    var myOptions = {
      zoom: 15,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    
    
    var map = new google.maps.Map(document.getElementById("map_canvas"),  myOptions);
 

    $('#id_address').change(function() {
      updateMapPosition(map);
    });

    // on load update map if address is not empty 
    if ($('#id_address').val()) {
      updateMapPosition(map);
    }
    
});


 
function updateMapPosition(map) {
  var geocoder = new google.maps.Geocoder();
  var position = geocoder.geocode({'address': $('#id_address').val()} ,
    function(results,status) { 
      if (status == google.maps.GeocoderStatus.OK) {
        if (status != google.maps.GeocoderStatus.ZERO_RESULTS) {
          map.setCenter(results[0].geometry.location);
          var marker = new google.maps.Marker({map:map, position:results[0].geometry.location});
        }
      }
      else {
        alert("Adresse inconnue par google map, rajoutez le code postal et le pays.");
      }
    }
  );
}

