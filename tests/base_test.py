"""Authenticate a user, driver and an admin to be used during testing
Set up required items to be used during testing
"""
# pylint: disable=W0612
import unittest
import json
from werkzeug.security import generate_password_hash
import psycopg2

import sys # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
import models
from setup import db
import config


class BaseTests(unittest.TestCase):
    """Authenticate a user and an admin and make the tokens available. Create an entry"""


    def setUp(self):
        self.application = app.create_app('config.TestingConfig')
        with self.application.app_context():
            self.db = db
            self.db.drop()
            self.db.tables_creation()
            models.User(username="admin",
                        email="admin@gmail.com",
                        password="admin1234",
                        admin=True)

        user_reg = json.dumps({
            "username" : "user",
            "email" : "user@gmail.com",
            "password" : "12345678",
            "confirm_password" : "12345678"})

        self.user_log = json.dumps({
            "email" : "user@gmail.com",
            "password" : "12345678"})

        self.admin_log = json.dumps({
            "email" : "admin@gmail.com",
            "password" : "admin1234"})

        self.app = self.application.test_client()

        
        register_user = self.app.post(
            '/api/v1/auth/signup', data=user_reg,
            content_type='application/json')
    

        admin_result = self.app.post(
            '/api/v1/auth/login', data=self.admin_log,
            content_type='application/json')

        admin_response = json.loads(admin_result.get_data(as_text=True))
        admin_token = admin_response["token"]
        self.admin_header = {"Content-Type" : "application/json", "x-access-token" : admin_token}

       
        user_response = json.loads(user_result.get_data(as_text=True))
        user_token = user_response["token"]
        self.user_header = {"Content-Type" : "application/json", "x-access-token" : user_token}


        user_result = self.app.post(
            '/api/v1/auth/login', data=self.user_log,
            content_type='application/json')

        user_response = json.loads(user_result.get_data(as_text=True))
        user_token = user_response["token"]
        self.user_header = {"Content-Type" : "application/json", "x-access-token" : user_token}

        # entry = json.dumps({"departurepoint" : "Syokimau", "destination" : "Nairobi",
        #  "departuretime" : "16/04/2015 1400HRS", "numberplate" : "KBH 400", "maximum" : "2"})

       

        create_entry = self.app.post(
            '/api/v1/entries', data=ride, content_type='application/json',
            headers=self.user_header)



    def tearDown(self):
        with self.application.app_context():
            self.db.drop()
