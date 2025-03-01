#import your libraries


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.ensemble import RandomForestClassifier 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae

#Data importation 
sale= pd.read_csv(r'https://cdn.theforage.com/vinternships/companyassets/e6nrxEAa6MHFh3Jmw/DCGoJxzfdJHirTYGe/1652212400513/sales.csv')
sale.columns
sale.head()
sale.drop(['Unnamed: 0'], axis=1, inplace=True)
sale.describe()


temp_df=pd.read_csv(r'https://cdn.theforage.com/vinternships/companyassets/e6nrxEAa6MHFh3Jmw/DCGoJxzfdJHirTYGe/1652212467098/sensor_storage_temperature.csv')
temp_df.drop(columns=['Unnamed: 0'],axis=1, inplace=True,)
temp_df.head()
temp_df.describe()


stock_df=pd.read_csv(r'https://cdn.theforage.com/vinternships/companyassets/e6nrxEAa6MHFh3Jmw/DCGoJxzfdJHirTYGe/1652212438184/sensor_stock_levels.csv')
stock_df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)

stock_df.head()
stock_df.describe()


#Creating Dummy for the Date
def Date_model (data:pd.DataFrame=None, column: str=None):
    dummy=data.copy()
    dummy[column]=pd.to_datetime(dummy[column], format='%Y-%m-%d %H:%M:%S')
    return dummy

sale=Date_model(sale,'timestamp')
sale.info()
temp_df=Date_model(temp_df,'timestamp')
temp_df.info()
stock_df=Date_model(stock_df, 'timestamp')
stock_df.info()
from datetime import datetime
#Data featureing
def Date_hourly(data, column):
    dummy=data.copy()
    new_da= dummy[column].tolist()
    new_da= [i.strftime('%Y-%m-%d %H:00:00')for i in new_da]
    new_da=[datetime.strptime(i, '%Y-%m-%d %H:00:00') for i in new_da]
    dummy[column]=new_da
    return dummy

Date_hourly(sale, 'timestamp')
Date_hourly(stock_df,'timestamp')
Date_hourly(temp_df, 'timestamp')

sale.info()
stock_df.info()
temp_df.info()

sale_agg=sale.groupby(['timestamp','product_id']).agg({'quantity' : 'sum'}).reset_index()
sale_agg


stock_agg=stock_df.groupby(['timestamp','product_id']).agg({'estimated_stock_pct': 'mean'}).reset_index()
stock_agg

temp_agg=temp_df.groupby(['timestamp']).agg({'temperature': 'mean'}).reset_index()
temp_agg.info()

merge_df=stock_agg.merge(sale_agg, on=['timestamp', 'product_id'], how='left')
merge_df.head()
merge_df=merge_df.merge(temp_agg, on='timestamp', how='left')
merge_df.isnull().sum()



product_sale=sale[['product_id','category']]
product_sale=sale[['product_id','category']].drop_duplicates()
merge_df=merge_df.merge(product_sale, on="product_id", how='left')
merge_df

product_unit=sale[['product_id','unit_price']]
product_unit=sale[['product_id','unit_price']].drop_duplicates()

merge_df=merge_df.merge(product_unit, on="product_id", how="left")
merge_df

merge_df['quantity']=merge_df['quantity'].fillna(0)
merge_df['temperature']=merge_df['temperature'].fillna(0)
merge_df.isnull().sum()

merge_df['timestamp_to_day']=merge_df['timestamp'].dt.day
merge_df['timestamp_to_week']=merge_df['timestamp'].dt.dayofweek
merge_df['timestamp_to_hours']=merge_df['timestamp'].dt.hour
merge_df.drop(['timestamp'], axis=1, inplace=True)
merge_df.head()
merge_df=pd.get_dummies(merge_df, columns=['category'])
dummy_columns = merge_df.filter(like='category_').columns
merge_df[dummy_columns] = merge_df[dummy_columns].astype(int)

merge_df.info()

merge_df.drop(['product_id'], inplace=True, axis=1)
merge_df.info()

x=merge_df.drop(['estimated_stock_pct'],axis=1)
y=merge_df['estimated_stock_pct']
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
y=label.fit_transform(y)

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

features = [i.split("__")[0] for i in x.columns]
importances = model.feature_importances_
indices = np.argsort(importances)

fig, ax = plt.subplots(figsize=(10, 20))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
