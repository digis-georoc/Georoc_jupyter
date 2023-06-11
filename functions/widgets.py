from ipywidgets import widgets
from ipywidgets import Layout

# Erstellen Sie ein Text-Widget
api_key_widget = widgets.Text(
    placeholder='Geben Sie Ihren API-Schlüssel ein',
    description='API Key:',
    disabled=False,
    layout=Layout(width="auto")
)

limit_widget = widgets.Text(
    placeholder='Enter a value for Limit',
    description='Limit:'
)

offset_widget = widgets.Text(
    placeholder='Enter a value for Offset',
    description='Offset:'
)

location1_widget = widgets.Text(
    placeholder='Enter a value for Location1',
    description='Location1:'
)

location2_widget = widgets.Text(
    placeholder='Enter a value for Location2',
    description='Location2:'
)

location3_widget = widgets.Text(
    placeholder='Enter a value for Location3',
    description='Location3:'
)

setting_widget = widgets.Text(
    placeholder='Enter a value for Setting',
    description='Setting:'
)

latitude_widget = widgets.Text(
    placeholder='Enter a value for Latitude',
    description='Latitude:'
)

longitude_widget = widgets.Text(
    placeholder='Enter a value for Longitude',
    description='Longitude:'
)

rocktype_widget = widgets.Text(
    placeholder='Enter a value for Rocktype',
    description='Rocktype:'
)

rockclass_widget = widgets.Text(
    placeholder='Enter a value for Rockclass',
    description='Rockclass:'
)

mineral_widget = widgets.Text(
    placeholder='Enter a value for Mineral',
    description='Mineral:'
)

material_widget = widgets.Text(
    placeholder='Enter a value for Material',
    description='Material:'
)

inclusiontype_widget = widgets.Text(
    placeholder='Enter a value for Inclusiontype',
    description='Inclusiontype:'
)

sampletech_widget = widgets.Text(
    placeholder='Enter a value for SampleTech',
    description='SampleTech:'
)

element_widget = widgets.Text(
    placeholder='Enter a value for Element',
    description='Element:'
)

elementtype_widget = widgets.Text(
    placeholder='Enter a value for Elementtype',
    description='Elementtype:'
)

value_widget = widgets.Text(
    placeholder='Enter a value for Value',
    description='Value:'
)

title_widget = widgets.Text(
    placeholder='Enter a value for Title',
    description='Title:'
)

publicationyear_widget = widgets.Text(
    placeholder='Enter a value for Year of Publication',
    description='Year of Publication:'
)

doi_widget = widgets.Text(
    placeholder='Enter a value for DOI',
    description='DOI:'
)

firstname_widget = widgets.Text(
    placeholder='Enter a value for First Name',
    description='First Name:'
)

lastname_widget = widgets.Text(
    placeholder='Enter a value for Lastname',
    description='Lastname:'
)

agemin_widget = widgets.Text(
    placeholder='Enter a value for Age Minimum',
    description='Age Minimum:'
)

agemax_widget = widgets.Text(
    placeholder='Enter a value for Age Maximum',
    description='Age Maximum:'
)

geoage_widget = widgets.Text(
    placeholder='Enter a value for Geo Age',
    description='Geo Age:'
)

geoageprefix_widget = widgets.Text(
    placeholder='Enter a value for Geo Age Prefix',
    description='Geo Age Prefix:'
)

lab_widget = widgets.Text(
    placeholder='Enter a value for Lab',
    description='Lab:'
)


# Specify the desired keys
keys = ['Sample_Num', 'unique_id', 'Batches', 'References', 'SampleName', 'Location_Names', 'Location_Types', 
        'Loc_Data','Elevation_Min', 'Elevation_Max', 'Land_Or_Sea', 'Rock_Types', 'Rock_Classes', 'Rock_Textures', 
        'Age_Min', 'Age_Max', 'Materials', 'Minerals', 'Inclusion_Types', 'Location_Num', 'Latitude', 'Longitude', 
        'Latitude_Min', 'Latitude_Max', 'Longitude_Min', 'Longitude_Max', 'Tectonic_Setting', 'Method', 'Comment', 
        'Institution', 'Item_Name', 'Item_Group', 'Standard_Names', 'Standard_Values', 'Values', 'Units']


# Erstellen Sie eine Checkbox für jeden Schlüssel
checkboxes = [widgets.Checkbox(value=False, description=key) for key in keys]

# Erstellen Sie eine Box, um alle Checkboxen zu halten
checkboxes_box = widgets.VBox(children=checkboxes)