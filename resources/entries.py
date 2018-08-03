"""Contains all endpoints to manipulate entry information
"""
import datetime

from flask import request, jsonify, Blueprint, make_response
from flask_restful import Resource, Api, reqparse
import jwt
import psycopg2
# pylint: disable=W0612

import models
import config
from .auth import user_required, user_id_required, user_admin_required
from setup import db

class EntryList(Resource):
    """Contains GET and POST methods"""


    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'user_id',
            required=True,
            type=int,
            help='kindly provide a valid id',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'entry',
            required=True,
            help='kindly provide a valid entry)',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'date',
            required=True,
            location=['form', 'json'])

        super().__init__()

    @user_id_required
    def post(self, user_id): 
        """Adds a new entry"""
        kwargs = self.reqparse.parse_args()
        user_id = str(user_id)

        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries WHERE user_id=%s and date=%s and entry=%s")
                         
        entry = db_cursor.fetchone()
        result = models.Entry.create_entry(entry=entry,
                                         user_id=user_id,
                                         date=kwargs.get("date"),)
        return result

    def get(self):
        """Gets all entries"""
        return models.Entry.get_all_entries()


class Entry(Resource):
    """Contains GET, PUT and DELETE methods for manipulating a single entry"""


    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'user_id',
            required=True,
            type=int,
            help='kindly provide a valid id',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'entry',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a valid entry)',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'date',
            required=True,
            location=['form', 'json'])

        super().__init__()
    

    def get(self, entry_id):
        """Get a particular entry"""
        return models.Entry.get_entry(entry_id)


    @user_id_required
    def post(self, entry_id, user_id):
        """start a particular entry"""
        user_id = user_id

        result = models.Entry.start_entry(entry_id=entry_id, user_id=user_id)
        if result == {"message" : "entry successful"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

    @user_id_required
    def put(self, entry_id, user_id):
        """Update a particular entry"""
        kwargs = self.reqparse.parse_args()

        user_id = user_id
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries WHERE entry_id=%s", (entry_id,))
        entry = db_cursor.fetchall()

        if entry == []:
            return make_response(jsonify({"message" : "entry does not exist"}), 404)

        result = models.Entry.update_entry(entry_id=entry_id,
                                         entry=entry,
                                         user_id=user_id,
                                         date=kwargs.get("date"))
        return result

    @user_required
    def delete(self, entry_id):
        """Delete a particular entry"""
        result = models.Entry.delete_entry(entry_id)
        return result


entries_api = Blueprint('resources.entries', __name__)
api = Api(entries_api)
api.add_resource(EntryList, '/entries', endpoint='entries')
api.add_resource(Entry, '/entries/<int:entry_id>', endpoint='entry')

