package com.example.demo;

import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;
import com.example.demo.API.UserAPI;
import com.example.demo.HelloApplication;


import java.io.IOException;

public class LoginController {

    private Stage stage;
    @FXML
    private TextField email;

    @FXML
    private TextField password;

    @FXML
    private Button submit;

    public void setController(Stage stage) {
        this.stage = stage;
    }

    @FXML
    void loginClicked(MouseEvent event) throws IOException {
        UserAPI user = new UserAPI();
        //user.login("http://127.0.0.1:8000/api/v1/login/","test@gmail.com","test123456");
        user.login("http://127.0.0.1:8000/api/v1/login/",email.getText(),password.getText());

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("dashboard.fxml"));
        //Scene scene = new Scene(fxmlLoader.load(), 800, 600);
        Scene scene = new Scene(fxmlLoader.load());
        stage.setScene(scene);



    }
}
