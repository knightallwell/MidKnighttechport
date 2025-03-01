#import your libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.ensemble import RandomForestClassifier 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#Data Load and transform 
df1= pd.read_csv(r'path.csv')
df1.columns
df1.head()
df1.drop(['Unnamed: 0'], axis=1, inplace=True)
df1.describe()


df2=pd.read_csv(r'path.csv')
df2.drop(columns=['Unnamed: 0'],axis=1, inplace=True,)
df2.head()
df2.describe()


df3=pd.read_csv(r'path.csv')
df3.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

df3.head()
df3.describe()


#Creating Data cleaning
#timestamp transformation
def Date_model (data:pd.DataFrame=None, column: str=None):
    dummy=data.copy()
    dummy[column]=pd.to_datetime(dummy[column], format='%Y-%m-%d %H:%M:%S')
    return dummy

df1=Date_model(df1,'timestamp')
df1.info()
df2=Date_model(df2,'timestamp')
df2.info()
df3=Date_model(df3, 'timestamp')
df3.info()

#timestamp transformation to hourly 
from datetime import datetime
def Date_hourly(data, column):
    dummy=data.copy()
    new_da= dummy[column].tolist()
    new_da= [i.strftime('%Y-%m-%d %H:00:00')for i in new_da]
    new_da=[datetime.strptime(i, '%Y-%m-%d %H:00:00') for i in new_da]
    dummy[column]=new_da
    return dummy

Date_hourly(df1, 'timestamp')
Date_hourly(df2,'timestamp')
Date_hourly(df3, 'timestamp')

df1.info()
df2.info()
df3.info()

#Data featureing

#Data grouping

df1_agg=df1.groupby(['timestamp','product_id']).agg({'quantity' : 'sum'}).reset_index()
df1_agg


df2_agg=df2.groupby(['timestamp','product_id']).agg({'estimated_stock_pct': 'mean'}).reset_index()
df2_agg

df3_agg=df3.groupby(['timestamp']).agg({'temperature': 'mean'}).reset_index()
df3_agg.info()

#Data_merge
merge_df=df2_agg.merge(df1_agg, on=['timestamp', 'product_id'], how='left')
merge_df.head()
merge_df=merge_df.merge(df3_agg, on='timestamp', how='left')
merge_df.isnull().sum()


#Additional data from df1
product_category=df1[['product_id','category']]
product_category=df1[['product_id','category']].drop_duplicates()
merge_df=merge_df.merge(product_sale, on="product_id", how='left')
merge_df

product_unit=df1[['product_id','unit_price']]
product_unit=df1[['product_id','unit_price']].drop_duplicates()

#addtional data merge
merge_df=merge_df.merge(product_unit, on="product_id", how="left")
merge_df

#null values conversion 
merge_df['quantity']=merge_df['quantity'].fillna(0)
merge_df['temperature']=merge_df['temperature'].fillna(0)
merge_df.isnull().sum()

#The allow the timestamp data to stand individually

merge_df['timestamp_to_day']=merge_df['timestamp'].dt.day
merge_df['timestamp_to_week']=merge_df['timestamp'].dt.dayofweek
merge_df['timestamp_to_hours']=merge_df['timestamp'].dt.hour
merge_df.drop(['timestamp'], axis=1, inplace=True)
merge_df.head()
merge_df=pd.get_dummies(merge_df, columns=['category'])
dummy_columns = merge_df.filter(like='category_').columns
merge_df[dummy_columns] = merge_df[dummy_columns].astype(int)

merge_df.info()
#drop Data not needed
merge_df.drop(['product_id'], inplace=True, axis=1)
merge_df.info()

#Data predictions
#determine the label data and the predictors
x=merge_df.drop(['column1'],axis=1)
y=merge_df['column1']
#encode the label data to avoid bias act of training & testing the model
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
y=label.fit_transform(y)

#split the model to training and testing models using train_test_split,
# determine the random state and test size
# fit the  model using the algorithm of your choice 
# and test the accuracy of the model

train_test_split
accuracy=[]
average_accuracy=0
for fold in range(0,10):
    x_train, x_test, y_train, y_test=train_test_split(x,y, random_state=42,test_size=.20)
    scalar= StandardScaler()
    
    x_train1=scalar.fit_transform(x_train)
    x_test1=scalar.transform(x_test)
    model= RandomForestClassifier(random_state=42)
    main_mod=model.fit(x_train1,y_train)
    y_pred= main_mod.predict(x_test1)
    acc=accuracy_score(y_test,y_pred)
    
    accuracy.append(acc)
    print(f'Fold {fold +1}:Accuracy={acc:.3f}')
print(f"Average Accuracy: {(sum(accuracy) / len(accuracy)):.2f}")

#Data visualization 

features = [i.split("__")[0] for i in x.columns]
importances = model.feature_importances_
indices = np.argsort(importances)

fig, ax = plt.subplots(figsize=(10, 20))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
