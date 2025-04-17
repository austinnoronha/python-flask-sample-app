"""
Flask App Route 
For the route home we have configured the APIs and Templates
"""
import os
import json
from flask import Blueprint, render_template
from sample_app.libs.config import APP_PATH

# Configure the app route with blueprint
flask_route_home = Blueprint('flask_route_home',
                             __name__,
                             template_folder='../templates',
                             static_folder='../static')

@flask_route_home.route("/", methods=["GET", "POST"])
def home():
    """
    App Route handling homepage.

    Returns:
        str: Rendered HTML template for the homepage.
    """
    # Default username
    name = 'Austin'

    # Initialize list of users
    list_users = []

    # Load user data from JSON file
    with open(os.path.join(APP_PATH, 'static', 'user.json'), encoding='utf-8') as user_file:
        list_users = json.load(user_file)

    # Render HTML template with data
    return render_template('index.html', title='Welcome', username=name, list_users=list_users)
