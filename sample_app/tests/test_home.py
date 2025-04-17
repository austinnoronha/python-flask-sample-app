"""Pytest Start Route Testing."""
import os
import sys
import json
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest
from flask import Flask
from sample_app.routes.home import flask_route_home
from sample_app.libs.config import APP_PATH

@pytest.fixture
def client():
    """Fixture to set up Flask test client."""
    app = Flask(__name__, template_folder=os.path.join(APP_PATH, 'templates'))  # Adjust the path to your templates folder
    app.register_blueprint(flask_route_home)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test the home route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data  # Logic check: Ensure "Welcome" is in the response

def test_home_route_post(client):
    """Test the home route with POST method."""
    response = client.post("/negative-value")
    assert response.status_code == 404  # Negative assertion: POST should not be allowed

def test_home_route_xss(client):
    """Test the home route for XSS vulnerability."""
    xss_payload = "<script>alert('XSS')</script>"
    response = client.get(f"/?input={xss_payload}")
    assert xss_payload.encode() not in response.data  # Ensure XSS payload is not reflected