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


def create_table():
    conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS entries (user_id INTEGER, entry TEXT, date TEXT)")
    conn.commit()
    conn.close()

def insert(username,email,password):
    db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO users VALUES('%s','%s','%s')", (username,email,password))
    # db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s)", (username,email, password))
    db_connection.commit()
    db_connection.close()

create_table()

    
class User(object):


    @staticmethod
    def create_user(username, email, password, admin=False, **kwargs):
        """Creates a new user and appends his information to the all_users dictionary"""
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        users = db_cursor.fetchall()
        all_users[user_count] = {"id": user_count, "username" : username,
                                 "email" : email, "password" : password, "admin" : admin}
        new_user = all_users[user_count]
        user_count += 1
        return new_user

    @staticmethod
    def update_user(user_id, username, email, password, admin=False, **kwargs):
        """Updates user information"""
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        users = db_cursor.fetchall()
        if user_id in all_users.keys():
            all_users[user_id] = {"id" : user_id, "username" : username, "email" : email,
                                  "password" : password, "admin" : admin}
            return all_users[user_id]
        return {"message" : "user does not exist"}

    @staticmethod
    def delete_user(user_id):
        """Deletes a user"""
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        users = db_cursor.fetchall()
        try:
            del all_users[user_id]
            return {"message" : "user successfully deleted"}
        except KeyError:
            return {"message" : "user does not exist"}

    @staticmethod
    def all_users():
        """get all users"""
        db_connection = psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        users = db_cursor.fetchall()
        db_connection.close()
        if user_id in all_users.keys():
            all_users[user_id] = {"id" : user_id, "username" : username, "email" : email,
                                  "password" : password, "admin" : admin}

        users = []
        return {"all_users" : users}

    @staticmethod
    def get_user(user_id):
        """Gets a particular user"""
        db_connection = psycopg2.connect(db)
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        user = db_cursor.fetchall()
        if user != []:
            user=user[0]

        return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_all_users():
        """Gets all users"""
        db_connection = psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        user = db_cursor.fetchall()
        all_users = []
        for user in users:
    
            return make_response(jsonify({"All users" : all_users}), 200)


class Entry(object):

    @staticmethod
    def create_entry(user_id, entry):
        """Creates a new entry"""
        db_connection = psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        
        all_entries[entry_count] = {"id": entry_count, "entry": entry}
        new_entry = all_entries[entry_count]
        entry_count += 1

        db_connection.commit()
        db_connection.close()
        
        return new_entry
        return make_response(jsonify({"message" : "ride has been successfully created"}), 201)


    @staticmethod
    def update_entry(email, date, entry, **kwargs):
        """Updates entries information"""
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        entries = db_cursor.fetchall()
        if email in all_entries.keys():
           all_entries[email] = {"user_id": user_id, "date" : date, "entry" : entry}
        
        return all_entries[user_id]
        return {"message" : "entry does not exist"}

    @staticmethod
    def delete_entry(user_id):
        """Deletes an entry"""
       
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        entries = db_cursor.fetchall()
        try:
            del all_entries[user_id]
            return {"message" : "entry is successfully deleted"}
        except KeyError:
            return {"message" : "entry does not exist"}
        
        return {"message" : "entry is successfully deleted"}
        return {"message" : "entry does not exist"}


