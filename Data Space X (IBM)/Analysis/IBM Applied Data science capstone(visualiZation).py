import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

visibm= pd.read_csv(r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')
visibm.head()
sns.catplot(y='PayloadMass',x='FlightNumber',hue='Class',data=visibm, aspect=5 )
plt.ylabel('PayloadMass', fontsize=20)
plt.xlabel('FlightNumber', fontsize=20)
plt.show()
#1
sns.catplot(x='FlightNumber',y='LaunchSite',hue='Class', data=visibm )
plt.xlabel('FlightNumber', fontsize=20)
plt.ylabel('LaunchSite', fontsize=20)
plt.show()
#2
sns.catplot(x='PayloadMass',y='LaunchSite',hue='Class', data=visibm )
plt.xlabel('PayloadMass', fontsize=20)
plt.ylabel('LaunchSite', fontsize=20)
plt.show()

sns.countplot(x='Orbit',hue='Class',data=visibm)

sns.relplot(x='FlightNumber', y='Orbit', kind='scatter', hue='Class', data=visibm)

sns.relplot(x='PayloadMass', y='Orbit', kind='scatter', hue='Class', data=visibm)

year=[]
def Extract_year(date):
    for i in visibm["Date"]:
        year.append(i.split("-")[0])
    return year

year=visibm['Date']
year
sns.relplot(x='Date', y='Class', kind='scatter', data=visibm)
visibm.info()
feature