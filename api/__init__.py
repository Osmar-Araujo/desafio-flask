from flask import Flask, Blueprint
from api.views import health, insert, get

def create_app():
    api = Blueprint('api', __name__)
    app = Flask(__name__)

    # define api routes
    api.add_url_rule('/status', 'health', view_func=health, methods=['GET'])

    api.add_url_rule('/despesas', 'insert', view_func=insert, methods=['POST'])

    api.add_url_rule('/despesas', 'get', view_func=get, methods=['GET'])

    app.register_blueprint(api, url_prefix='/api')
    return app