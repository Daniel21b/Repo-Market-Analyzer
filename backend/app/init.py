from flask import Flask
from config import configure_app  # Update import to be relative to backend directory

app = Flask(__name__)
configure_app(app)