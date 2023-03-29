import asyncio
import json
import websockets
import mysql.connector
import requests


async def handle_reservation(websocket, path):
    # Connexion à la base de données
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sallecinemadb"
    )
    cursor = db.cursor()

    # Récupération de la liste des séances depuis l'API REST
    seances_response = requests.get("localhost/seances")
    seances = seances_response.json()

    # Envoi de la liste des séances au client
    await websocket.send(json.dumps(seances))

    # Attente de messages du client
    async for message in websocket:
        data = json.loads(message)

        # Vérification de la validité de la réservation
        seance_id = data.get("seance_id")
        nombre_places = data.get("nombre_places")
        cursor.execute("SELECT nombre_places_disponibles FROM seances WHERE id=%s", (seance_id,))
        result = cursor.fetchone()
        if not result or nombre_places > result[0]:
            await websocket.send(json.dumps({"error": "Réservation invalide"}))
            continue

        # Enregistrement de la réservation dans la base de données
        cursor.execute("UPDATE seances SET nombre_places_disponibles=nombre_places_disponibles-%s WHERE id=%s",
                       (nombre_places, seance_id))
        db.commit()
        cursor.execute("INSERT INTO reservations (seance_id, nombre_places) VALUES (%s, %s)",
                       (seance_id, nombre_places))
        db.commit()

        # Envoi de la confirmation de réservation au client
        await websocket.send(json.dumps({"success": "Réservation réussie"}))

    # Fermeture de la connexion à la base de données
    cursor.close()
    db.close()


start_server = websockets.serve(handle_reservation, "localhost", 5003)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()