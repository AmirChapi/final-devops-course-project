"""
QuakeWatch Flask application.

This module provides a simple Flask app that returns
a Hello World response.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """
    Root endpoint.

    Returns a simple greeting string.
    """
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
