"""Contains all endpoints to manipulate diary information
"""
import datetime
from flask import jsonify, Blueprint, make_response
from flask_restful import Resource, Api, reqparse, inputs
import os

from werkzeug.security import check_password_hash
import jwt

import config
import models 
from .auth import admin_required

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
            'to-do',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a valid to-do)',
            location=['form', 'json'])
        super().__init__()

    def post(self):
        """Adds a new entry"""
        kwargs = self.reqparse.parse_args()

        token = request.headers['x-access-token']
        data = jwt.decode(token, config.Config.SECRET_KEY)
        user_id = data['id']

        result = models.Entry.create_entry(user_id=user_id, **kwargs)
        return result

   
    def get(self): 
        """Gets all entries."""
        return make_response(jsonify(models.all_entries), 200)



class Entries(Resource):
    """Contains GET, PUT and DELETE methods for manipulating a single entry option"""


   
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'user_id',
            required=True,
            type=int,
            help='kindly provide a valid id',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'to-do',
            required=True,
            type=inputs.regex(r"(.*\S.*)"),
            help='kindly provide a valid to-do)',
            location=['form', 'json'])
        super().__init__()

    def get(self, entry_id):
        """Get a particular entry_option"""
        try:
            diary = models.all_entries[entry_id]
            return make_response(jsonify(diary), 200)
        except KeyError:
            return make_response(jsonify({"message" : "entry option does not exist"}), 404)

    def put(self, user_id):
        """Update a particular entry"""

        token = request.headers['x-access-token']
        data = jwt.decode(token, config.Config.SECRET_KEY)
        driver_id = data['id']

        kwargs = self.reqparse.parse_args()
        token = request.headers['x-access-token']
        data = jwt.decode(token, config.Config.SECRET_KEY)
        entry_id = data['id']
        
        result = models.Entry.update_entries(user_id, **kwargs)
        if result != {"message" : "entry does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

    def delete(self, entry_id):
        """Delete a particular entry option"""

        token = request.headers['x-access-token']
        data = jwt.decode(token, config.Config.SECRET_KEY)
        user_id = data['id']

        result = models.Entry.delete_entry(entry_id)
        if result != {"message" : "entry option does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

entries_api = Blueprint('resources.entries', __name__)
api = Api(entries_api) # create the API
api.add_resource(EntryList, '/entries', endpoint='entries')
api.add_resource(Entries, '/entries/<int:entry_id>', endpoint='entry')



