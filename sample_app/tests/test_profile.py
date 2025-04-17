"""Pytest Start Route Testing."""
import os
import sys
import json
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from flask import Flask
from sample_app.routes.profile import flask_route_profile
from sample_app.libs.config import APP_PATH


@pytest.fixture
def client():
    """Fixture to set up Flask test client."""
    app = Flask(__name__, template_folder=os.path.join(APP_PATH, 'templates'))  # Adjust the path to your templates folder
    app.register_blueprint(flask_route_profile)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        

def test_profile_list_route(client):
    """Test the profile list route."""
    response = client.get("/profile")
    # print("response.status_code ------> ",response.status_code)  # Debugging: Print the response data for inspection
    # print("response.data ------> ",response.data)  # Debugging: Print the response data for inspection
    assert response.status_code == 200
    assert response.is_json  # Logic check: Ensure the response is JSON
    assert isinstance(response.json, list)  # Ensure the response is a list

def test_profile_route_valid_guid(client):
    """Test the profile route with a valid GUID."""
    valid_guid = "bad3efcb-ec77-4f99-9523-e790d6064731"  # Replace with a valid GUID from your data
    response = client.get(f"/profile/{valid_guid}")
    # print("response.status_code ------> ",response.status_code)  # Debugging: Print the response data for inspection
    # print("response.data ------> ",response.data)  # Debugging: Print the response data for inspection
    assert response.status_code == 200
    assert b"Profile" in response.data  # Logic check: Ensure "Profile" is in the response

def test_profile_route_invalid_guid(client):
    """Test the profile route with an invalid GUID."""
    invalid_guid = "invalid-guid"
    response = client.get(f"/profile/{invalid_guid}")
    print("response.data ------> ",response.data)  # Debugging: Print the response data for inspection
    assert response.status_code == 404  # Negative assertion: Ensure 404 for invalid GUID

def test_profile_route_xss(client):
    """Test the profile route for XSS vulnerability."""
    xss_payload = "<script>alert('XSS')</script>"
    response = client.get(f"/profile/{xss_payload}")
    assert xss_payload.encode() not in response.data  # Ensure XSS payload is not reflected