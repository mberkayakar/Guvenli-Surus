// Haritanın türkiye başlangıç konumu enlem ve boylamdan veriri

var anlikKonum = null;
var kazaKonumlar = [];

var myLatLng = {
    lat: 39.0578771,
    lng: 34.4999527
};
var mapOptions = {
    center: myLatLng,
    zoom: 6.2,
    streetViewControl: false,
    mapTypeControl: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

var baslangic =new google.maps.Marker({
    position: null,
    map: map
     
}); 
var bitis =new google.maps.Marker({
    position: null,
    map: map
 
});  


var icons = {
    start: new google.maps.MarkerImage(
        // URL
        'http://maps.google.com/mapfiles/ms/micons/blue.png',
        // (width,height)
        new google.maps.Size(44, 32),
        // The origin point (x,y)
        new google.maps.Point(0, 0),
        // The anchor point (x,y)
        new google.maps.Point(22, 32)),
    end: new google.maps.MarkerImage(
        // URL
        'http://maps.google.com/mapfiles/ms/micons/green.png',
        // (width,height)
        new google.maps.Size(44, 32),
        // The origin point (x,y)
        new google.maps.Point(0, 0),
        // The anchor point (x,y)
        new google.maps.Point(22, 32))
};


var currentLoc = {
    'lat': '',
    'lng': ''
};

// Hide result box
document.getElementById("output").style.display = "none";

// Create/Init map
var map = new google.maps.Map(document.getElementById('google-map'), mapOptions);
const trafficLayer = new google.maps.TrafficLayer();


// Create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

// Create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer({
    map: map,
    suppressMarkers: true
});

// Bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);



// Define calcRoute function
function calcRoute() {
    baslangic.setMap(null);
    bitis.setMap(null);
    if (odaklama==true)
    kameraodakla()
    //create request
    var request = {
        origin: document.getElementById("location-1").value,
        destination: document.getElementById("location-2").value,
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC
    }

    function makeMarker(position, icon, title, map) {
        return new google.maps.Marker({
            position: position,
            map: map,
            icon: icon,
            title: title
        });
    }
    // Routing
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {

            //Get distance and time            
            var leg = result.routes[0].legs[0];
            baslangic = makeMarker(leg.start_location, icons.start, "start", map);
            bitis = makeMarker(leg.end_location, icons.end, "end", map);

            $("#output").html("<div class='result-table'>  Sürüş Mesafesi: " + result.routes[0].legs[0].distance.text + ".<br />Süre: " + result.routes[0].legs[0].duration.text + ".</div>");
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
    baslangic.setMap(null);
    bitis.setMap(null);

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

var anlikKonumIcon = {
    url: "https://i.hizliresim.com/8O2iHy.png",
    scaledSize: new google.maps.Size(30, 30), // scaled size
};

function showPos(position) {
    if (anlikKonum != null)
        anlikKonum.setMap(null);
    anlikKonum = new google.maps.Marker({
        position: {
            'lat': position.coords.latitude,
            'lng': position.coords.longitude
        },
        map: map,
        icon: anlikKonumIcon
    })
    currentLoc['lat'] = position.coords.latitude;
    currentLoc['lng'] = position.coords.longitude;

    document.getElementById("location-1").value = position.coords.latitude + ', ' + position.coords.longitude;
}

function deneme(lat, lng) {
    debug = true;
    if (anlikKonum != null)
        anlikKonum.setMap(null);
    anlikKonum = new google.maps.Marker({
        position: {
            'lat': lat,
            'lng': lng
        },
        map: map,
        icon: anlikKonumIcon
    })
    currentLoc['lat'] = lat;
    currentLoc['lng'] = lng;

    document.getElementById("location-1").value = lat + ', ' + lng;
}

function showKazalar() {
    var kazaPoint = []
    var baslangicIcon = {
        url: "https://i.hizliresim.com/xH3SCp.png",
        scaledSize: new google.maps.Size(20, 25), // scaled size

    };
    var bitisIcon = {
        url: "https://i.hizliresim.com/2QWAVj.png",
        scaledSize: new google.maps.Size(20, 25), // scaled size

    };
    var kazaIcon = {
        url: "https://i.hizliresim.com/C9hTed.png",
        scaledSize: new google.maps.Size(25, 20), // scaled size

    };
    var uyariIcon = {
        url: "https://i.hizliresim.com/VY2JOM.png",
        scaledSize: new google.maps.Size(20, 20), // scaled size

    };
    kazaKonumlar.forEach(kaza => {
        marker = {
            position: {
                'lat': parseFloat(kaza['lat']),
                'lng': parseFloat(kaza['lng'])
            },
            map: map
        }
        if (kaza['sorun'] == "Kaza")
            marker.icon = kazaIcon;
        else if (kaza['sorun'] == "Tehlike")
            marker.icon = uyariIcon;

        kazaPoint.push(new google.maps.Marker(marker))
    });
}

function kazaGoster(enlem, boylam) {
    console.log(parseFloat(enlem), parseFloat(boylam));


    map.setZoom(17)
    map.setCenter({
        'lat': parseFloat(enlem),
        'lng': parseFloat(boylam),
    });
    window.scrollTo(0, 0);
}

$(".toggle").click(function () {
    $('.kaza-container').toggleClass("expand");
});


function getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2) {
    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2 - lat1); // deg2rad below
    var dLon = deg2rad(lon2 - lon1);
    var a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var d = R * c; // Distance in km
    return d;
}

