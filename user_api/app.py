from flask import Flask
from flask_smorest import Api
from resources.user import UserBlueprint

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'User REST API'
app.config['API_VERSION'] = 'v1.0'
app.config['OPENAPI_VERSION'] = '3.1'
app.config['OPENAPI_URL_PREFIX'] = '/'

api = Api(app)

api.register_blueprint(UserBlueprint)
