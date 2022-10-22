package com.example.demo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class HelloController {
    @FXML
    private Label welcomeText;

    @FXML
    protected void onPredictedButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
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

 */
    public void initialize(URL url, ResourceBundle rb) {
        WebView webView = new WebView();
        WebEngine engine = webView.getEngine();
        String u = getClass().getResource("H:\\stay hungry stay foolish\\Y4\\Fianl Year Project\\demo\\dr_age.html").toExternalForm();
        engine.load(u);
        webView.getZoom();
        webView.getEngine();
        var scene = new Scene(webView, 640, 480);

    }

}