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
    return jsonify(seances)

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
        return jsonify(seance_dict)
    else:
        return jsonify({'message': 'Séance non trouvée'})

# Route pour créer une nouvelle séance
@app.route('/seances', methods=['POST'])
def create_seance():
    date = request.json['date']
    heure = request.json['heure']
    film = request.json['film']
    salle = request.json['salle']
    cursor = db.cursor()
    cursor.execute("INSERT INTO seances (date_seance, heure_seance, film, salle) VALUES (%s, %s, %s, %s)", (date, heure, film, salle))
    db.commit()
    return jsonify({'message': 'Séance créée'})

# Route pour mettre à jour une séance existante
@app.route('/seances/<int:id>', methods=['PUT'])
def update_seance(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM seances WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        date = request.json['date']
        heure = request.json['heure']
        film = request.json['film']
        salle = request.json['salle']
        cursor.execute("UPDATE seances SET date_seance = %s, heure_seance = %s, film = %s, salle = %s WHERE id = %s", (date, heure, film, salle, id))
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
    app.run(debug=True, port=5002)