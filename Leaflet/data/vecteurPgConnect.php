<?php
  // Utilisation de la méthode pg_connect (Traitement par Postgres)
  include("accesBaseDonneesPgConnect.php"); // Inclusion de la connexion à la base de données

  // Ecriture de la requete pour avoir un résultat formater en JSON
  $sql = "SELECT row_to_json(fc) FROM (
    SELECT 'FeatureCollection' AS type, array_to_json(array_agg(f)) AS features
    FROM (
      SELECT 'Feature' AS type, row_to_json((SELECT attribut FROM (
        SELECT nom_attribut AS nom) AS attribut)) AS properties, ST_AsGeoJSON(ST_Transform(geom, 4326), 6)::json AS geometry
      FROM data.vecteur
    ) AS f
  ) AS fc";

  // Execution de la requête
  $resultat_json = pg_exec($database, $sql) OR die(pgErrorMessage());
  while($ligne = pg_fetch_row($resultat_json))
  {
    echo trim ($ligne[0]);
  }
  
  // Fermeture de la connection avec la Base de Données
  pg_close($database);
?>
