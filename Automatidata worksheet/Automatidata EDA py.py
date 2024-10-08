import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\allwe\Downloads\data set\archive\2017_Yellow_Taxi_Trip_Data (1).csv')
df.head()

df.info()
#The df has 7 integers, 8 float and 3 object, the datatime object need to be converted to datetime
df.describe()

df.value_counts()
#Both values are not the same because the trip_distance does not have a causal effect on the price
df.sort_values('trip_distance', ascending=False)
df.sort_values('total_amount',ascending=False)
#The short distance  has a relatively high amount promising that there are other factors that may affect the price other than distance 
dfs = df.groupby(['total_amount', 'trip_distance']).agg({'payment_type' : 'sum'}).reset_index()
dfs.sort_values('total_amount', ascending=False)
df_trip=df[df['payment_type']==2]
df_payment=df[df['payment_type']==1]
df_payment,
df['VendorID'].mean()
df['VendorID'].count()
df_trip

df.isnull().sum()

df['payment_type'].mean()
df[df['payment_type'] == 2].mean()
