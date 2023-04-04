import json

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuration de la connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seancecinemadb"
)


# définition de la route pour la page d'accueil
@app.route('/')
def home():
    return '<h3>bonjour:</h3> ' \
           '<p style="background-color: #EEE">Voici l\'API REST des séances de cinéma</p>' \
           '<h3> Informations:</h3>' \
           '<div style="background-color: #EEE"><p>-\'/seances\' #Visualiser les séances existante </p>' \
           '<p>-\'/seances/id\' #Visualiser la séance qui possède cette id</p>' \
           '<p>-</p>' \
           '<p>-</p>' \
           '<p>-</p></div>'


# Route pour récupérer toutes les séances
@app.route('/seances', methods=['GET'])
def get_all_seances():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM seances")
    result = cursor.fetchall()
    seances = []
    for seance in result:
        seance_dict = {
            'id': seance[0],
            'date': seance[1],
            'heure': seance[2],
            'film': seance[3],
            'salle': seance[4]
        }

        seances.append(seance_dict)
    return json.dumps(seances, indent=4, sort_keys=True, default=str)


# Route pour récupérer une séance par ID
@app.route('/seances/<int:id>', methods=['GET'])
def get_seance_by_id(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM seances WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        seance_dict = {
            'id': result[0],
            'date': result[1],
            'heure': result[2],
            'film': result[3],
            'salle': result[4]
        }

        return json.dumps(seance_dict, indent=4, sort_keys=True, default=str)
    else:
        return jsonify({'message': 'Séance non trouvée'})


# Route pour créer une nouvelle séance
@app.route('/seances', methods=['POST'])
def create_seance():
    dates = request.json['date']
    heures = request.json['heure']
    film = request.json['film']
    salle = request.json['salle']
    cursor = db.cursor()
    cursor.execute("INSERT INTO seances (date, heure, film_id, nomsalle) VALUES (%s, %s, %s, %s)",
                   (dates, heures, film, salle))
    db.commit()
    return jsonify({'message': 'Séance créée'})


# Route pour mettre à jour une séance existante
@app.route('/seances/<int:id>', methods=['PUT'])
def update_seance(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM seances WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        dates = request.json['date']
        heures = request.json['heure']
        film = request.json['film']
        salle = request.json['salle']
        cursor.execute("UPDATE seances SET date = %s, heure = %s, film_id = %s, nomsalle = %s WHERE id = %s",
                       (dates, heures, film, salle, id))
        db.commit()
        return jsonify({'message': 'Séance mise à jour'})
    else:
        return jsonify({'message': 'Séance non trouvée'})


# Route pour supprimer une séance
@app.route('/seances/<int:id>', methods=['DELETE'])
def delete_seance(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM seances WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM seances WHERE id = %s", (id,))
        db.commit()
        return jsonify({'message': 'Séance supprimée'})
    else:
        return jsonify({'message': 'Séance non supprimer'})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
