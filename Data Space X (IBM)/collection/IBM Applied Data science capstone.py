import requests
import pandas as pd
import numpy as np
import datetime
pd.set_option('display.max_column',None)
pd.set_option('display.max_colwidth',None)
def getBoosterVersion(data):
    for x in data['rocket']:
        if x:
            response=requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
            BoosterVersion.append(response['name'])
            
def getLaunchSite(data):
    for x in data['launchpad']:
       if x:
         response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
         Longitude.append(response["longitude"])
         Latitude.append(response["latitude"])
         LaunchSite.append(response["name"])

def getpayload(data):
    for load in data['payloads']:
        if load:
            response=requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
            PayloadMass.append(response['mass_kg'])
            Orbit.append(response['orbit'])                     

def getcore(data):
    for core in data['cores']:
        if core['core']!= None:
            response= requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
            Block.append(response['block'])
            ReusedCount.append(response['reuse_count'])
            Serial.append(response['serial'])
        else:
            Block.append(None)
            Reusedcount.append(None)
            Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flight.append(core['flight'])
            GrindFin.append(core['grindfins'])
            Reused.append(core['reuse'])
            Legs.append(core['legs'])
            LandingPad.append(core['landingpad'])
            
            
spacexurl='https://api.spacexdata.com/v4/launches/past'
response=requests.get(spacexurl)
response.content


static_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
responses=requests.get(static_json_url)
responses.content
response.status_code
data=pd.json_normalize(response.json())
data

data=data[['rocket','payloads','launchpad','cores','flight_number','date_utc',]]
data
data=data[data['cores'].map(len)==1]
data=data[data['payloads'].map(len)==1]
data
data['cores']=data['cores'].map(lambda x:x[0])
data['payloads']=data['payloads'].map(lambda x:x[0])
data
data['date']=pd.to_datetime(data['date_utc']).dt.date
data=data[data['date']<=datetime.date(2020,11,13)]
data
#globalvariables

BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []
getBoosterVersion(data)
getLaunchSite(data)
getpayload(data)
getcore(data)

d#ef launchda(launch_dict):
    headers = list(launch_dict.keys())
    print("\t".join(headers)) 
    for i in range(len(launch_dict['flightnumber'])):
        row = []
        for key in headers:
            if i < len(launch_dict[key]):
                row.append(str(launch_dict[key][i]))
            else:
                row.append("NA")
                print("  \t".join(row))
    

launch_dict={
'flightnumber':list(data['flight_number']),
'Date':list(data['date']),
'BoosterVersion':BoosterVersion,
'PayloadMass':PayloadMass,
'Orbit':Orbit,
'LaunchSite':LaunchSite,
'Outcome':Outcome,
'Flights':Flights,
'GridFins':GridFins,
'Reused':Reused,
'Legs':Legs,
'LandingPad':LandingPad,
'Block':Block,
'ReusedCount':ReusedCount,
'Serial':Serial,
'Longitude': Longitude,
'Latitude': Latitude}
# Check lengths of all arrays in the dictionary
array_lengths = [len(arr) for arr in launch_dict.values()]

if len(set(array_lengths)) > 1:
    max_length = max(array_lengths)
    
    # Adjust arrays to have the same length
    launch_dict = {key: arr + [None] * (max_length - len(arr)) for key, arr in launch_dict.items()}

# Create the DataFrame from the updated dictionary
launch_data_df = pd.DataFrame(launch_dict)


launch_data_df.head()
launch_data_df.count()

