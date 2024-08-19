#!/usr/bin/python3
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Define a route for the root URL ("/") with strict_slashes set to False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Check if the executed file is the main program and run the app
if __name__ == '__main__':
    # Start the Flask application listening on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
