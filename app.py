"""Creates app instance, registers Blueprints and runs the Flask application
"""
import os
import datetime

from flask import Flask

from resources.entries import entries_api 
from resources.users import users_api
from models import tables_creation


def create_app(configuration):
    """Create flask app"""
    app = Flask(__name__)
    app.config.from_object(configuration)
    app.url_map.strict_slashes = False

    app.register_blueprint(users_api, url_prefix='/api/v1')
    app.register_blueprint(entries_api, url_prefix='/api/v1')

    return app

app = create_app('config.TestingConfig')
tables_creation()

@app.route('/')
def hello_world():
    "test that flask app is running"
    
    return "welcome to MyDIARY"

if __name__ == '__main__':
    app.run()
    # port = int(os.environ.get('PORT', 5000))
    # app.run('', port=port)
