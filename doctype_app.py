"""Contain interactive doccumentation to help one get started using the API
"""
import os

from flasgger import Swagger

from app import create_app

app = create_app()
swagger = Swagger(app)


# Users
@app.route('/api/v1/auth/signup/', methods=["POST"])
def signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
    """

@app.route('/api/v1/auth/login', methods=["POST"])
def login():
    """ endpoint for logging in users.
    ---
    parameters:
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
    """

@app.route('/api/v1/users', methods=["POST"])
def users_signup():
    """ endpoint for registering users.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
    """

@app.route("/api/v1/users", methods=["GET"])
def get_all_users():
    """endpoint for  getting all users.
    No parameters required
    """

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_one_user():
    """endpoint for  getting a particular user.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/id', methods=["PUT"])
def update_user():
    """ endpoint for updating an existing user.
    ---
    parameters:
      - name: username
        required: true
        in: formData
        type: string
      - name: email
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
      - name: confirm_password
        in: formData
        type: string
        required: true
      - name: id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/<int:user_id>', methods=["DELETE"])
def delete_user():
    """ endpoint for deleting an existing user.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """


# Diaries
@app.route('/api/v1/diaries', methods=["POST"])
def create_diary():
    """ endpoint for creating a diary.
    ---
    parameters:
      - name: diary_no
        required: true
        in: formData
        type: integer
      - name: to-do
        in: formData
        type: string
        required: true
    """

@app.route("/api/v1/diaries", methods=["GET"])
def get_all_diaries():
    """endpoint for getting all diaries.
    No parameters required
    """

@app.route("/api/v1/diaries/<int:diary_id>", methods=["GET"])
def get_one_diary():
    """endpoint for  getting a particular diary.
    ---
    parameters:
      - name: diary_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/diaries/<int:diary_id>', methods=["PUT"])
def modify_diary():
    """ endpoint for modifying an existing diary.
    ---
    parameters:
      - name: diary_no
        required: true
        in: formData
        type: integer
      - name: to-do
        in: formData
        type: string
        required: true
      - name: diary_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/diaries/<int:diary_id>', methods=["DELETE"])
def delete_diary():
    """ endpoint for deleting an existing diary.
    ---
    parameters:
      - name: diary_id
        in: path
        type: integer
        required: true
    """


# Entries
@app.route('/api/v1/entries', methods=["POST"])
def create_entries():
    """ endpoint for creating an entry option.
    ---
    parameters:
      - name: entry_option
        required: true
        in: formData
        type: string
      - name: to-do
        in: formData
        type: string
        required: true
    """

@app.route("/api/v1/entries", methods=["GET"])
def get_all_entries():
    """endpoint for  getting all entries options.
    No parameters required
    """

@app.route("/api/v1/entries/<int:entry_id>", methods=["GET"])
def get_one_entry_option():
    """endpoint for getting a particular entry option.
    ---
    parameters:
      - name: entry_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/entries/<int:entry_id>', methods=["PUT"])
def modify_entries():
    """ endpoint for modify an existing entry option.
    ---
    parameters:
      - name: entry_option
        required: true
        in: formData
        type: string
      - name: to-do
        in: formData
        type: string
        required: true
      - name: entry_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/diaries/<int:entry_id>', methods=["DELETE"])
def delete_entry():
    """ endpoint for deleting an existing entry option.
    ---
    parameters:
      - name: entry_id
        in: path
        type: integer
        required: true
    """




@app.route('/')
def hello_world():
    "test that flask app is running"
    return "welcome to myDiary"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run('', port=port)