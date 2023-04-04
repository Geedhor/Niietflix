import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;

public class APIGestion {
    
    private final String BASE_URL = "http://localhost:5001";
    
    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_2)
            .build();
    
    // méthode pour récupérer toutes les séances
    public ArrayList<String> getAllSeances() throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(BASE_URL + "/seances"))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
       return trierJSON(response.body());
    }
    
    // méthode pour récupérer une séance par ID
    public String getSeanceById(int id) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .GET()
                .uri(URI.create(BASE_URL + "/seances/" + id))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        return trierJSON(response.body()).get(0);
    }
    
    // méthode pour créer une nouvelle séance
    public void createSeance(String date, String heure, String film, String salle) throws IOException, InterruptedException {
        String requestBody = String.format("{\"date\": \"%s\", \"heure\": \"%s\", \"film\": \"%s\", \"salle\": \"%s\"}", date, heure, film, salle);
        
        HttpRequest request = HttpRequest.newBuilder()
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .uri(URI.create(BASE_URL + "/seances"))
                .header("Content-Type", "application/json")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println(response.body());
    }
    
    // méthode pour mettre à jour une séance existante
    public void updateSeance(int id, String date, String heure, String film, String salle) throws IOException, InterruptedException {
        String requestBody = String.format("{\"date\": \"%s\", \"heure\": \"%s\", \"film\": \"%s\", \"salle\": \"%s\"}", date, heure, film, salle);
        
        HttpRequest request = HttpRequest.newBuilder()
                .PUT(HttpRequest.BodyPublishers.ofString(requestBody))
                .uri(URI.create(BASE_URL + "/seances/" + id))
                .header("Content-Type", "application/json")
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println(response.body());
    }
    
    // méthode pour supprimer une séance
    public void deleteSeance(int id) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .DELETE()
                .uri(URI.create(BASE_URL + "/seances/" + id))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        
        System.out.println(response.body());
    }


    private ArrayList<String> trierJSON(String chaine){
        String s = chaine;
        ArrayList<String> rep = new ArrayList<>();
        int i = 0;
        char c;
        boolean printer = false;
        String tmp = "";
        while (i < s.length()){
            c = s.charAt(i);
            if(c == '{'){
                printer = true;
            }else if (c == '}') {
                printer = false;
                rep.add(tmp.trim());
                tmp = "";
            } else if (printer) {
                tmp += c;
            }
            i++;
        }
        return rep;
    }



}