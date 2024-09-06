import folium.map
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import wget
import folium
from folium.features import DivIcon
from folium.plugins import MousePosition
from folium.plugins import MarkerCluster
import branca

space11=wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
space11df=pd.read_csv(space11)
space1=space11df[['Launch Site', 'class', 'Lat', 'Long']]
space2=space1.groupby(['Launch Site'],as_index=False).first()
space1
space2
space3=space2[['Launch Site', 'Lat', 'Long']]


nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)


circle =folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))

marker = folium.map.Marker(
    nasa_coordinate,
    
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)
site_map.save('map.html')
site_map
#CCAFS LC-40
CCAFSLC_40= [28.562302,-80.577356]
site_map1 = folium.Map(location=CCAFSLC_40, zoom_start=10)

circle =folium.Circle(CCAFSLC_40, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('CCAFSLC_40'))

marker = folium.map.Marker(
    CCAFSLC_40,
    
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC_40',
        )
    )
site_map1.add_child(circle)
site_map1.add_child(marker)
site_map1

CCAFSSLC_40= [28.563197,-80.576820]
site_map2 = folium.Map(location=CCAFSSLC_40, zoom_start=10)
circle=folium.Circle(CCAFSSLC_40, radius=1000, color='#d45600', fill=True).add_child(folium.Popup('CCAFSSLC_40'))
marker=folium.map.Marker(
    CCAFSSLC_40,
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size:20; color:#d45600">;"><b>%s</div>'%'CCAFSSLC_40'))
site_map2.add_child(circle)
site_map2.add_child(marker)

#KSCLC_390A
KSCLC_390A = [28.573255, -80.646895]

site_map3 = folium.Map(location=KSCLC_390A, zoom_start=10)

circle = folium.Circle(
    location=KSCLC_390A,
    radius=1000,
    color='#d35400',
    fill=True
).add_child(folium.Popup('KSCLC_390A'))

marker = folium.Marker(
    location=KSCLC_390A,
    icon=DivIcon(
        icon_size=(150, 36),
        icon_anchor=(0, 0),
        html='<div style="font-size: 12px; color:#d35400;"><b>KSCLC_390A</b></div>'
    )
)

site_map3.add_child(circle)
site_map3.add_child(marker)

# Display the map
site_map3


VAFBSLC_4E= [34.632834,-120.610745]

site_map4=folium.Map(location=VAFBSLC_4E, zoom_start=10)
circle=folium.Circle(
    location=VAFBSLC_4E,
    radius=1000,
    color='#d35400',
    fill=True
).add_child(folium.Popup('VAFBSLC_4E'))

marker=folium.Marker(
    location=VAFBSLC_4E,
    icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 12px; color:#d35400;"><b>VAFBSLC_4E</b></div>'
    )
)
site_map4.add_child(circle)
site_map4.add_child(marker)
site_map4



#
space11df
marker_cluster = MarkerCluster()

def align_marker(Launch_outcome):
    if Launch_outcome ==1:
        return 'green'
    else:
        return 'red'

space11df['class']=space11df['class'].apply(align_marker)
space11df




site_map.add_child(marker_cluster)


for index, record in space11df.iterrows():
    marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
    marker_cluster.add_child(marker)
site_map

site_map1.add_child(marker_cluster)
for index in space11df.iterrows():
    marker = folium.map.Marker(
    CCAFSLC_40,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFSLC_40',
        )
    )
    marker_cluster.add_child(marker)
site_map1

site_map2.add_child(marker_cluster)
for index in space11df.iterrows():
    marker=folium.map.Marker(
    CCAFSSLC_40,
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size:20; color:#d45600">;"><b>%s</div>'%'CCAFSSLC_40'))
    marker_cluster.add_child(marker)
site_map2

site_map3.add_child(marker_cluster)
for index in space11df.iterrows():
    marker = folium.Marker(
    location=KSCLC_390A,
    icon=DivIcon(
        icon_size=(150, 36),
        icon_anchor=(0, 0),
        html='<div style="font-size: 12px; color:#d35400;"><b>KSCLC_390A</b></div>'
    )
)
    marker_cluster.add_child(marker)   
site_map3

site_map4.add_child(marker_cluster)
for index in space11df.iterrows():
    marker=folium.Marker(
    location=VAFBSLC_4E,
    icon=DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 12px; color:#d35400;"><b>VAFBSLC_4E</b></div>'
    )
)
    marker_cluster.add_child(marker)  
site_map4



from math import cos, sqrt, sin, atan2, radians

# Distance calculation function
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6378.0  # Approximate radius of Earth in km
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    
    return distance

# Coordinates of the coastlines
coastlines = [
    (28.562302, -80.577356),
    (28.563197, -80.576820),
    (28.573255, -80.646895),
    (34.632834, -120.610745)
]

# Function to find the closest coastline point
def closest_coastline(nasa_coordinate, coastlines):
    min_distance = float('inf')
    closest_point = None
    for lat, lon in coastlines:
        distance = calculate_distance(nasa_coordinate[0], nasa_coordinate[1], lat, lon)
        if distance < min_distance:
            min_distance = distance
            closest_point = (lat, lon)
    return closest_point, min_distance

# NASA coordinate
nasa_coordinate = [29.559684888503615, -95.0830971930759]

# Find the closest coastline point and the distance
closest_point, min_distance = closest_coastline(nasa_coordinate, coastlines)

# Initialize a map centered on the NASA coordinate
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)

# Add a marker for the closest coastline point
closest_point_marker = folium.Marker(
    closest_point,
    icon=DivIcon(
        icon_size=(20, 20),
        icon_anchor=(0, 0),
        html='<div style="font-size: 12px; color:#d35400;"><b>{:.2f} KM</b></div>'.format(min_distance),
    )
)
site_map.add_child(closest_point_marker)

# Add a marker for the NASA launch site
launch_site_marker = folium.Marker(
    location=nasa_coordinate,
    popup='NASA JSC',
    icon=folium.Icon(color='blue', icon='info-sign')
)
site_map.add_child(launch_site_marker)

# Display the map
site_map
