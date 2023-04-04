<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Page d'accueil des séances de cinéma</title>
    <style>
        body {
            background-color: #F5F5F5;
            font-family: Arial, sans-serif;
        }

        h1 {
            text-align: center;
            margin-top: 30px;
            color: #333;
        }

        #seances {
            margin: 30px auto;
            max-width: 800px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .seance {
            background-color: #FFF;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 5px #CCC;
            margin-bottom: 20px;
            width: 30%;
        }

        .seance h2 {
            font-size: 20px;
            margin-bottom: 10px;
            color: #333;
        }

        .seance p {
            font-size: 16px;
            color: #666;
            margin-bottom: 5px;
        }

        .seance .button {
            background-color: #008CBA;
            color: #FFF;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
        }

        .seance .button:hover {
            background-color: #005f73;
        }
    </style>
</head>
<body>
    <h1>Bienvenue sur notre site de réservation de séances de cinéma</h1>

    <div id="seances">
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $.ajax({
            url: "ws://localhost:5006",
            type: "GET",
            success: function (data) {
                for (var i = 0; i < data.length; i++) {
                    var seance = data[i];
                    var seanceHtml = '<div class="seance">';
                    seanceHtml += '<h2>' + seance.film + '</h2>';
                    seanceHtml += '<p>Date : ' + seance.date + '</p>';
                    seanceHtml += '<p>Heure : ' + seance.heure + '</p>';
                    seanceHtml += '<p>Salle : ' + seance.salle + '</p>';
                    seanceHtml += '<button class="button" onclick="reserver(' + seance.id + ')">Réserver</button>';
                    seanceHtml += '</div>';
                    $("#seances").append(seanceHtml);
                }
            }
        });

        function reserver(idSeance) {
            alert("Réservation effectuée pour la séance " + idSeance);
        }
    </script>
</body>
</html>
