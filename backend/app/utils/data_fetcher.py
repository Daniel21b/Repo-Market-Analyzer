import requests

def fetch_stfm_data(mnemonic):
    base_url = "https://data.financialresearch.gov/v1"
    endpoint = "/series/timeseries"
    url = f"{base_url}{endpoint}?mnemonic={mnemonic}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}, Response: {response.text}")
