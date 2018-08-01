"""Contains all endpoints to manipulate diary information
"""
from flask import jsonify, Blueprint, make_response
from flask_restful import Resource, Api, reqparse, inputs


from werkzeug.security import check_password_hash

import jwt
import psycopg2
import config
import models 



from .auth import user_required, admin_required, user_id_required



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
            help='kindly provide a valid todo)',
            location=['form', 'json'])
        super().__init__()
        
    @user_id_required
    def post(self, user_id):
        """Adds a new entry"""
        kwargs = self.reqparse.parse_args()
        user_id = str(user_id)

        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM entries")
        entry = db_cursor.fetchone()

        if entry != None:
            return make_response(jsonify({"message" : "post another entry"}), 400)

        entry= kwargs.get("user_id") + kwargs.get("to-do")
        result = models.Entry.create_entry(entry=entry,
                                         user_id=user_id)
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
            help='kindly provide a valid entry)',
            location=['form', 'json'])
        super().__init__()

    def get(self, entry_id):
        """Get a particular entry_option"""
        try:
            diary = models.all_entries[entry_id]
            return make_response(jsonify(diary), 200)
        except KeyError:
            return make_response(jsonify({"message" : "entry option does not exist"}), 404)

         
    def post(self, entry_id):
        """start a particular entry"""
        token = request.headers['x-access-token']
        data = jwt.decode(token, config.Config.SECRET_KEY)
        user_id = data['id']

        result = models.Entry.start_entry(entry_id=entry_id, user_id=user_id)
        if result == {"message" : "entry is successful"}:
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
                                         user_id=user_id)
        return result
    def delete(self, entry_id):
        """Delete a particular entry option"""

        result = models.Entry.delete_entry(entry_id)
        if result != {"message" : "entry option does not exist"}:
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 404)

entries_api = Blueprint('resources.entries', __name__)
api = Api(entries_api) # create the API
api.add_resource(EntryList, '/entries', endpoint='entries')
api.add_resource(Entries, '/entries/<int:entry_id>', endpoint='entry')



