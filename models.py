"""Handles data storage for Users and Entries
"""
# pylint: disable=E1101

import datetime

from flask import make_response, jsonify, current_app
from werkzeug.security import generate_password_hash

import config

import psycopg2
from setup import db



class User():
    """Contains user columns and methods to add, update and delete a user"""


    def __init__(self, username, email, password, admin):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        if admin == True:
            self.admin = '1'
        else:
            self.admin = '0'

        new_user = "INSERT INTO users (username, email, password, admin) VALUES " \
                    "('" + self.username + "', '" + self.email + "', '" + self.password + "', '" + self.admin + "')"
        db_cursor = db.con()
        db_cursor.execute(new_user)
        db.commit()
        

    @staticmethod
    def create_user(username, email, password, admin=False, **kwargs):
        """Creates a new user and appends his information to the all_users dictionary"""
        global all_users
        global user_count
        all_users[user_count] = {"id": user_count, "username" : username,
                                 "email" : email, "password" : password, "admin" : admin}
        new_user = all_users[user_count]
        user_count += 1
        return new_user




    @staticmethod
    def update_user(user_id, username, email, password, admin):
        """Updates user information"""
        try:
            db_cursor = db.con()
            db_cursor.execute("UPDATE users SET username=%s, email=%s, password=%s, admin=%s",
                                (username, email, password, admin, user_id))
            db.commit()
            return make_response(jsonify({"message" : "user has been successfully updated"}), 200)
        except:
            return make_response(jsonify({"message" : "user does not exist"}), 404)

    @staticmethod
    def delete_user(user_id):
        """Deletes a user"""
        try:
            db_cursor = db.con()
            db_cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id,))
            db.commit()
            return make_response(jsonify({"message" : "user has been successfully deleted"}), 200)
        except:
            return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_user(user_id):
        """Gets a particular user"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        user = db_cursor.fetchall()

        if user != []:
            user=user[0]
            info = {user[0] : {"email": user[1],
                                "username": user[2],
                                "admin": user[4]}}
            return make_response(jsonify({"profile" : info}), 200)
        return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_all_users():
        """Gets all users"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM users")
        users = db_cursor.fetchall()

        all_users = []
        for user in users:
            info = {user[0] : {"email": user[1],
                                "username": user[2],
                                "admin": user[4]}}
            all_users.append(info)
        return make_response(jsonify({"All users" : all_users}), 200)


class Entry():
    """Contains entry columns and methods to add, update and delete an entry"""


    def __init__(self, entry, user_id):
        self.entry = entry
        self.user_id = user_id
        


        new_entry = "INSERT INTO entries (entry, user_id) VALUES " \
                    "('" + self.entry + "', '" + self.user_id + "')"
        db_cursor = db.con()
        db_cursor.execute(new_entry)
        db.commit()

    @classmethod
    def create_entry(cls, entry, user_id):
        """Creates a new entry"""

        cls(entry, user_id, date)
        return make_response(jsonify({"message" : "entry has been successfully created"}), 201)

    @staticmethod
    def update_entry(entry_id, entry, user_id, date):
        """Updates entry information"""
        try:
            db_cursor = db.con()
            db_cursor.execute("UPDATE entries SET entry=%s, user_id=%s, date=%s WHERE entry_id=%s",
                                  (entry, user_id, date,entry_id))
            db.commit()
            return make_response(jsonify({"message" : "user has been successfully updated"}), 200)
        except:
            return make_response(jsonify({"message" : "user does not exist"}), 404)

    @staticmethod
    def delete_entry(entry_id):
        """Deletes an entry"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries")
        rides = db_cursor.fetchall()

        for entry in entries:
            if entry[0] == entry_id:
                db_cursor.execute("DELETE FROM entries WHERE entry_id=%s", (entry_id,))
                db.commit()

                return make_response(jsonify({"message" : "entry has been successfully deleted"}), 200)
        return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_entry(entry_id):
        """Gets a particular entry"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries WHERE entry_id=%s", (entry_id,))
        entry = db_cursor.fetchall()

        if entry != []:
            entry=entry[0]
            info = {entry[0] : {"entry": entry[1],
                                "user_id": entry[2],
                                "date": entry[3]}}
            return make_response(jsonify({"entry" : info}), 200)
        return make_response(jsonify({"message" : "entry does not exists"}), 404)

    @staticmethod
    def get_all_entries():
        """Gets all entries"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries")
        entries = db_cursor.fetchall()
        all_entries = []
        for entry in entries:
            info = {entry[0] : {"entry": entry[1],
                                "user_id": entry[2],
                                "date": entry[3]}}
            all_entries.append(info)
        return make_response(jsonify({"All entries" : all_entries}), 200)
