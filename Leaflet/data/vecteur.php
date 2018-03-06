<?php
    header('Content-Type: application/json'); // Pour dire au navigateur que c'est du JSON

    include("accesBaseDonnees.php");

    $geojson = array(
        'type' => 'FeatureCollection',
        'feature' => array()
    );

    $requete_vecteur = $db->prepare("SELECT id, nom_attribut AS nom, st_asgeojson(st_transform(geom, 4326), 6) as geojson FROM data.vecteur");
    $requete_vecteur->execute();
    $resultat = $requete_vecteur->fetchAll(PDO::FETCH_ASSOC);

    foreach ($resultat as $r) {
        $attribut = array(
            'type' => 'Feature',
            'geometry' => json_decode($r['geojson'], true),
            'properties' => array(
                'nom' => $r['nom']
            )
        );
        array_push($geojson['attribut'], $attribut);
    }

    $resultat_json = json_encode($geojson);
    echo $resultat_json
?>
