// Haritanın türkiye başlangıç konumu enlem ve boylamdan veriri

var myLatLng = {
    lat: 39.0578771,
    lng: 34.4999527
};
var mapOptions = {
    center: myLatLng,
    zoom: 6.2,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

var currentLoc;

// Hide result box
document.getElementById("output").style.display = "none";

// Create/Init map
var map = new google.maps.Map(document.getElementById('google-map'), mapOptions);

// Create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

// Create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

// Bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);


// Define calcRoute function
function calcRoute() {
    //create request
    var request = {
        origin: document.getElementById("location-1").value,
        destination: document.getElementById("location-2").value,
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC
        
    }

    // Routing
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {

            //Get distance and time            

            $("#output").html("<div class='result-table'> Sürüş Mesafesi: " + result.routes[0].legs[0].distance.text + ".<br />Süre: " + result.routes[0].legs[0].duration.text + ".</div>");
            document.getElementById("output").style.display = "block";
            //display route
            directionsDisplay.setDirections(result);
        } else {
            //delete route from map
            directionsDisplay.setDirections({
                routes: []
            });
            //center map in London
            map.setCenter(myLatLng);

            //Show error message           

            alert("Rota oluşturulamadı lütfen daha sonra tekrar deneyin");
            clearRoute();
        }
    });

}

// Clear results

function clearRoute() {
    document.getElementById("output").style.display = "none";
    document.getElementById("location-1").value = "";
    document.getElementById("location-2").value = "";
    directionsDisplay.setDirections({
        routes: []
    });

}

// Create autocomplete objects for all inputs

var options = {
    types: ['(cities)']
}


var input1 = document.getElementById("location-1");
var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

var input2 = document.getElementById("location-2");
var autocomplete2 = new google.maps.places.Autocomplete(input2, options);


//var x = document.getElementById("demo");
function getLoc() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPos);
    } else {
        //x.innerHTML = "Geolocation is not supported by this browser.";
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPos(position) {
    currentLoc = position.coords.latitude + ', ' + position.coords.longitude;
    document.getElementById("location-1").style.display = "inline";
    document.getElementById("location-1").value = position.coords.latitude + ', ' + position.coords.longitude;
}

function showKazalar() {
    var kazaPoint = []

    kazalar.forEach(kaza => {
        kaza = kaza.split('|');
        kazaPoint.push(new google.maps.Marker({
            position: {
                'lat': parseFloat(kaza[1]),
                'lng': parseFloat(kaza[3])
            },
            map: map,
        }))
    });
}

$(document).ready(function () {
    showKazalar();

});