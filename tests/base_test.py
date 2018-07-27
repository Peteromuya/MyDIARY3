"""Authenticate a user and admin registration and login tests.
"""
# pylint: disable=W0612
import unittest
import json
from werkzeug.security import generate_password_hash

import sys # fix import errors
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app
import models


class BaseTests(unittest.TestCase):
    """Authenticate a user and an admin and make the tokens available. Create a diary and entries"""


    def setUp(self):
        self.application = app.create_app('config.TestingConfig')
        self.user_reg = json.dumps({
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
            '/api/v1/auth/userregister', data=user_reg,
            content_type='application/json')
       
        admin_result = self.app.post(
            '/api/v1/auth/login', data=self.admin_log,
            content_type='application/json')
        
        admin_response = json.loads(admin_result.get_data(as_text=True))
        admin_token = admin_response["token"]
        self.admin_header = {"Content-Type" : "application/json", "x-access-token" : admin_token}

    
        
        user_result = self.app.post(
            '/api/v1/auth/login', data=self.user_log,
            content_type='application/json')

        user_response = json.loads(user_result.get_data(as_text=True))
        user_token = user_response["token"]
        self.user_header = {"Content-Type" : "application/json", "x-access-token" : user_token}

       
    
    def tearDown(self):
        with self.application.app_context():

            models.all_users = {}
            models.user_count = 1

            models.all_diaries = {}
            models.diary_count = 1

            models.all_entries = {}
            models.entry_count = 1