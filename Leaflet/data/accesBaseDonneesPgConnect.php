<?php
// Utilisation de la méthode pg_connect (Traitement par Postgres)
// Pour WampServeur, Nécéssite l'activation de l'extention php_pgsql
<?php
  $dbConnect = pg_connect("host=localhost port=5432 dbname=equipement_cen user=postgres password=postgres")
  OR die("Connection échoué");
?>

?>
