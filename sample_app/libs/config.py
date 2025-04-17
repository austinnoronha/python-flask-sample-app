"""
Flask App Config Lib 
Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
"""
import os, sys
from dotenv import dotenv_values

# CONFIG = {"MONGO_DB":"", ...}
CONFIG = dotenv_values(".env")
APP_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))