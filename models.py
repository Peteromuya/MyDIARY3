"""Handles data storage for Users and Entries
"""
# pylint: disable=E1101

import datetime

from flask import make_response, jsonify
from werkzeug.security import generate_password_hash
import psycopg2


import config
from os import getenv

db = config.TestingConfig.db


    # def create_table(username, email, password):
    #     """Creates a new user and ensures that the email is unique"""
    #     conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    #     cur=conn.cursor()
    #     conn.commit()
    #     conn.close()  

    # def insert(username,email,password):
    #     db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    #     db_cursor = db_connection.cursor()
    #     db_cursor.execute("INSERT INTO users VALUES('%s','%s','%s')", (username,email,password))
    #     db_connection.commit()
    #     db_connection.close()


    # create_table()
    # insert("kevin","k@gmail.com",secret12345")
                                    

    @staticmethod
    def update_user(user_id, username, email, password):
        """Updates user information"""
        db_connection = psycopg2.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM users")
        users = db_cursor.fetchall()
        for user in users:
            if user[1] == email:
                return make_response(jsonify({"message" : "user with that email already exists"}), 400)

        for user in users:
            if user[0] == user_id:
                db_cursor.execute("UPDATE users SET username=%s, email=%s, password=%, WHERE user_id=%s",
                                  (username, email, password, user_id))
                return make_response(jsonify({"message" : "user has been successfully updated"}), 200)

        return make_response(jsonify({"message" : "user does not exist"}), 404)


    @staticmethod
    def delete_user(user_id):
        """Deletes a user"""
        db_connection = psycopg2.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM users")
        users = db_cursor.fetchall()
        if users != []:
            for user in users:
                if user[0] == user_id:
                    db_cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
                    db_connection.commit()
                    db_connection.close()
                    return make_response(jsonify({"message" : "user has been successfully deleted"}), 200)
        
        return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_user(user_id):
        """Gets a particular user"""
        db_connection = psycopg2.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        user = db_cursor.fetchall()
        if user != []:
            user=user[0]
            info = {user[0] : {"email": user[1],
                                "username": user[2],}}
            return make_response(jsonify({"profile" : info}), 200)
        return make_response(jsonify({"message" : "user does not exists"}), 404)


    @staticmethod
    def get_all_users():
        """Gets all users"""
        db_connection = psycopg2.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM users")
        users = db_cursor.fetchall()
        all_users = []
        for user in users:
            info = {user[0] : {"email": user[1],
                                "username": user[2],}}
            all_users.append(info)
        return make_response(jsonify({"All users" : all_users}), 200)

  
  