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

all_users = {}
user_count = 1

all_entries = {}
entry_count = 1

    
"""Handles data storage for Users and Diaries
"""
class User(object):


    @staticmethod
    def create_user(username, email, password, admin=False, **kwargs):
        """Creates a new user and appends his information to the all_users dictionary"""
       
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        global all_users
        global user_count
        all_users[user_count] = {"id": user_count, "username" : username,
                                 "email" : email, "password" : password, "admin" : admin}
        new_user = all_users[user_count]
        user_count += 1
        return new_user

    @staticmethod
    def update_user(user_id, username, email, password, admin=False, **kwargs):
        """Updates user information"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        if user_id in all_users.keys():
            all_users[user_id] = {"id" : user_id, "username" : username, "email" : email,
                                  "password" : password, "admin" : admin}
            return all_users[user_id]
        return {"message" : "user does not exist"}

    @staticmethod
    def delete_user(user_id):
        """Deletes a user"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        try:
            del all_users[user_id]
            return {"message" : "user successfully deleted"}
        except KeyError:
            return {"message" : "user does not exist"}

    @staticmethod
    def get_user(user_id):
        """Gets a particular user"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        if user != []:
            user=user[0]
        return make_response(jsonify({"message" : "user does not exists"}), 404)


    @staticmethod
    def get_all_users():
        """Gets all users"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        all_users = []
        for user in users:
            return make_response(jsonify({"all users" : all_users}), 200)


class Entry(object):

    @staticmethod
    def create_entry(user_id, todo):
        """Creates a new date and appends this information to the all_entries dictionary"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        global all_entries
        global entry_count
        all_entries[entry_count] = {"id": entry_count, "to-do": todo}
        new_entry = all_entries[entry_count]
        entry_count += 1
        return new_entry

    @staticmethod
    def update_entry(user_id, todo):
        """Updates entries' dates information"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        if email in all_entries.keys():
            all_entries[email] = {"user_idl": user_id, "date" : date, "to-do" : todo}
            return all_entries[user_id]
        return {"message" : "id with that entry does not exist"}

    @staticmethod
    def delete_entry(user_id):
        """Deletes an entry"""
        conn=psycopg2.connect("dbname='Database9' user='postgres' password='0725401106' host='localhost' port='5435'")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, admin TEXT)")
        conn.commit()
        try:
            del all_entries[user_id]
            return {"message" : "entry with that id is successfully deleted"}
        except KeyError:
            return {"message" : "entry with that id does not exist"}


    @staticmethod
    def get_one_entry(user_id):
        if entry != []:
            entry=entry[0]

            return make_response(jsonify({"message" : "entry does not exists"}), 404)

    @staticmethod
    def get_all_entries(user_id, todo):
        all_entries = []
        for entry in entries:
            return make_response(jsonify({"All entries" : all_entries}), 200)
