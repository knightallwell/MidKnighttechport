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

# Safely creating a set of bad outcomes using only available indices
available_indices = [1, 3, 5]  # Adjusted to match the length of 'Outcome' column
bad_outcomes = set(space['Outcome'].iloc[available_indices])
print("Bad outcomes:", bad_outcomes)

# Enumerate over the values in the 'Outcome' column
for i, outcome in enumerate(space['Outcome']):
    print(i, outcome)

# Creating dummy variables
space2 = pd.get_dummies(space, columns=['Outcome'])
space2

# Convert dummy columns to integers
dummy_columns = space2.filter(like='Outcome_').columns
space2[dummy_columns] = space2[dummy_columns].astype(int)
space2

# Count occurrences of each outcome
outcome_counts = pd.get_dummies(space['Outcome']).count()
print("Outcome counts:\n", outcome_counts)

#Create a list for landing class
landing_class = [0 if outcome in bad_outcomes else 1 for outcome in space['Outcome']]

# Assign it to the landing_class variable
space['landing_class'] = landing_class
space['landing_class'].value_counts()
# Display the DataFrame
space

