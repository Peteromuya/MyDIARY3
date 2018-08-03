"""Contains all endpoints to manipulate user information
"""
import datetime

import psycopg2
from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse, inputs
from werkzeug.security import check_password_hash
import jwt

from .auth import user_required, user_id_required, user_admin_required

import models
import config

from setup import db


class User_Register(Resource):
    "Contains a POST method to register a new user"


    def __init__(self):
        "Validates input from the form as well as json input"
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='kindly provide a valid username',
            # match anything but newline + something not whitespace + anything but newline
            type=inputs.regex(r"(.*\S.*)"),
            location=['form', 'json'])
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            trim=True,
            help='kindly provide a valid confirmation password',
            location=['form', 'json'])

        super().__init__()

    def post(self):
        """Register a new user"""
        kwargs = self.reqparse.parse_args()

        if kwargs.get('password') == kwargs.get('confirm_password'):
            if len(kwargs.get('password')) >= 8:
                db_cursor = db.con()
                db_cursor.execute("SELECT * FROM users WHERE email=%s", (kwargs.get('email'),))
                user = db_cursor.fetchall()

                if user != []:
                    return make_response(jsonify({"message" : "user with that email already exists"}), 400)

                result = models.User(username=kwargs.get('username'),
                                     email=kwargs.get('email'),
                                     password=kwargs.get('password'),
                                     admin=False)
                return make_response(jsonify({"message" : "user has been successfully created"}), 201)
            return make_response(jsonify({
                "message" : "password should be atleast 8 characters"}), 400)
        return make_response(jsonify({
            "message" : "password and cofirm password should be identical"}), 400)


class Login(Resource):
    "Contains a POST method to login a user"


    def __init__(self):
        "Validates input from the form as well as json input"
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        super().__init__()

    def post(self):
        """login a user"""
        try:
            kwargs = self.reqparse.parse_args()
            db_cursor = db.con()
            db_cursor.execute("SELECT * FROM users WHERE email=%s", (kwargs.get("email"),))
            user = db_cursor.fetchone()
            if check_password_hash(user[3], kwargs.get("password")) == True:
                # print(user[0])
                # print(user[4])
                # print(config.Config.SECRET_KEY)
                # print(datetime.datetime.utcnow() + datetime.timedelta(weeks=5))

                token = jwt.encode({
                    'id' : user[0],
                    'admin' : user[4],
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(weeks=5)},
                                    config.Config.SECRET_KEY)
                print(token)

                return make_response(jsonify({
                    "message" : "successfully logged in",
                    "token" : token.decode('UTF-8')}), 200)
            return make_response(jsonify({"message" : "invalid email or password"}), 400)
        except:
            return make_response(jsonify({"message" : "invalid email address or password"}), 400)

class UserList(Resource):
    "Contains a POST method to register a new user and a GET method to get all users"


    def __init__(self):
        "Validates input from the form as well as json input"
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='kindly provide a valid username',
            # match anything but newline + something not whitespace + anything but newline
            type=inputs.regex(r"(.*\S.*)"),
            location=['form', 'json'])
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            trim=True,
            help='kindly provide a valid confirmation password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'admin',
            required=False,
            type=inputs.boolean,
            default=False,
            location=['form', 'json'])
        super().__init__()

    # @admin_required
    def post(self):
        """Register a new user or admin"""
        kwargs = self.reqparse.parse_args()

        if kwargs.get('password') == kwargs.get('confirm_password'):
            if len(kwargs.get('password')) >= 8:
                db_cursor = db.con()
                db_cursor.execute("SELECT * FROM users WHERE email=%s", (kwargs.get('email'),))
                user = db_cursor.fetchall()

                if user != []:
                    return make_response(jsonify({"message" : "user with that email already exists"}), 400)

                result = models.User(username=kwargs.get('username'),
                                                 email=kwargs.get('email'),
                                                 password=kwargs.get('password'),
                                                 admin=kwargs.get('admin'))
                return make_response(jsonify({"message" : "user has been successfully created"}), 201)
            return make_response(jsonify({
                "message" : "password should be atleast 8 characters"}), 400)
        return make_response(jsonify({
            "message" : "password and cofirm password should be identical"}), 400)

    # @admin_required
    def get(self):
        """Get all users"""
        result = models.User.get_all_users()
        return result

class User(Resource):
    """Contains GET PUT and DELETE methods for interacting with a particular user"""


    def __init__(self):
        "Validates input from the form as well as json input"
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='kindly provide a valid username',
            # match anything but newline + something not whitespace + anything but newline
            type=inputs.regex(r"(.*\S.*)"),
            location=['form', 'json'])
        self.reqparse.add_argument(
            'email',
            required=True,
            help='kindly provide a valid email address',
            location=['form', 'json'],
            type=inputs.regex(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        self.reqparse.add_argument(
            'password',
            required=True,
            trim=True,
            help='kindly provide a valid password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            trim=True,
            help='kindly provide a valid confirmation password',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'admin',
            required=True,
            default=False,
            location=['form', 'json'])
        super().__init__()

    # @admin_required
    def get(self, user_id):
        """Get a particular user"""
        result = models.User.get_user(user_id)
        return result

    # @admin_required
    def put(self, user_id):
        """Update a particular user"""
        kwargs = self.reqparse.parse_args()
        if kwargs.get('password') == kwargs.get('confirm_password'):
            if len(kwargs.get('password')) >= 8:
                db_cursor = db.con()
                db_cursor.execute("SELECT * FROM users WHERE email=%s", (kwargs.get('email'),))
                user = db_cursor.fetchall()

                if user != []:
                    return make_response(jsonify({"message" : "user with that email already exists"}), 400)

                db_cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
                by_id = db_cursor.fetchall()

                if by_id == []:
                    return make_response(jsonify({"message" : "user does not exist"}), 404)


                result = models.User.update_user(user_id=user_id,
                                                 username=kwargs.get('username'),
                                                 email=kwargs.get('email'),
                                                 password=kwargs.get('password'),
                                                 admin=kwargs.get('admin'))
                return result
            return make_response(jsonify({
                "message" : "password should be at least 8 characters"}), 400)
        return make_response(jsonify({
            "message" : "password and confirm password should be identical"}), 400)

    # @admin_required
    def delete(self, user_id):
        """Delete a particular user"""
        db_cursor = db.con()
        db_cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        user = db_cursor.fetchall()

        if user == []:
            return make_response(jsonify({"message" : "user does not exist"}), 404)
        return models.User.delete_user(user_id=user_id)


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(User_Register, '/auth/signup', endpoint='signup')
api.add_resource(Login, '/auth/login', endpoint='login')
api.add_resource(UserList, '/users', endpoint='users')
api.add_resource(User, '/users/<int:user_id>', endpoint='user')