from functions.georoc_api import GeoRocAPI
from ipywidgets import widgets


class MyApp:
    def __init__(self):
        self.api = None
        self.api_key_text = widgets.Password(description='API Key:')
        self.save_button = widgets.Button(description="Save")
        self.save_button.on_click(self.save_api_key)
        display(self.api_key_text, self.save_button)

    def save_api_key(self, sender):
        api_key = self.api_key_text.value
        self.api = GeoRocAPI(api_key)
        GeoRocAPI.api_key = api_key
        print("API key saved and API connection established!")