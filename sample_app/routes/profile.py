"""
Flask App Route 
For the route profile we have configured the APIs and Templates
"""
import os, datetime, json
from flask import jsonify
from flask import Blueprint, render_template, request
from sample_app.libs.config import APP_PATH

# configure the app route with blueprint
flask_route_profile = Blueprint('flask_route_profile',
                                __name__, 
                                template_folder=os.path.join(APP_PATH, '/templates'), 
                                static_folder=os.path.join(APP_PATH, '../static') )

@flask_route_profile.route("/profile", methods=["GET"])
def profile_list():
    """
    App Route handling profile list.
    
    Returns:
        JSON: JSON response containing the list of profiles.
    """
    parsed_json = []

    # Load user data from JSON file
    with open(os.path.join(APP_PATH, 'static', 'user.json'), encoding='utf-8') as user_file:
        parsed_json = json.load(user_file)

    # Return JSON response with profile list
    return jsonify(parsed_json)

@flask_route_profile.route("/profile/<string:guid>", methods=["GET"])
def profile(guid):
    """
    App Route handling profile data based on GUID.
    
    Args:
        guid (str): GUID of the profile to fetch.
        
    Returns:
        HTML: Rendered profile template with profile data.
    """
    profile_data = []

    # Load user data from JSON file
    with open(os.path.join(APP_PATH, 'static', 'user.json'), encoding='utf-8') as user_file:
        parsed_json = json.load(user_file)

    # Iterate over user data to find matching profile
    for user in parsed_json:
        if user.get('guid') == guid:
            profile_data.append(user)
            break
       
    if len(profile_data) == 0:
        return render_template('profile.html', title='404 Not Found', profile_data=profile_data, profile_id=guid), 404  
           
    # Render profile template with profile data
    return render_template('profile.html', title='Profile', profile_data=profile_data, profile_id=guid)