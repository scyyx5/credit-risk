module com.example.demo {
    requires javafx.controls;
    requires javafx.fxml;
    requires jython.slim;
    requires javafx.web;
    requires javafx.graphics;
    requires java.net.http;

    opens com.example.demo to javafx.fxml;
    exports com.example.demo;
}