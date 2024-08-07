import requests
import logging

logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://data.financialresearch.gov/v1"

def fetch_mnemonics():
    """
    Fetch all time series mnemonics.
    """
    url = f"{BASE_URL}/metadata/mnemonics"
    logging.debug(f"Fetching mnemonics from URL: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching mnemonics: {e}")
        raise

def fetch_series_data(mnemonic):
    """
    Fetch time series data for a given mnemonic.
    """
    url = f"{BASE_URL}/series/timeseries"
    params = {"mnemonic": mnemonic}
    logging.debug(f"Fetching series data from URL: {url} with params: {params}")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching series data: {e}")
        raise

def search_series(query):
    """
    Search for series based on a query string.
    """
    url = f"{BASE_URL}/metadata/search"
    params = {"query": query}
    logging.debug(f"Searching series from URL: {url} with params: {params}")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Filter results to include only items with 'mnemonic' and 'description'
        filtered_results = [
            item for item in data
            if isinstance(item, dict) and 'mnemonic' in item and 'description' in item
        ]
        
        return filtered_results
    except requests.exceptions.RequestException as e:
        logging.error(f"Error searching series: {e}")
        raise

def fetch_stfm_data(mnemonic):
    """
    Combine searching for a mnemonic and fetching its data.
    """
    try:
        # Search for the mnemonic
        search_results = search_series(mnemonic)
        
        # If we find a match, fetch its data
        if search_results and len(search_results) > 0:
            # Assume the first result is the one we want
            found_mnemonic = search_results[0]['mnemonic']
            return fetch_series_data(found_mnemonic)
        else:
            raise ValueError(f"No matching mnemonic found for: {mnemonic}")
    except Exception as e:
        logging.error(f"Error in fetch_stfm_data: {e}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        mnemonics = fetch_mnemonics()
        logging.info(f"Mnemonics: {mnemonics}")

        series_data = fetch_stfm_data('example_mnemonic')
        logging.info(f"Series Data: {series_data}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
