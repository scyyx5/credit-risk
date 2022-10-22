package com.example.demo;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import org.python.util.PythonInterpreter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;




public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        //HelloController h = new HelloController();
        Process proc;

        try {
            proc = Runtime.getRuntime().exec("python src\\visualization\\dr_age.py");
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

        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 320, 240);
        stage.setTitle("Hello!");
        stage.setScene(scene);
        stage.show();

    }

    public static void main(String[] args) {
        launch();
    }
}



/**
 public class HelloApplication extends Application {
@Override
public void start(Stage stage) throws IOException {
PythonInterpreter interpreter = new PythonInterpreter();

interpreter.exec("import sys");
interpreter.exec("sys.path.append('C:\\Users\\86151\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages')");
interpreter.exec("sys.path.append('C:\\Users\\86151\\AppData\\Local\\Programs\\Python\\Python39\\site-packages')");
interpreter.exec("sys.path.append('C:\\Users\\86151\\AppData\\Local\\Programs\\Python\\Python39\\lib')");

//interpreter.execfile("src\\main\\java\\com\\example\\demo\\hello.py");
//interpreter.execfile("src\\visualization\\dr_age.py");


FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
Scene scene = new Scene(fxmlLoader.load(), 320, 240);
stage.setTitle("Hello!");
stage.setScene(scene);
stage.show();
}

public static void main(String[] args) {
launch();
}
}
 */