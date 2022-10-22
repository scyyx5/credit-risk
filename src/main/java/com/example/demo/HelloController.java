package com.example.demo;

import javafx.event.ActionEvent;
import javafx.event.Event;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;


public class HelloController {

    @FXML
    private Pane dr_agePane;

    @FXML
    private Pane dr_calPane;



    @FXML
    void dr_ageTab(Event event) {

    }

    @FXML
    void dr_calTab(Event event) {

    }

    @FXML
    void ondr_agePredictedButtonClick(ActionEvent event) {

    }

    @FXML
    void ondr_calPredictedButtonClick(ActionEvent event) {

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