import requests
import json
import pandas as pd
from functions.widgets import *
from functions.georoc_api import *


def get_measurement_data(api_key, sampling_feature_id, selected_keys):
    base_url = f"https://api-test.georoc.eu/api/v1/queries/fulldata/{sampling_feature_id}"
    headers = {
        "accept": "application/json",
        "DIGIS-API-ACCESSKEY": api_key
    }

    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text)['Data'][0]

        # Create a dictionary containing only the selected keys and their values from data
        df_data = {key: data[key] for key in selected_keys}

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


# Iterate over the list of SamplingFeatureIDs
for index, sampling_feature_id in enumerate(sampling_feature_ids):
    print(f"Fetching measurement data for SamplingFeatureID: {sampling_feature_id}")

    # Get the selected keys from the checkboxes
    selected_keys = [checkboxes[i].description for i in range(len(checkboxes)) if checkboxes[i].value]

    # Get the measurement data for the current SamplingFeatureID using the selected keys
    df = get_measurement_data(my_app.api.api_key, sampling_feature_id, selected_keys)

    # Check if the dataframe is not empty and not None
    if df is not None and not df.empty:
        # Append the dataframe to the measurement_data DataFrame
        measurement_data = measurement_data._append(df, ignore_index=True)

        # Print the dataframe
        print(f"Data for SamplingFeatureID {sampling_feature_id}:\n", df)
    elif df is None:
        print(f"Error occurred while fetching data for SamplingFeatureID {sampling_feature_id}")
    else:
        print(f"No measurement data found for SamplingFeatureID {sampling_feature_id}")

    # Update the progress bar
    progress_bar.value = index + 1



def get_selected_keys(checkboxes):
    selected_keys = []
    for checkbox in checkboxes:
        if checkbox.value:
            selected_keys.append(checkbox.description)
    return selected_keys