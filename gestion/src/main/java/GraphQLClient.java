import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import org.json.JSONArray;
import org.json.JSONObject;

public class GraphQLClient {

    public JSONArray getListFilms(){

        // URL de l'API GraphQL
        String url = "http://localhost:5002/graphql";

        // Requête GraphQL pour récupérer la liste des films
        String query = "{films { id titre duree Realisateur synopsis }}";
        JSONArray filmsJson = null;
        try {
            // Création de la connexion HTTP
            HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoOutput(true);

            // Envoi de la requête GraphQL à l'API
            String requestBody = new JSONObject().put("query", query).toString();
            conn.getOutputStream().write(requestBody.getBytes());

            // Lecture de la réponse de l'API
            BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder responseBuilder = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                responseBuilder.append(line);
            }
            br.close();

            // Traitement de la réponse JSON de l'API
            JSONObject responseJson = new JSONObject(responseBuilder.toString());
            JSONObject dataJson = responseJson.getJSONObject("data");
            filmsJson = dataJson.getJSONArray("films");
            for (int i = 0; i < filmsJson.length(); i++) {
                JSONObject filmJson = filmsJson.getJSONObject(i);
                int id = filmJson.getInt("id");
                String titre = filmJson.getString("titre");
                int duree = filmJson.getInt("duree");
                String realisateur = filmJson.getString("Realisateur");
                String synopsis = filmJson.getString("synopsis");
                // Faites quelque chose avec les données des films récupérées
            }

            // Fermeture de la connexion HTTP
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return filmsJson;
    }
}