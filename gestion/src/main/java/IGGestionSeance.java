import java.awt.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.swing.*;
import net.miginfocom.swing.*;
/*
 * Created by JFormDesigner on Tue Apr 04 02:03:38 CEST 2023
 */



/**
 * @author grand
 */
public class IGGestionSeance extends JPanel {

    public IGGestionSeance() {
        initComponents();
    }

    public void Ajout(String date, String heure, String titre, String salle){
        APIGestion apiGestion = new APIGestion();
        try {
            apiGestion.createSeance(date,heure,titre,salle);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        loadSeances();

    }

    private void loadSeances() {
        panel4 = new JPanel();
        panel4.setLayout(new GridLayout(0, 1));
        APIGestion apiGestion = new APIGestion();
        ArrayList<String> seances;
        try {
            seances = apiGestion.getAllSeances();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        if(seances.size() != 0){

        }


    }

    public void Retirer(int id){
        APIGestion apiGestion = new APIGestion();
        try {
            apiGestion.deleteSeance(8);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        loadSeances();
    }


    private void initComponents() {
        // JFormDesigner - Component initialization - DO NOT MODIFY  //GEN-BEGIN:initComponents  @formatter:off
        // Generated using JFormDesigner Evaluation license - Alexandre Royer
        panel1 = new JPanel();
        label2 = new JLabel();
        panel2 = new JPanel();
        button3 = new JButton();
        button4 = new JButton();
        panel4 = new JPanel();

        //======== panel1 ========
        {
            panel1.setBorder (new javax. swing. border. CompoundBorder( new javax .swing .border .TitledBorder (new javax. swing. border. EmptyBorder(
            0, 0, 0, 0) , "JF\u006frmDes\u0069gner \u0045valua\u0074ion", javax. swing. border. TitledBorder. CENTER, javax. swing. border. TitledBorder
            . BOTTOM, new java .awt .Font ("D\u0069alog" ,java .awt .Font .BOLD ,12 ), java. awt. Color.
            red) ,panel1. getBorder( )) ); panel1. addPropertyChangeListener (new java. beans. PropertyChangeListener( ){ @Override public void propertyChange (java .
            beans .PropertyChangeEvent e) {if ("\u0062order" .equals (e .getPropertyName () )) throw new RuntimeException( ); }} );
            panel1.setLayout(new BorderLayout());

            //---- label2 ----
            label2.setText("Nietflix Seances");
            label2.setHorizontalAlignment(SwingConstants.CENTER);
            panel1.add(label2, BorderLayout.NORTH);

            //======== panel2 ========
            {
                panel2.setLayout(new GridLayout(2, 1));

                //---- button3 ----
                button3.setText("Ajouter Seance");
                panel2.add(button3);

                //---- button4 ----
                button4.setText("Supprimer Seance");
                panel2.add(button4);
            }
            panel1.add(panel2, BorderLayout.WEST);

            //======== panel4 ========
            {
                panel4.setLayout(new GridLayout(0, 1));
            }
            panel1.add(panel4, BorderLayout.CENTER);
        }
        // JFormDesigner - End of component initialization  //GEN-END:initComponents  @formatter:on
    }

    // JFormDesigner - Variables declaration - DO NOT MODIFY  //GEN-BEGIN:variables  @formatter:off
    // Generated using JFormDesigner Evaluation license - Alexandre Royer
    private JPanel panel1;
    private JLabel label2;
    private JPanel panel2;
    private JButton button3;
    private JButton button4;
    private JPanel panel4;
    // JFormDesigner - End of variables declaration  //GEN-END:variables  @formatter:on
}
