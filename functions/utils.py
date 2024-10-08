import requests
import json
import pandas as pd
from functions.widgets import *
from functions.georoc_api import *
from IPython.display import display, HTML
import ipywidgets as widgets


def get_measurement_data(api_key, sampling_feature_id, selected_keys_data, selected_keys_metadata):
    base_url = f"https://api-test.georoc.eu/api/v1/queries/fulldata/{sampling_feature_id}"
    headers = {
        "accept": "application/json",
        "DIGIS-API-ACCESSKEY": api_key
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)['batchData'][0]['results']
        metadata = json.loads(response.text)

        # Create list of dictionaries containing only the selected keys and their values from data
        #df_data = {key: data[key] for key in selected_keys_data}
        df_metadata = {key: metadata[key] for key in selected_keys_metadata}
        
        df_data = []
        for l in data:
            data_entry = {key: l[key] for key in selected_keys_data}
            df_entry = df_metadata | data_entry
            df_data.append(df_entry)

        # Create the DataFrame
        df = pd.DataFrame(df_data)

        return df

    else:
        print(f"Error fetching data for sample ID {sampling_feature_id}, Status code: {response.status_code}")
        return None


def get_selected_keys(checkboxes):
    selected_keys = []
    for checkbox in checkboxes:
        if checkbox.value:
            selected_keys.append(checkbox.description)
    return selected_keys
