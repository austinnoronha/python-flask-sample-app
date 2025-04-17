""" 
In this sample, the Flask app object is contained within the sample_app; 
along with relative imports. Because

The solution is to provide a simple alternate startup file, like this present
startup.py, that just imports the app object. You can then just specify
startup:app in the Gunicorn command.
"""

from sample_app.main import app


if __name__ == '__main__':
    app.run(debug = True,  host = '0.0.0.0', port = 5000)