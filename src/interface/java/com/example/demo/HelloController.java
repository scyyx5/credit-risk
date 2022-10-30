package com.example.demo;

import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Pane;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;




public class HelloController {

    public final String URL = "http://127.0.0.1:8000/";
    //use API to send HTML
    @FXML
    private final String dr_ageAPI = "download_dr_age/";


    @FXML
    private WebView dr_ageWebView;
    WebEngine dr_agewebEngine = null;
    @FXML
    private CheckBox dr_age_predicted;
    @FXML
    private Button dr_age_pre;


    @FXML
    void dr_ageTab(Event event) {

    }

    @FXML
    private int count_dr_age_predicted_click;
    @FXML
    void ondr_agePredictedButtonClick(ActionEvent event) throws MalformedURLException {
        if (dr_age_predicted.isSelected()) {
            File f = new File("res\\dr_age_predicted.html");
            dr_agewebEngine.load(f.toURI().toURL().toString());
        } else {
            File f = new File("res\\dr_age.html");
            dr_agewebEngine.load(f.toURI().toURL().toString());
        }
    }

    @FXML
    void ondr_agePredictedButton(ActionEvent event) {

    }


    @FXML
    void dr_calTab(Event event) {

    }


    @FXML
    private WebView dr_calWebView;
    WebEngine dr_calwebEngine = null;
    @FXML
    private CheckBox dr_cal_predicted;
    @FXML
    private Button dr_cal_pre;
    @FXML
    private int count_dr_cal_predicted_click;
    @FXML
    void ondr_calPredictedButtonClick(ActionEvent event) throws MalformedURLException {
        if(dr_cal_predicted.isSelected()){
            File f = new File("res\\dr_cal_predicted.html");
            dr_calwebEngine.load(f.toURI().toURL().toString());
        }else{
            File f = new File("res\\dr_cal.html");
            dr_calwebEngine.load(f.toURI().toURL().toString());
        }
        //System.out.println("click");
    }

    @FXML
    void ondr_calPredictedButton(ActionEvent event ) throws MalformedURLException {
        //if(dr_cal_pre.setOnAction())
        dr_cal_pre.addEventHandler(MouseEvent.MOUSE_CLICKED, new EventHandler<MouseEvent>() {
                    public void handle(MouseEvent event) {
                        count_dr_cal_predicted_click ++;
                        if(count_dr_cal_predicted_click % 2 != 0){    //click even number
                            File f = new File("res\\dr_cal_predicted.html");
                            try {
                                System.out.println(count_dr_cal_predicted_click);
                                dr_calwebEngine.load(f.toURI().toURL().toString());
                            } catch (MalformedURLException e) {
                                throw new RuntimeException(e);
                            }
                        }else{
                            File f = new File("res\\dr_cal.html");
                            try {
                                System.out.println(count_dr_cal_predicted_click);
                                dr_calwebEngine.load(f.toURI().toURL().toString());
                            } catch (MalformedURLException e) {
                                throw new RuntimeException(e);
                            }
                        }
                    }
                });
    }

    private void savehtml(String file){
        Process proc;
        try {
            proc = Runtime.getRuntime().exec("python " + file);
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            proc.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


    @FXML
    private WebView lexisDiagramWebView;
    WebEngine lexisDiagramEngine = null;


    //switch from different panes according to the left label
    @FXML
    private Label DefaultRateLabel;

    @FXML
    private Pane DefaultRatePane;

    @FXML
    private Label LexisDiagramLabel;

    @FXML
    private Pane LexisDiagramPane;

    public void clickDefaultRate(MouseEvent mouseEvent) {
        DefaultRatePane.setVisible(true);
        LexisDiagramPane.setVisible(false);
    }

    public void clickLexisDiagram(MouseEvent mouseEvent) {
        DefaultRatePane.setVisible(false);
        LexisDiagramPane.setVisible(true);
    }
    public void initialize() throws MalformedURLException {
        //count_dr_age_predicted_click = 0;
        //count_dr_cal_predicted_click = 0;
        DefaultRatePane.setVisible(true);
        LexisDiagramPane.setVisible(false);

        savehtml("src\\visualization\\dr_age.py");
        savehtml("src\\visualization\\dr_cal.py");
        savehtml("src\\visualization\\lexis.py");
        dr_agewebEngine = dr_ageWebView.getEngine();
        File dr_age_file = new File("res\\dr_age.html");
        dr_agewebEngine.load(dr_age_file.toURI().toURL().toString());
        //System.out.println("miao");

        dr_calwebEngine = dr_calWebView.getEngine();
        File dr_cal_file = new File("res\\dr_cal.html");
        dr_calwebEngine.load(dr_cal_file.toURI().toURL().toString());

        lexisDiagramEngine = lexisDiagramWebView.getEngine();
        File lexis_diagram = new File("res\\lexis_diagram.html");
        lexisDiagramEngine.load(lexis_diagram.toURI().toURL().toString());


        //System.out.println("miaomiao");
    }


}




