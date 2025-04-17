"""Flask App Start Module."""
import os
import sys

# import flask dependencies
from flask import Flask
from flask_cors import CORS
from flask import send_from_directory

# import app dependencies
from sample_app.libs.config import CONFIG

# Get Blueprint Apps
from sample_app.routes.home import flask_route_home
from sample_app.routes.profile import flask_route_profile

# Create and name Flask app
app = Flask(__name__)

# database connection
app.config['MONGODB_SETTINGS'] = {'HOST':CONFIG['MONGO_URI'],'DB': CONFIG['MONGO_DB']}
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.debug = os.environ.get('DEBUG',False)

# setup CORS
CORS(app)
resources = {r"/*": {"origins": "*"}}
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False

# Register Blueprints
app.register_blueprint(flask_route_home)
app.register_blueprint(flask_route_profile)

# add support for favicon
@app.route('/favicon.ico')
def favicon():
    """App Route for favicon default route"""
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
