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

query_films_by_realisateur = "SELECT * FROM film WHERE realisateur LIKE %(realisateur)s;"

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

# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5001)
