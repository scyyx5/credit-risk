package com.example.demo;

import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;



public class HelloController {

    @FXML
    private Pane dr_agePane;

    @FXML
    private WebView dr_ageWebView;
    WebEngine dr_agewebEngine = null;

    @FXML
    void dr_ageTab(Event event) {

    }


    @FXML
    void ondr_agePredictedButtonClick(ActionEvent event) {

    }

    @FXML
    void dr_calTab(Event event) {

    }

    @FXML
    private Pane dr_calPane;

    @FXML
    private WebView dr_calWebView;
    WebEngine dr_calwebEngine = null;

    @FXML
    void ondr_calPredictedButtonClick(ActionEvent event) {


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

    public void initialize() throws MalformedURLException {
        savehtml("src\\visualization\\dr_age.py");
        savehtml("src\\visualization\\dr_cal.py");
        dr_agewebEngine = dr_ageWebView.getEngine();
        File dr_age_file = new File("res\\dr_age.html");
        dr_agewebEngine.load(dr_age_file.toURI().toURL().toString());
        System.out.println("miao");

        dr_calwebEngine = dr_calWebView.getEngine();
        File dr_cal_file = new File("res\\dr_cal.html");
        dr_calwebEngine.load(dr_cal_file.toURI().toURL().toString());
        System.out.println("miaomiao");
    }
}




/**
@FXML
private WebView webView;
WebEngine webEngine = null;

@FXML
private void onPredictedButtonClick(ActionEvent event) {
    System.out.println("miao");
    //webEngine.load("H:\\stay hungry stay foolish\\Y4\\Fianl Year Project\\demo\\dr_age.html");
}


public void initialize(URL url, ResourceBundle rb) {
    WebView webView = new WebView();
    WebEngine engine = webView.getEngine();
    String u = getClass().getResource("D:\\dr_age.html").toExternalForm();
    engine.load(u);
    webView.getZoom();
    webView.getEngine();
    var scene = new Scene(webView, 640, 480);

}

}*/