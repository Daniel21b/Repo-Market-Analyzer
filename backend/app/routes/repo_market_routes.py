from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from app.services.repo_market_service import RepoMarketService
from app.models.repo_market_model import RepoMarketModel
from app.models.validation import RepoMarketData
from pydantic import ValidationError

repo_market_bp = Blueprint('repo_market', __name__)
api = Api(repo_market_bp)
repo_market_service = RepoMarketService()

class RepoMarket(Resource):
    def post(self):
        data = request.get_json()
        try:
            validated_data = RepoMarketData(**data)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400
        
        repo_market_model = RepoMarketModel(
            start_date=validated_data.start_date,
            end_date=validated_data.end_date,
            bank=validated_data.bank,
            loan_amount=validated_data.loan_amount
        )
        
        try:
            interest_rate_prediction = repo_market_service.predict_interest_rate(repo_market_model.to_dict())
            market_analysis = repo_market_service.analyze_market(repo_market_model.to_dict())
            risk_assessment = repo_market_service.assess_risk(repo_market_model.to_dict())
            
            response = {
                'interest_rate_prediction': interest_rate_prediction,
                'market_analysis': market_analysis,
                'risk_assessment': risk_assessment
            }
            return jsonify(response)
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

api.add_resource(RepoMarket, '/api/repo-market')
