<?php
// Utilisation de la méthode PDO (Traitement par PHP)
// Pour WampServeur, Nécéssite l'activation de l'extention php_pdo_pgsql

// Tentative de connexion
    try {
        // accès postgis
        // $database = new PDO("pgsql:host=localhost;dbname=NomTable;port=5432", "Identitfiant", "MotDePasse") ;
        $database = new PDO("pgsql:host=localhost;dbname=leaflet;port=5432", "postgres", "postgres") ;
    } // Fin du try

    // Si la connexion ne fonctionne pas ...
    catch(PDOException $exeption) {
        // Message
            echo 'La connexion a échoué :-( : ' . $exeption->getMessage() ;
            exit;

    } // Fin du catch
?>
