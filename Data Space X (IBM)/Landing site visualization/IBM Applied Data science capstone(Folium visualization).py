import folium.map
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import wget
import folium
from folium.features import DivIcon
from folium.plugins import MousePosition
from folium.plugins import MarkerCluster

space11=wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
space11df=pd.read_csv(space11)
space1=space11df[['Launch Site', 'class', 'Lat', 'Long']]
space2=space1.groupby(['Launch Site'],as_index=False).first()
space1
space2
space3=space2[['Launch Site', 'Lat', 'Long']]

# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)

# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
circle =folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)

site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
site_map

Mc_cl=MarkerCluster()

def align_marker(Launch_outcome):
    if Launch_outcome ==1:
        return 'green'
    else:
        return 'yellow'

space1=space1['class'].apply(align_marker)
space1

# Assuming some initial setup for site_map, Mc_cl, and marker objects

# Adding Mc_cl as a child to site_map
site_map.add_child(Mc_cl)

# Iterating through space1 DataFrame to add markers to Mc_cl
for index, row in space1.iterrows():
    # Assuming some logic to create or retrieve a marker object for each record
    marker = create_marker(record)
    
    # Add marker as a child to Mc_cl
    Mc_cl.add_child(marker)

# Display the updated site_map
print(site_map)