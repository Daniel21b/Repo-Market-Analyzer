# /Users/danielberhane/Desktop/Repo Market/Repo-Market-Analyzer/backend/app/__init__.py

from flask import Flask
from config import configure_app  # Adjusted import path

app = Flask(__name__)
configure_app(app)

def initialize_routes(app):
    from .routes.repo_market_routes import repo_market_bp
    app.register_blueprint(repo_market_bp)

# Initialize routes
initialize_routes(app)
