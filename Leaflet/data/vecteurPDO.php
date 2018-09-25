<?php
    // Utilisation de la méthode PDO (Traitement par PHP)

    header('Content-Type: application/json'); // Pour dire au navigateur que c'est du JSON

    include("accesBaseDonneesPDO.php"); // Inclusion de la connexion à la base de données

    // Initialisation pour configurer la données au format JSON
    $geojson = array(
        'type' => 'FeatureCollection',
        'features' => array()
    );

    // Lancement & Exécution de la requête
    $requete_vecteur = $db->prepare("SELECT id, nom_attribut AS nom, st_asgeojson(st_transform(geom, 4326), 6) as geojson FROM data.vecteur");
    $requete_vecteur->execute();
    $resultat = $requete_vecteur->fetchAll(PDO::FETCH_ASSOC);

    // Suite de l'initialisation pour configurer la données au format JSON
    foreach ($resultat as $r) {
        $attribut = array(
            'type' => 'Feature',
            'geometry' => json_decode($r['geojson'], true),
            'properties' => array(
                'nom' => $r['nom']
            )
        );
        array_push($geojson['features'], $attribut);
    }

    $resultat_json = json_encode($geojson); // Encodage du résultat au format JSON
    echo $resultat_json // Retourner $resultat_json
?>
