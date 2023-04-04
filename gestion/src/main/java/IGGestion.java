import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.ArrayList;
import javax.swing.*;
/*
 * Created by JFormDesigner on Tue Apr 04 18:54:16 CEST 2023
 */



/**
 * @author grand
 */
public class IGGestion extends JFrame {
    public IGGestion() {
        initComponents();
    }

    private void initComponents() {
        // JFormDesigner - Component initialization - DO NOT MODIFY  //GEN-BEGIN:initComponents  @formatter:off
        // Generated using JFormDesigner Evaluation license - Alexandre Royer
        panel1 = new JPanel();
        label2 = new JLabel();
        panel3 = new JPanel();
        button1 = new JButton();
        panel4 = new JPanel();
        comboBox1 = new JComboBox();
        nomsalle = new JTextField();
        date = new JTextField();
        heure = new JTextField();
        panel5 = new JPanel();

        //======== this ========
        setMinimumSize(new Dimension(700, 600));
        setVisible(true);
        var contentPane = getContentPane();
        contentPane.setLayout(new GridLayout());

        //======== panel1 ========
        {
            panel1.setBorder ( new javax . swing. border .CompoundBorder ( new javax . swing. border .TitledBorder ( new javax . swing. border
            .EmptyBorder ( 0, 0 ,0 , 0) ,  "JF\u006frm\u0044es\u0069gn\u0065r \u0045va\u006cua\u0074io\u006e" , javax. swing .border . TitledBorder. CENTER ,javax
            . swing. border .TitledBorder . BOTTOM, new java. awt .Font ( "D\u0069al\u006fg", java .awt . Font. BOLD ,
            12 ) ,java . awt. Color .red ) ,panel1. getBorder () ) ); panel1. addPropertyChangeListener( new java. beans
            .PropertyChangeListener ( ){ @Override public void propertyChange (java . beans. PropertyChangeEvent e) { if( "\u0062or\u0064er" .equals ( e.
            getPropertyName () ) )throw new RuntimeException( ) ;} } );
            panel1.setLayout(new BorderLayout());

            //---- label2 ----
            label2.setText("Nietflix Seances");
            label2.setHorizontalAlignment(SwingConstants.CENTER);
            panel1.add(label2, BorderLayout.NORTH);

            //======== panel3 ========
            {
                panel3.setLayout(new BorderLayout());

                //---- button1 ----
                button1.setText("Ajout seance");
                panel3.add(button1, BorderLayout.NORTH);

                //======== panel4 ========
                {
                    panel4.setLayout(new GridLayout(4, 1));
                    panel4.add(comboBox1);
                    panel4.add(nomsalle);
                    panel4.add(date);
                    panel4.add(heure);
                }
                panel3.add(panel4, BorderLayout.CENTER);
            }
            panel1.add(panel3, BorderLayout.WEST);

            //======== panel5 ========
            {
                panel5.setLayout(new GridLayout(1, 1));
            }
            panel1.add(panel5, BorderLayout.CENTER);
        }

        APIManager am = new APIManager();
        ArrayList<String> ls = am.getLsFilm();

        for(String s : ls)
            comboBox1.addItem(s);

        date.setText("Date format 20231225");
        heure.setText("Heure format hhmmss");
        nomsalle.setText("Nom de la salle (chiffre)");

        button1.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if(!date.getText().isBlank() && !heure.getText().isBlank() && !nomsalle.getText().isBlank()){

                    String tmp = comboBox1.getSelectedItem().toString();
                    String[] tab = tmp.split("-");
                    am.ajoutBDDSeance(date.getText(),heure.getText(),tab[1],nomsalle.getText());
                    try {
                        loadSeances();
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    } catch (InterruptedException ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });


        try {
            loadSeances();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        contentPane.add(panel1);
        pack();
        setLocationRelativeTo(getOwner());
        // JFormDesigner - End of component initialization  //GEN-END:initComponents  @formatter:on
    }


    public void loadSeances() throws IOException, InterruptedException {
        APIManager am = new APIManager();
        ArrayList<String> ls = am.getAllSeances();
        GridLayout layout;
        panel5.removeAll();
        if(ls.size() > 0){
            layout = (GridLayout) panel5.getLayout();
            layout.setColumns(1);
            layout.setRows(ls.size());
            for(String s : ls){
                String[] tmp = s.split(",");
                JPanel jp = new JPanel(new FlowLayout());
                JLabel jl = new JLabel(tmp[1] + "," + tmp[0]+","+tmp[2]+","+tmp[4] + "," + tmp[3]);
                JButton delete = new JButton("Supprimer la séance");

                delete.addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        Container parent = delete.getParent();
                        int index = parent.getComponentZOrder(delete);
                        Component component = parent.getComponent(index - 1);
                        if (component instanceof JLabel) {
                            JLabel label = (JLabel) component;
                            String tmp = label.getText();
                            String[] tmp2 = tmp.split(",");
                            tmp = tmp2[4];
                            tmp2 = tmp.split(":");
                            tmp = tmp2[1];

                            am.supprimerBDDSeance(Integer.parseInt(tmp.trim()));
                            try {
                                loadSeances();
                            } catch (IOException ex) {
                                ex.printStackTrace();
                            } catch (InterruptedException ex) {
                                ex.printStackTrace();
                            }
                        }
                    }});


                jp.add(jl);
                jp.add(delete);

                panel5.add(jp);
                panel5.revalidate();
                panel5.repaint();
            }
        }


    }






    // JFormDesigner - Variables declaration - DO NOT MODIFY  //GEN-BEGIN:variables  @formatter:off
    // Generated using JFormDesigner Evaluation license - Alexandre Royer
    private JPanel panel1;
    private JLabel label2;
    private JPanel panel3;
    private JButton button1;
    private JPanel panel4;
    private JComboBox comboBox1;
    private JTextField nomsalle;
    private JTextField date;
    private JTextField heure;
    private JPanel panel5;
    // JFormDesigner - End of variables declaration  //GEN-END:variables  @formatter:on
}
