import requests
import json
import pandas as pd
from functions.widgets import *


def get_measurement_data(api_key, sampling_feature_id):
    base_url = f"https://api-test.georoc.eu/api/v1/queries/fulldata/{sampling_feature_id}"
    headers = {
        "accept": "application/json",
        "DIGIS-API-ACCESSKEY": api_key
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)['Data'][0]

        # Create a dictionary containing all keys and values from data
        df_data = {key: data[key] for key in keys}

        # Convert all values in df_data to lists
        for key, value in df_data.items():
            if not isinstance(value, list):
                df_data[key] = [value]

        # Find the longest list in df_data
        max_len = max([len(value) for value in df_data.values()])

        # Extend all the lists to the length of the longest list
        for key, value in df_data.items():
            if len(value) < max_len:
                df_data[key] = value + [None] * (max_len - len(value))

        # Create the DataFrame
        df = pd.DataFrame(df_data)

        return df

    else:
        print(f"Error fetching data for sample ID {sampling_feature_id}, Status code: {response.status_code}")
        return None
    