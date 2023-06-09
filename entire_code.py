import requests
import json
import io
from contextlib import redirect_stdout
import pandas as pd
from tqdm.auto import tqdm
from ipywidgets import widgets


# Erstellen Sie ein Text-Widget
api_key_widget = widgets.Text(
    placeholder='Geben Sie Ihren API-Schlüssel ein',
    description='API Schlüssel:',
    disabled=False
)

# Anzeige des Widgets
display(api_key_widget)


# Define API-Key, Base-URL and headers
api_key = api_key_widget.value
base_url = "https://api-test.georoc.eu/api/v1/"
headers = {
    "accept": "application/json",
    "DIGIS-API-ACCESSKEY": api_key
}


def api_query(endpoint, params=None):
    response = requests.get(f"{base_url}{endpoint}", headers=headers, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        print("\n", f"API query successful for endpoint:{endpoint}", "\n")
        return data
    else:
        print(f"API query error for endpoint: {endpoint}, Statuscode:{response.status_code}", "\n")
        print(response.text)
        return None


def get_filtered_samples(
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
        if key not in ["endpoint"] and value is not None
    }

    data = api_query(endpoint, params=filters)
    return data


# Specify the desired keys
keys = ['Item_Name', 'Values', 'Units', 'Item_Group']


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



def check_api_connection():
    endpoint = "ping"
    response = api_query(endpoint)

    if response is not None:
        print("Connection to API server successful!\n")
    else:
        print("Failed to connect to API server!\n")
        exit(1)


# Check the connection to the API server
check_api_connection()


# Get SamplingFeatureIDs for the given filters
filtered_samples_combined = get_filtered_samples(
    limit="1",  # update the limit to retrieve more than one SamplingFeatureID
    location1="EAST AFRICAN RIFT",
    location2="ETHIOPIAN RIFT",
    setting="RIFT VOLCANICS"
)

print(filtered_samples_combined, "\n")

# Extract SamplingFeatureIDs
if "Data" in filtered_samples_combined and filtered_samples_combined["Data"]:
    sampling_feature_ids = [sample["SampleID"] for sample in filtered_samples_combined["Data"]]
    print("\n", f"The extracted SampleIDs are:", sampling_feature_ids, "\n")
else:
    print("No data found or unexpected data structure", "\n")

# Create an empty DataFrame to store all measurement data
measurement_data = pd.DataFrame()

# Initialize the progress bar
progress_bar = tqdm(
    total=len(sampling_feature_ids),
    desc="Processing",
    unit="sample",
    dynamic_ncols=True,
    leave=True,
    colour="#00507d",
)

# Redirect the standard output to suppress intermediate prints
with io.StringIO() as buf, redirect_stdout(buf):

    # Iterate over the list of SamplingFeatureIDs
    for sampling_feature_id in sampling_feature_ids:
        print(f"Fetching measurement data for SamplingFeatureID: {sampling_feature_id}")

        # Get the measurement data for the current SamplingFeatureID
        df = get_measurement_data(api_key, sampling_feature_id)

        # Check if the dataframe is not empty and not None
        if df is not None and not df.empty:
            # Append the dataframe to the measurement_data DataFrame
            measurement_data = measurement_data.append(df, ignore_index=True)
        elif df is None:
            print(f"Error occurred while fetching data for SamplingFeatureID {sampling_feature_id}")
        else:
            print(f"No measurement data found for SamplingFeatureID {sampling_feature_id}")

        # Update the progress bar for each completed step
        progress_bar.update(1)

# Close the progress bar after the loop
progress_bar.close()


# Save the combined measurement_data DataFrame
measurement_data.to_csv('measurement_data.csv', index=False)