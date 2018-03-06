$(document).ready(function () {
    //    Création de la carte avec coordonnées GNSS latitude, longitude et niveau de zoom
    maCarte = L.map('map').setView([46.15197, -1.15385], 17);
    lControl = L.control.layers().addTo(maCarte);

    //    Ajout d'un fond de plan topo style IGN Scan25
    fondTopo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        maxZoom: 17
    });
    lControl.addBaseLayer(fondTopo, "Carte Topo");

    //    Fond de plan Ortho
    fondOrtho = L.tileLayer('img/xyz_larochelle/{z}/{x}/{y}.png', {
        maxZoom: 19,
        minZoom: 15
    }).addTo(maCarte);
    lControl.addBaseLayer(fondOrtho, "OrthoPhoto");

    //    Couche de ligne : Route
    $.getJSON('data/route.php', {},
        function (data) {
            vRoute = L.geoJSON(data, {
                style: function () {
                    return {
                        color: "#F00",
                        weight: 2,
                        opacity: 0.7,
                        dashArray: '15,8'
                    };
                }
//                onEachFeature: function(f, l) {
//                    l.on({
//                        click: function(e) {
////                            console.log(f.properties.NOM_VOIE_G); // Affiche l'attribut dans la console
////                            popup = L.popup({closeOnClick:false}).setLatLng(e.latlng).setContent(f.properties.NOM_VOIE_G).openOn(maCarte); // Affiche l'attribut dans dans une popup
//                            if (f.properties.NOM_VOIE_G) {
//                                popup = L.popup({closeOnClick:false}).setLatLng(e.latlng).setContent(f.properties.NOM_VOIE_G).openOn(maCarte);
//                            }
//                        }
//                    });
//                }
            });

            vRoute.addTo(maCarte);
            lControl.addOverlay(vRoute, "Route");
        });

    //    Couche de polygone : Surface d'eau
    $.getJSON('data/eau_light.geojson', {},
        function (data) {
            vSurfaceEau = L.geoJSON(data, {
                style: function (poly) {
                    if (poly.properties.REGIME == "Intermittent") couleurR = "#00F";
                    else if (poly.properties.REGIME == "Permanent") couleurR = "#A9D1F5";
                    else couleurR == "#A9D1F5";
                    return {
                        color: "#A9D1F5",
                        fillColor: couleurR,
                        weight: 0, // 0 = Pas de contour
                        opacity: 1,
                        fillOpacity: 1
                    };
                },
                onEachFeature: function(f, l) {
                    l.on({
                        click: function(e) {
                            contenu = "<b>Id : </b>" + f.properties.ID + "<br>";
                            contenu += "<b>Nature : </b>" + f.properties.NATURE + "<br>";
                            contenu += "<b>Régime : </b>" + f.properties.REGIME;
                            popup = L.popup({closeOnClick:false}).setLatLng(e.latlng).setContent(contenu).openOn(maCarte);
                        }
                    });
                }
            });

            vSurfaceEau.addTo(maCarte);
            lControl.addOverlay(vSurfaceEau, "Surface en eau");
        });

    //    Couche de point : Lieu Dit
    $.getJSON('data/lieu_light.geojson', {},
        function (data) {
            vLieuDit = L.geoJSON(data, {
                pointToLayer: function (pt, latlng) {
                    if (pt.properties.NATURE == "Lieu-dit habité")
                        return L.marker(latlng, {
                            icon: new L.Icon({
                                iconUrl: './img/location64.png',
                                iconSize: [28, 28],
                                iconAnchor: [14, 28]
                            })
                        });
                    else if (pt.properties.NATURE == "Quartier")
                        return L.circleMarker(latlng, {
                            radius: 8,
                            color: "#FFF",
                            fillColor: "#000",
                            weight: 3,
                            opacity: 1,
                            fillOpacity: 0.8
                        });
                    else
                        return L.circleMarker(latlng, {
                            radius: 8,
                            color: "#000",
                            fillColor: "#FFF",
                            weight: 3,
                            opacity: 1,
                            fillOpacity: 0.8
                        });
                },
                onEachFeature: function(entite, couche) {
//                    couche.bindTooltip(entite.properties.NOM, {permanent: false, sticky: false, opacity: 1, direction: "top"});
                    contenu = "<b>Nom : </b>" + entite.properties.NOM + "<br>";
                    contenu += "<b>Type : </b>" + entite.properties.NATURE;
                    couche.bindTooltip(contenu, {permanent: false, sticky: false, opacity: 1, direction: "top", className: "EtiqLieuDit"});
                }
            });

            vLieuDit.addTo(maCarte);
            lControl.addOverlay(vLieuDit, "Lieu-Dit");
        });

});


