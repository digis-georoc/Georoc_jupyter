import requests
import json

class GeoRocAPI:
    api_key = None

    def __init__(self, api_key):
        GeoRocAPI.api_key = api_key
        print("API Key:", GeoRocAPI.api_key)
        self.base_url = "https://api-dev.georoc.eu/api/v1/"
        self.headers = {
            "accept": "application/json",
            "DIGIS-API-ACCESSKEY": GeoRocAPI.api_key
        }

    def api_query(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)
            print(f"API query successful for endpoint:{endpoint}", "\n")
            return data
        else:
            print(f"API query error for endpoint: {endpoint}, Statuscode:{response.status_code}", "\n")
            print(response.text)
            return None

    def get_filtered_samples(
        self,
        limit=None,
        offset=None,
        setting=None,
        location1=None,
        location2=None,
        location3=None,
        latitude=None,
        longitude=None,
        rocktype=None,
        rockclass=None,
        mineral=None,
        material=None,
        inclusiontype=None,
        sampletech=None,
        element=None,
        elementtype=None,
        value=None,
        title=None,
        publicationyear=None,
        doi=None,
        firstname=None,
        lastname=None,
        agemin=None,
        agemax=None,
        geoage=None,
        geoageprefix=None,
        lab=None
    ):
        endpoint = "queries/samples"

        filters = {
            key: value
            for key, value in locals().items()
            if key not in ["self", "endpoint"] and value is not None
        }

        data = self.api_query(endpoint, params=filters)
        return data
