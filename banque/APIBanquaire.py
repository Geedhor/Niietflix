from flask import Flask, jsonify, request

app = Flask(__name__)

# définition des comptes bancaires
bank_accounts = [
    {"account_number": 345371, "balance": 2000},  #Thommas
    {"account_number": 368697, "balance": 2000},  #Alexandre
    {"account_number": 370068, "balance": 2000},  #Antoine
    {"account_number": 430077, "balance": 2000},  #Julien
    {"account_number": 484842, "balance": 2000},  #Theo
    {"account_number": 877411, "balance": 10000}, #Cinema1
    {"account_number": 706693, "balance": 10000}, #Cinema2
    {"account_number": 171644, "balance": 10000}  #Cinema3
]

# définition de la route pour la page d'accueil
@app.route('/')
def home():
    return '<h3>bonjour:</h3> ' \
           '<p style="background-color: #EEE">Voici l\'API banquaire.</p>' \
           '<h3> Informations:</h3>' \
           '<div style="background-color: #EEE"><p>-\'/comptes\' #Visualiser les comptes existant </p>' \
           '<p>-\'/transfer?sender_account_number=...&receiver_account_number = ...&amount = ...\' #Faire un virement</p></div>'

# définition de la route pour afficher les comptes bancaires
@app.route('/comptes', methods=['GET'])
def get_accounts():
    return jsonify(bank_accounts)

# définition de la route pour effectuer un transfert d'argent
@app.route('/transfer', methods=['POST'])
def transfer_money():
    # récupération des données de la transaction
    sender_account_number = int(request.json['sender_account_number'])
    receiver_account_number = int(request.json['receiver_account_number'])
    amount = int(request.json['amount'])

    # recherche des comptes bancaires correspondants aux numéros de compte
    sender_account = next((acc for acc in bank_accounts if acc["account_number"] == sender_account_number), None)
    receiver_account = next((acc for acc in bank_accounts if acc["account_number"] == receiver_account_number), None)

    # vérification de l'existence des comptes bancaires
    if sender_account is None:
        return jsonify({"error": "Compte bancaire émetteur non trouvé."}), 404
    elif receiver_account is None:
        return jsonify({"error": "Compte bancaire destinataire non trouvé."}), 404

    # vérification du solde du compte émetteur
    if sender_account["balance"] < amount:
        return jsonify({"error": "Solde insuffisant."}), 400

    # mise à jour des soldes des comptes bancaires
    sender_account["balance"] -= amount
    receiver_account["balance"] += amount

    # envoi de la réponse en format JSON
    return jsonify({"message": "Transfert effectué avec succès."}), 200

# exécution de l'application Flask
if __name__ == '__main__':
    app.run(debug=True, port=5004)