import graphene
import mysql.connector
from flask import Flask, jsonify, request

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='filmdb'
)

# Création du curseur MySQL
cursor = conn.cursor(dictionary=True)

# Définition de la requête SQL pour récupérer tous les films
query_all_films = "SELECT * FROM film;"

# Définition de la requête SQL pour récupérer les films par titre
query_films_by_title = "SELECT * FROM film WHERE titre LIKE %(titre)s;"

# Définition de la requête SQL pour récupérer les films par realisateur
query_films_by_realisateur = "SELECT * FROM film WHERE realisateur LIKE %(realisateur)s;"

# Définition de la requête SQL pour supprimer les films par le titre
query_dell_film = "DELETE FROM film WHERE titre LIKE %(titre)s;"

# Définition de la requête SQL pour ajouter un film
query_add_film = "INSERT INTO film (titre, Realisateur, duree, synopsis) VALUES (%(titre)s, %(Realisateur)s, %(duree)s, %(synopsis)s)"

# Définition de l'objet Film pour le schéma GraphQL
class Film(graphene.ObjectType):
    id = graphene.ID()
    titre = graphene.String()
    duree = graphene.Int()
    Realisateur = graphene.Field(graphene.String)
    synopsis = graphene.String()


# Définition de la requête pour récupérer tous les films
class Query(graphene.ObjectType):
    films = graphene.List(Film, titre=graphene.String(), realisateur=graphene.String())

    def resolve_films(self, info, titre=None, realisateur=None):
        if titre:
            cursor.execute(query_films_by_title, {'titre': f'%{titre}%'})
        elif realisateur:
            cursor.execute(query_films_by_realisateur, {'realisateur': f'%{realisateur}%'})
        else:
            cursor.execute(query_all_films)
        return [Film(**film) for film in cursor.fetchall()]

# Création du schéma GraphQL
schema = graphene.Schema(query=Query)

# Création de l'application Flask
app = Flask(__name__)


# définition de la route pour la page d'accueil
@app.route('/')
def home():
    return '<h3>bonjour:</h3> ' \
           '<p style="background-color: #EEE">Voici l\'API GraphQL connecter à la base de données des films \'filmdb\'.' \
           '<h3>Informations:</h3>' \
           '<div style="background-color: #EEE"><p>-/graphql + schéma json # visualiser les film</p>'\
           '<p>-/add + # ajouter un film </p>' \
           '<p>-/del?titre=... # supprimer film </p></div>' \
           '<h3>Exemple schéma json:</h3>' \
           '<p style="background-color: #EEE">{' \
              ' films {<br>'\
              ' id<br>' \
              ' titre<br>' \
              ' duree<br>'\
              ' Realisateur<br>'\
              ' synopsis<br>'\
              ' }'\
            '}</p>' \
           '<h3>Récupération de données:</h3>' \
           '<div style="background-color: #EEE"><h5>PHP:</h5>' \
           '<p style="padding: 10px">// URL de l\'API GraphQL<br>' \
           '$url = \'http://localhost:5002/graphql\';<br><br>' \
           '// Requête GraphQL pour récupérer la liste des films<br>' \
           '$query =\'{films {<br>'\
              ' id<br>' \
              ' titre<br>' \
              ' duree<br>'\
              ' Realisateur<br>'\
              ' synopsis<br>'\
              ' }<br>' \
           '}<br><br>'\
           '// Envoi de la requête GraphQL à l\'API <br>' \
           '$ch = curl_init(); <br>' \
           'curl_setopt($ch, CURLOPT_URL, $url); <br>' \
           'curl_setopt($ch, CURLOPT_POST, true); <br>' \
           'curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([\'query\' => $query])); <br>' \
           'curl_setopt($ch, CURLOPT_HTTPHEADER, [\'Content-Type: application/json\']); <br>' \
           'curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); <br>' \
           '$response = curl_exec($ch); <br>' \
           'curl_close($ch); <br><br>' \
           '// Traitement de la réponse JSON de l\'API <br>' \
           '$data = json_decode($response, true); <br>' \
           '$films = $data[\'data\'][\'films\'];</p></div> <br>'

# Définition de la vue manuelle pour traiter les requêtes GraphQL
@app.route('/graphql', methods=['POST'])
def graphql():
    # Récupération de la requête GraphQL depuis le corps de la requête HTTP
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables')

    # Exécution de la requête GraphQL en utilisant le schéma défini
    result = schema.execute(query, variable_values=variables)

    # Retour de la réponse HTTP avec le résultat de la requête GraphQL
    response_data = {'data': result.data}
    if result.errors:
        response_data['errors'] = [str(error) for error in result.errors]
    return jsonify(response_data)

# traitement de la requête GraphQL pour ajouter un film
@app.route('/graphql/add', methods=['POST'])
def add():
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables')

# traitement de la requête GraphQL pour supprimer un film
@app.route('/graphql/del', methods=['DELETE'])
def delete():
    data = request.get_json()
    query = data.get('query')
    variables = data.get('variables')


# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5002)
