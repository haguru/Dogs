import os

from flask import Flask
import json

app = Flask(__name__)

if __name__ == "__main__":

    #app.config.from_pyfile('config.py', silent=True)
    from views import *

    app.run(debug=True)