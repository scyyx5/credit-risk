from urllib import response
from django.test import TestCase
from django.test import Client
# Create your tests here.
import unittest
import json
import jsonschema
from jsonschema import validate
import psycopg2
import requests

# Create your tests here.
userSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "user_fname": {"type": "string"},
        "user_lname": {"type": "string"},
        "user_email": {"type": "string"},
        "user_password": {"type": "string"},
    },
}



c = Client()

def validateMultipleJSON(jsonData, currentSchema):
    try:
        for json1 in jsonData:
            validate(instance=json1, schema=currentSchema)
    except jsonschema.exceptions.ValidationError as err: 
        return False 
    return True

def validateJSON(jsonData, currentSchema):
    try:
        validate(instance=jsonData, schema=currentSchema)
    except jsonschema.exceptions.ValidationError as err: 
        return False 
    return True

class userTestCase(TestCase):
    def test_add_user(self):
        response = requests.post("http://127.0.0.1:8000/api/v1/Register/", json= {
            "username": "AutoTestAccount",
            "password": "AutoMaticTesting123!",
            "password2": "AutoMaticTesting123!",
            "email": "auto_test@gmail.com",
            "first_name": "auto_test",
            "last_name": "auto_test"}, verify=False)
        print(response.json())
        self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 201)


    def test_log_in(self):
        response = requests.post("http://127.0.0.1:8000/api/v1/login/", json= {
        "email": "test@gmail.com",
        "password": "test123456"},
        verify=False)

        print(response.json())
        self.assertEqual(validateJSON(response.json(), userSchema), True)
        
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):

        response = c.post("/api/v1/login/", json= {"user_fname": "UNIQUETEXT23244411111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "user_lname": "UNIQUETEXT232444", "user_email": "UNIQUETEXT232444@gmail.com"})
        self.assertNotEqual(response.status_code, 200)

    def test_invalid_user2(self):

        response = c.post("/api/v1/login/", json= {    "username": "testaccount","password": "test1234"})
        self.assertNotEqual(response.status_code, 200)
        
        
