from flask import Blueprint, jsonify, request
from app.services.repo_market_service import RepoMarketService
from app.utils.data_fetcher import fetch_mnemonics, fetch_series_data, search_series

test_bp = Blueprint('test', __name__)
repo_market_service = RepoMarketService()

@test_bp.route('/test-fetch-mnemonics', methods=['GET'])
def test_fetch_mnemonics():
    try:
        mnemonics = fetch_mnemonics()
        return jsonify({"message": "Mnemonics fetched successfully", "data": mnemonics}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@test_bp.route('/test-search-series', methods=['GET'])
def test_search_series():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    try:
        results = search_series(query)
        if results:
            return jsonify({"message": "Search completed successfully", "data": results}), 200
        else:
            return jsonify({"message": "No results found", "data": []}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@test_bp.route('/test-fetch-data/<mnemonic>', methods=['GET'])
def test_fetch_data(mnemonic):
    try:
        data = fetch_series_data(mnemonic)
        return jsonify({"message": "Data fetched successfully", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add more test routes as needed