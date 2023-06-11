from functions.widgets import *

# Define API-Key, Base-URL and headers
api_key = api_key_widget.value
base_url = "https://api-test.georoc.eu/api/v1/"
headers = {
    "accept": "application/json",
    "DIGIS-API-ACCESSKEY": api_key
}