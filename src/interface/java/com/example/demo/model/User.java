package com.example.demo.model;

public class User{
    private String ID;
    private String username;
    private String password;
    private String password2;
    private String email;
    private String first_name;
    private String last_name;
    private String token;

    public User(String id,String token){
        this.username = id;
        this.token = token;
    }

}