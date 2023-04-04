import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;

public class APIManager {

    APIGestion apig;
    GraphQLClient gc;

    public APIManager(){
        apig = new APIGestion();
        gc = new GraphQLClient();
    }


    public ArrayList<String> getLsFilm(){
        ArrayList<String> res = new ArrayList<>();
        JSONArray lf = gc.getListFilms();
        for(int i = 0; i < lf.length(); i++){
            JSONObject jso = lf.getJSONObject(i);

            res.add(jso.getString("titre") + "-"  +jso.getString("id"));

        }
        return res;
    }



    public void ajoutBDDSeance(String date,String heure,String film_id,String salle){
        try {
            apig.createSeance(date,heure,film_id,salle);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }



    public ArrayList<String> getAllSeances() throws IOException, InterruptedException {
        return apig.getAllSeances();
    }


    public void supprimerBDDSeance(int id){
        try {
            apig.deleteSeance(id);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


}