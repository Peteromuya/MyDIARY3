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
       
        all_users[user_count] = {"id": user_count, "username" : username,
                                 "email" : email, "password" : password, "admin" : admin}
       
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return new_user

    @staticmethod
    def update_user(user_id, username, email, password, admin=False, **kwargs):
        """Updates user information"""
        if user_id in all_users.keys():
            all_users[user_id] = {"id" : user_id, "username" : username, "email" : email,
                                  "password" : password, "admin" : admin}
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return all_users[user_id]
        return {"message" : "user does not exist"}

    @staticmethod
    def delete_user(user_id):
        """Deletes a user"""
      
        db_connection = psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return {"message" : "user successfully deleted"}
        return {"message" : "user does not exist"}

    @staticmethod
    def all_users():
        """get all users"""
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
        return make_response(jsonify({"message" : "user does not exists"}), 404)

    @staticmethod
    def get_all_users():
        """Gets all users"""
        db_connection = psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
    
        return make_response(jsonify({"All users" : all_users}), 200)

class Entry(object):


    @staticmethod
    def create_entry(user_id, todo):
        """Creates a new date and appends this information to the all_entries dictionary"""
       
        all_entries[entry_count] = {"id": entry_count, "to-do": todo}
        new_entry = all_entries[entry_count]
        entry_count += 1
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return new_entry

    @staticmethod
    def update_entry(email, date, todo, **kwargs):
        """Updates entries' dates information"""
        if email in all_entries.keys():
            all_entries[email] = {"user_idl": user_id, "date" : date, "to-do" : todo}
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return all_entries[user_id]
        return {"message" : "id with that entry does not exist"}

    @staticmethod
    def delete_entry(user_id):
        """Deletes an entry"""
       
        db_connection=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s)", (username, email, password, admin))
        db_connection.commit()
        db_connection.close()
        return {"message" : "entry with that id is successfully deleted"}
        return {"message" : "entry with that id does not exist"}


