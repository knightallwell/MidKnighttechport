import pandas as pd
import numpy as np


space=pd.read_csv(r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv')
space.head()
space.count()
space['Outcome'].unique()
space.describe()
space.info()
space.isnull().sum()/len(space)*100
space['Outcome'].value_counts()
space['LaunchSite'].value_counts()
space['Orbit'].value_counts()
space['LandingPad'].value_counts()
space['Serial'].value_counts()
space['BoosterVersion'].value_counts()
space.isnull().sum()
space=space.dropna(axis=0)
space.info()
# Safely creating a set of bad outcomes using only available indices
available_indices = [1, 3, 5]  # Adjusted to match the length of 'Outcome' column
bad_outcomes = set(space['Outcome'].iloc[available_indices])
print("Bad outcomes:", bad_outcomes)

# Enumerate over the values in the 'Outcome' column
for i, outcome in enumerate(space['Outcome']):
    print(i, outcome)

space['Date']=pd.to_datetime(space['Date'],format='ISO8601')
space.info()

space2 = pd.get_dummies(space, columns=['Outcome'])
space2

dummy_columns = space2.filter(like='Outcome_').columns
space2[dummy_columns] = space2[dummy_columns].astype(int)
space2


outcome_counts = pd.get_dummies(space['Outcome']).count()
print("Outcome counts:\n", outcome_counts)


landing_class = [0 if outcome in bad_outcomes else 1 for outcome in space['Outcome']]

# Assign it to the landing_class variable
space['landing_class'] = landing_class
space['landing_class'].value_counts()

space2

from sklearn.preprocessing import  LabelEncoder
en = LabelEncoder()
columns_to_encode = ['GridFins', 'Reused', 'Legs']
for col in columns_to_encode:
    space2[col] = en.fit_transform(space2[col])

space2

Orbit=pd.get_dummies(space2['Orbit']).astype(int)
space2=pd.concat([space2,Orbit], axis=1)
space2.drop(['Orbit'],axis=1, inplace=True)
space2

LaunchSite=pd.get_dummies(space2['LaunchSite']).astype(int)
space2=pd.concat([space2,LaunchSite], axis=1)
space2.drop(['LaunchSite'],axis=1, inplace=True)
space2


