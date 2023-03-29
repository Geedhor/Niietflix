<?php

// URL de l'API GraphQL
$url = 'http://localhost:5001/graphql';

// Requête GraphQL pour récupérer la liste des films
$query =
'{
  films {
    id
    titre
    duree
    Realisateur
    synopsis
  }
}';

// Envoi de la requête GraphQL à l'API
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(['query' => $query]));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// Traitement de la réponse JSON de l'API
$data = json_decode($response, true);
$films = $data['data']['films'];

// Affichage des films
foreach ($films as $film) {
    echo '<h2>' . $film['titre'] . '</h2>';
    echo '<p><strong>Réalisateur :</strong> ' . $film['Realisateur'] . '</p>';
    echo '<p><strong>Durée :</strong> ' . $film['duree'] . ' minutes</p>';
    echo '<p><strong>Synopsis :</strong> ' . $film['synopsis'] . '</p>';
    echo '<hr>';
}
