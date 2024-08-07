from flask import Flask
from flask_cors import CORS
from .routes.repo_market_routes import repo_market_bp
from .routes.root_route import root_bp
from .routes.test_routes import test_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for all /api routes

    app.register_blueprint(repo_market_bp)
    app.register_blueprint(root_bp)
    app.register_blueprint(test_bp)
    return app

app = create_app()
