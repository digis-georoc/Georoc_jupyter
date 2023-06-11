from ipywidgets import widgets
from ipywidgets import Layout

# Erstellen Sie ein Text-Widget
api_key_widget = widgets.Text(
    placeholder='Geben Sie Ihren API-Schlüssel ein',
    description='API Key:',
    disabled=False,
    layout=Layout(width="auto")
)

widget_list = [
    widgets.Text(placeholder='Enter a value for Limit', description='Limit:'),
    widgets.Text(placeholder='Enter a value for Offset', description='Offset:'),
    widgets.Text(placeholder='Enter a value for Location1', description='Location1:'),
    widgets.Text(placeholder='Enter a value for Location2', description='Location2:'),
    widgets.Text(placeholder='Enter a value for Location3', description='Location3:'),
    widgets.Text(placeholder='Enter a value for Setting', description='Setting:'),
    widgets.Text(placeholder='Enter a value for Latitude', description='Latitude:'),
    widgets.Text(placeholder='Enter a value for Longitude', description='Longitude:'),
    widgets.Text(placeholder='Enter a value for Rocktype', description='Rocktype:'),
    widgets.Text(placeholder='Enter a value for Rockclass', description='Rockclass:'),
    widgets.Text(placeholder='Enter a value for Mineral', description='Mineral:'),
    widgets.Text(placeholder='Enter a value for Material', description='Material:'),
    widgets.Text(placeholder='Enter a value for Inclusiontype', description='Inclusiontype:'),
    widgets.Text(placeholder='Enter a value for SampleTech', description='SampleTech:'),
    widgets.Text(placeholder='Enter a value for Element', description='Element:'),
    widgets.Text(placeholder='Enter a value for Elementtype', description='Elementtype:'),
    widgets.Text(placeholder='Enter a value for Value', description='Value:'),
    widgets.Text(placeholder='Enter a value for Title', description='Title:'),
    widgets.Text(placeholder='Enter a value for Year of Publication', description='Year of Publication:'),
    widgets.Text(placeholder='Enter a value for DOI', description='DOI:'),
    widgets.Text(placeholder='Enter a value for First Name', description='First Name:'),
    widgets.Text(placeholder='Enter a value for Lastname', description='Lastname:'),
    widgets.Text(placeholder='Enter a value for Age Minimum', description='Age Minimum:'),
    widgets.Text(placeholder='Enter a value for Age Maximum', description='Age Maximum:'),
    widgets.Text(placeholder='Enter a value for Geo Age', description='Geo Age:'),
    widgets.Text(placeholder='Enter a value for Geo Age Prefix', description='Geo Age Prefix:'),
    widgets.Text(placeholder='Enter a value for Lab', description='Lab:')
]

# Erstellen Sie ein Layout für die GridBox
grid_layout = widgets.Layout(grid_template_columns="repeat(3, 300px)")  # 2 Spalten, jede 300px breit

# Erstellen Sie eine GridBox, um alle Widgets zu halten
grid2 = widgets.GridBox(children=widget_list, layout=grid_layout)



# Specify the desired keys
keys = ['Sample_Num', 'unique_id', 'Batches', 'References', 'SampleName', 'Location_Names', 'Location_Types', 
        'Loc_Data','Elevation_Min', 'Elevation_Max', 'Land_Or_Sea', 'Rock_Types', 'Rock_Classes', 'Rock_Textures', 
        'Age_Min', 'Age_Max', 'Materials', 'Minerals', 'Inclusion_Types', 'Location_Num', 'Latitude', 'Longitude', 
        'Latitude_Min', 'Latitude_Max', 'Longitude_Min', 'Longitude_Max', 'Tectonic_Setting', 'Method', 'Comment', 
        'Institution', 'Item_Name', 'Item_Group', 'Standard_Names', 'Standard_Values', 'Values', 'Units']


# Erstellen Sie eine Checkbox für jeden Schlüssel
checkboxes = [widgets.Checkbox(value=False, description=key) for key in keys]

# Erstellen Sie ein Layout für die GridBox
grid_layout = widgets.Layout(grid_template_columns="repeat(3, 300px)")  # 3 Spalten, jede 300px breit

# Erstellen Sie eine GridBox, um alle Checkboxen zu halten
grid = widgets.GridBox(children=checkboxes, layout=grid_layout)