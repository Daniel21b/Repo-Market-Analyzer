from flask import Blueprint, jsonify
from app.services.repo_market_service import RepoMarketService

test_bp = Blueprint('test', __name__)
repo_market_service = RepoMarketService()

@test_bp.route('/test-fetch-data/<mnemonic>', methods=['GET'])
def test_fetch_data(mnemonic):
    try:
        repo_market_service.fetch_and_prepare_data(mnemonic)
        return jsonify({"message": "Data fetched and prepared successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@test_bp.route('/test-train-model', methods=['GET'])
def test_train_model():
    try:
        accuracy = repo_market_service.train_model()
        return jsonify({"message": "Model trained successfully", "accuracy": accuracy}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
