from flask import Flask
from flask_cors import CORS
from app.routes import repo_market_routes, root_route, test_routes
from config import configure_app

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    configure_app(app)

    # Initialize CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # Be cautious with "*" in production

    # Register blueprints
    app.register_blueprint(repo_market_routes.repo_market_bp)
    app.register_blueprint(root_route.root_bp)
    app.register_blueprint(test_routes.test_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)