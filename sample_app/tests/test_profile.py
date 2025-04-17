# filepath: tests/test_profile.py
import os, sys
import json
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from flask import Flask
from sample_app.routes.profile import flask_route_profile
from sample_app.libs.config import APP_PATH

@pytest.fixture
def client():
    """Fixture to set up Flask test client."""
    app = Flask(__name__, template_folder=os.path.join(APP_PATH, 'templates'))
    app.register_blueprint(flask_route_profile)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_profile_list_success(client, monkeypatch):
    """Test the /profile route for successful response."""
    mock_data = [{"guid": "1234", "name": "John Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile")
    assert response.status_code == 200
    assert response.json == mock_data


def test_profile_success(client, monkeypatch):
    """Test the /profile/<guid> route for successful response."""
    mock_data = [{"guid": "1234", "name": "John Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert response.status_code == 200
    assert b"John Doe" in response.data

def test_profile_not_found(client, monkeypatch):
    """Test the /profile/<guid> route when the GUID is not found."""
    mock_data = [{"guid": "5678", "name": "Jane Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert response.status_code == 404
    assert b"404 Not Found" in response.data

def test_profile_xss(client, monkeypatch):
    """Test the /profile/<guid> route for XSS vulnerability."""
    mock_data = [{"guid": "1234", "name": "<script>alert('XSS')</script>"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert b"<script>alert('XSS')</script>" not in response.data

def test_profile_list_invalid_method(client):
    """Test the /profile route with an invalid HTTP method."""
    response = client.post("/profile")
    assert response.status_code == 405  # Method Not Allowed

def test_profile_missing_guid(client):
    """Test the /profile/<guid> route with missing GUID."""
    response = client.get("/profile/")
    assert response.status_code == 404  # Not Found

def test_profile_invalid_guid(client, monkeypatch):
    """Test the /profile/<guid> route with an invalid GUID."""
    mock_data = [{"guid": "1234", "name": "John Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/invalid-guid")
    assert response.status_code == 404
    assert b"404 Not Found" in response.data

def test_profile_success(client, monkeypatch):
    """Test the /profile/<guid> route for successful response."""
    mock_data = [{"guid": "1234", "name": "John Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert response.status_code == 200
    assert b"John Doe" in response.data

def test_profile_not_found(client, monkeypatch):
    """Test the /profile/<guid> route when the GUID is not found."""
    mock_data = [{"guid": "5678", "name": "Jane Doe"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert response.status_code == 404
    assert b"404 Not Found" in response.data

def test_profile_xss(client, monkeypatch):
    """Test the /profile/<guid> route for XSS vulnerability."""
    mock_data = [{"guid": "1234", "name": "<script>alert('XSS')</script>"}]

    # Mock the JSON file loading
    monkeypatch.setattr(json, "load", lambda *args, **kwargs: mock_data)

    response = client.get("/profile/1234")
    assert b"<script>alert('XSS')</script>" not in response.data