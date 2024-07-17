from flask_restful import Api
from .repo_market_routes import RepoMarket
from .root_route import root_bp
from .test_routes import test_bp

def initialize_routes(app):
    api = Api(app)
    api.add_resource(RepoMarket, '/api/repo-market')
    app.register_blueprint(root_bp)
    app.register_blueprint(test_bp, url_prefix='/api')
