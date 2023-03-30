<style>
  body{
    background-color: #333;
  }

  div{
    background-color: white;
    padding: 5px;
    text-align: center;
  }

  #modification{
    text-align: end;
    float: top;
    position: relative;
    margin-bottom: 10px;

  }

  #titre{
    text-align: start;
  }
  
  button{
    border-radius: 5px;
    border-color: transparent;
    padding: 10px;
  }

  #ajout:hover{
    background-color: lightskyblue;
  }
  #suppression:hover{
    background-color: lightcoral;
  }


td{
  padding: 2px;
  border-top: 1px solid black;
}
</style>
<?php

// URL de l'API GraphQL
$url = 'http://localhost:5002/graphql';

// Requête GraphQL pour récupérer la liste des films
$query ='{films {
  id
  titre
  duree
  Realisateur
  synopsis
}}';

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

?>


<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>IMDB</title>
</head>
<body>

<div class="ui container">
    <h1>Liste des films</h1>
    <table class="ui celled table">
        <thead>
            <tr>
                <th>Titre</th>
                <th>Réalisateur</th>
                <th>Durée</th>
                <th>Synopsis</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($films as $film) { ?>
                <tr>
                    <td><?php echo $film['titre']; ?></td>
                    <td><?php echo $film['Realisateur']; ?></td>
                    <td><?php echo $film['duree'] . ' min'; ?></td>
                    <td><?php echo $film['synopsis']; ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>
</div>

<div style="margin-top: 20px; float:inline-end">
        
        <button id="ajout" onclick="">Ajouter un film</button>

        <button id="suppression" onclick="">supprimer un film</button>
        
      </div>

</body>

</html>