function deg2rad(deg) {
    return deg * (Math.PI / 180)
}


var siraliKazalar = [];

function yakinlikHesapla() {
    $("#kazalar").empty()
    kazaKonumlar.forEach(kaza => {

        var mesafe = getDistanceFromLatLonInKm(currentLoc['lat'], currentLoc['lng'], kaza['lat'], kaza['lng']);

        siraliKazalar.push({
            'mesafe': mesafe.toFixed(2),
            'lat': kaza['lat'],
            'lng': kaza['lng'],
            'kazaTur': kaza['sorun'],
            'id': kaza['id'],
            'ana_unsur': kaza['ana_unsur'],
        });
        // console.log(mesafe.toFixed(3))

    });
    siraliKazalar.sort((a, b) => (a.mesafe > b.mesafe) ? 1 : -1);

    /*
    console.log('\n\nSırasız');
    console.log(siraliKazalar);
    

    console.log('\n\nSıralı');
    console.log(siraliKazalar);
    */
   var audio = new Audio('https://media.geeksforgeeks.org/wp-content/uploads/20190531135120/beep.mp3');
   function play() { 
 
    audio.play(); 
} 

 

    var yakindakiKazalarSayi = 0;
    var mesafeStringi;
    siraliKazalar.forEach(kaza => {
        if (kaza['mesafe'] < 10) {
            if (kaza['mesafe'] < 1) {
                mesafeStringi = (kaza['mesafe'] * 1000).toString() + " Metre";
            } else {
                mesafeStringi = (kaza['mesafe']).toString() + " Kilometre"
            }
            yakindakiKazalarSayi++;
            $("#kazalar").append(`
                <li id="${kaza['id']}">
                <button class="kaza-liste" onClick =" kazaGoster(${kaza['lat']}, ${kaza['lng']})">
                <div class="row" style="width: 100%;">
                    <div class="col-md-3">${mesafeStringi}</div>
                    <div class="col-md-3">${kaza['kazaTur']}</div>
                    <div class="col-md-3">${kaza['ana_unsur']}</div>
                </div>
                </button>
            </li>`);

        } else {
            //console.log(kaza);
        }
    });
    $('#kazaSayisiSpan').text(yakindakiKazalarSayi)
    siraliKazalar.length = 0
}
var kitlimi = false;

function haritakilitle() {
    if (kitlimi === true) {
        map.setOptions({
            draggable: true

        });
        document.getElementById("haritaKilitleBtn").classList.remove("fa-lock");
        document.getElementById("haritaKilitleBtn").classList.add("fa-unlock");
        kitlimi = false;
    } else {
        map.setOptions({
            draggable: false
        });
        document.getElementById("haritaKilitleBtn").classList.remove("fa-unlock");
        document.getElementById("haritaKilitleBtn").classList.add("fa-lock");
        kitlimi = true;
    }
}
var myVar ;
var odaklama = false;
function kameraodakla() {
   
    
    if (odaklama === false) {
        map.setOptions({
            draggable: false,
            zoom:17

        });

        map.panTo(currentLoc)
        document.getElementById("kamerakilitle").classList.remove("fa-camera");
        document.getElementById("kamerakilitle").classList.add("fa-map-marker");
        odaklama = true;
        myVar = setInterval(function(){
            map.panTo(currentLoc)
            map.setZoom(17)
        }, 2000);
    } else {
        map.setOptions({
            draggable: true
        });
        
        clearInterval(myVar);
        document.getElementById("kamerakilitle").classList.remove("fa-map-marker");
        document.getElementById("kamerakilitle").classList.add("fa-camera");
        odaklama = false;
    }
}


var trafikvarmı = false;

function trafikgoster() {
    if (trafikvarmı === false) {
        trafficLayer.setMap(map);
        document.getElementById("trafikGosterBtn").classList.remove("fa-road");
        document.getElementById("trafikGosterBtn").classList.add("fa-car");
        trafikvarmı = true;
    } else {
        trafficLayer.setMap(null);
        document.getElementById("trafikGosterBtn").classList.remove("fa-car");
        document.getElementById("trafikGosterBtn").classList.add("fa-road");
        trafikvarmı = false;
    }
}

var debug = false;
$(document).ready(function () {
    kazalar.forEach(kaza => {
        kaza = kaza.split('|');
        kazaKonumlar.push({
            'id': kaza[1],
            'lat': kaza[3],
            'lng': kaza[5],

            'sorun': kaza[7],
            'ana_unsur': kaza[9]

        });
    });

    showKazalar();
    getLoc();

    setInterval(function () {
        if (!debug)
            getLoc();
        yakinlikHesapla();
        
    }, 2000);


});