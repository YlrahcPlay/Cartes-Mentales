// Quand la page html est chargé
$(document).ready(function() {
  // Création de la carte  
  maCarte = L.map('map', {
    center: [46.15197, -1.15385], // Centrage de la carte (Coordonnées Latitude, Longitude)
    zoom: 17, // Niveau de zoom au chargement de la carte
    zoomControle: false // Désactivation du controleur de zoom (permet de la déplacer, par défaut = 'Haut-Gauche')
  });
  // ALTERNATIVE
  // maCarte = L.map('map', {zoomControle: false}).setView([46.15197, -1.15385], 17); // (Centre, Niveau de zoom)


  // Création du controleur de Couches en position haut-gauche
  lControl = L.control.layers(null, null, {position: 'topleft'}).addTo(maCarte); // (BaseLayer, Overlay, Options)
  // ALTERNATIVE
  // lControl = L.control.layers().addTo(maCarte);
  // lControl.setPosition('topleft'); // Mise en position 'Haut-Gauche' (Défaut = 'Haut-Droit')

  // Création du controleur de Zoom en position haut-droite
  zoomControl = L.control.zoom({position: 'topright'}).addTo(maCarte);
  
  // Création d'une Echelle en position bas-gauche
  echelleControl = L.control.scale({position: 'bottomleft'}).addTo(maCarte);


  // Ajouter un titre à la carte
  titre = L.control();
  
  titre.onAdd = function (maCarte) {
    divTitre = L.DomUtil.create('div', 'titre');
    divTitre.innerHTML = "<h4>Mon Titre</h4>";
    return divTitre;
  };
  
  titre.addTo(maCarte);
  
  
  // Ajout de couche (raster et vecteur)
  // Ajout d'un fond de plan à la carte. (Nombreux choix sur : http://leaflet-extras.github.io/leaflet-providers/preview/)
  fondTopo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    maxZoom: 17
  }).addTo(maCarte);
  // Ajout d'une couche de base au controleur
  lControl.addBaseLayer(fondTopo, "Carte Topo");

  // Ajout d'une couche vectorielle à la carte (issue d'un geojson)
  $.getJSON('data/vecteur.geojson', {},
    function(donnees) {
      vVecteurGeoJ = L.geoJSON(donnees);
      vVecteurGeoJ.addTo(maCarte);
      // Ajout d'une couche sélectionnable au controleur
      lControl.addOverlay(vVecteurGeoJ, "Couche Vectorielle");
    });

  // Ajout d'une couche vectorielle à la carte (issue d'une base de données PostGis) (Attention création de requête PHP)
  $.getJSON('data/vecteur.php', {},
    function(donnees) {
      vVecteurBd = L.geoJSON(donnees);
      vVecteurBd.addTo(maCarte);
      // Ajout d'une couche sélectionnable au controleur
      lControl.addOverlay(vVecteurBd, "Couche Vectorielle");
    });



  // Personnalisation des couches vectorielle
  // Ajout d'une couche vectorielle polygone avec un style personnaliser
  $.getJSON('data/polygone.geojson', {},
    function(donnees) {
      vPolygone = L.geoJSON(donnees, {
        style: function(polygone) {
          return {
            color: "#A9D1F5" // couleur du contour
            , fillColor: "#FFF" // couleur de remplissage
            , weight: 0 // épaisseur du contour
            , opacity: 1 // opacité du contour
            , fillOpacity: 1 // opacité du remplissage
            , dashArray: '10, 15' // type de contour (tiret, point, etc...)
          };
        }
      });
      vPolygone.addTo(maCarte);
      lControl.addOverlay(vPolygone, "Couche Polygone");
    });

  // Ajout d'une couche vectorielle ligne avec un style personnaliser
  $.getJSON('data/ligne.geojson', {},
    function(donnees) {
      vLigne = L.geoJSON(donnees, {
        style: function() {
          return {
            color: "#F00", // couleur du trait
            weight: 2, // épaisseur du trait
            opacity: 0.7, // opacité du trait
            dashArray: '15,8' // type de trait (ligne, tiret, point, etc...)
          };
        }
      });
      vLigne.addTo(maCarte);
      // Ajout d'une couche sélectionnable au controleur
      lControl.addOverlay(vLigne, "Couche Ligne");
    });

  // Ajout d'une couche vectorielle point avec un style personnaliser
  $.getJSON('data/point.geojson', {},
    function(donnees) {
      vPoint = L.geoJSON(donnees, {
        pointToLayer: function(latlng) {
          return L.circleMarker(latlng, {
            radius: 8, // rayon
            color: "#000", // couleur du contour
            fillColor: "#FFF", // couleur de remplissage
            weight: 3, // épaisseur du contour
            opacity: 1, // opacité du contour
            fillOpacity: 0.8 // opacité du remplissage
          });
        }
      });
      vPoint.addTo(maCarte);
      // Ajout d'une couche sélectionnable au controleur
      lControl.addOverlay(vPoint, "Couche Point");
    });

  // Ajout d'une couche vectorielle point avec un icone personnaliser
  $.getJSON('data/point.geojson', {},
    function(donnees) {
      vPoint = L.geoJSON(donnees, {
        pointToLayer: function(pt, latlng) {
          return L.marker(latlng, {
            icon: new L.Icon({
              iconUrl: './img/icon.png', // chemin vers l'icone (Nombreux choix sur : https://www.flaticon.com/)
              iconSize: [28, 28], // taille de l'image [Largeur, Hauteur]
              iconAnchor: [14, 28] // point d'ancrage de l'image [Largeur, Hauteur]
            })
          });
        }
      });
      vPoint.addTo(maCarte);
      // Ajout d'une couche sélectionnable au controleur
      lControl.addOverlay(vPoint, "Couche Point");
    });



  // Ajout d'affichage des attributs en infobulle
  // Ajout d'une couche vectorielle avec affichages des informations attributaires au clique
  $.getJSON('data/vecteur.geojson', {},
    function(donnees) {
      vVecteur = L.geoJSON(donnees)
      onEachFeature: function(attribut, couche) {
        couche.on({
          click: function(entite) {
            contenu = "<b>Attribut : </b>" + couche.properties.ATTRIBUT + "<br>";
            popup = L.popup({
              closeOnClick: false
            }).setLatLng(entite.latlng).setContent(contenu).openOn(maCarte);
          }
        });
      }
      vVecteur.addTo(maCarte);
      lControl.addOverlay(vVecteur, "Couche Vectorielle");
    });

  // Ajout d'une couche vectorielle avec affichages des informations attributaires au survol
  $.getJSON('data/vecteur.geojson', {},
    function(donnees) {
      vVecteur = L.geoJSON(donnees)
      onEachFeature: function(attribut, couche) {
        contenu = "<b>Attribut : </b>" + couche.properties.ATTRIBUT + "<br>";
        couche.bindTooltip(contenu, {
          permanent: false,
          sticky: false,
          opacity: 1,
          direction: "top"
        });
        // sticky : la popup suit ou pas le curseur de la souris
        // direction  : endroit d'ouverture par rapport au survol ("top", "bottom", "left", "right", "center")
      }
      vVecteur.addTo(maCarte);
      lControl.addOverlay(vVecteur, "Couche Vectorielle");
    });

  
  
  // Ajout d'affichage des attributs en étiquettes (Attention ajout de CSS en plus)
  // Ajout d'une couche vectorielle avec affichages des informations attributaires au survol
  $.getJSON('data/vecteur.geojson', {},
    function(donnees) {
      vVecteur = L.geoJSON(donnees)
      onEachFeature: function(attribut, couche) {
        contenu = "<b>Attribut : </b>" + couche.properties.ATTRIBUT + "<br>";
        couche.bindTooltip(contenu, {
          permanent: true,
          sticky: false,
          permanent: true,
          opacity: 1,
          direction: "top",
          classeName: "etiquette"
        });
        // sticky : la popup suit ou pas le curseur de la souris
        // direction  : endroit d'ouverture par rapport au survol ("top", "bottom", "left", "right", "center")    }
      }
      vVecteur.addTo(maCarte);
      lControl.addOverlay(vVecteur, "Couche Vectorielle");
    });
});
