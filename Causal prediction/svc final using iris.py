import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.svm import SVR 
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

irs=pd.read_csv(r'C:\Users\timok\Downloads\DATA SCIENCE PRACTICE\suv_data.csv')
irs.tail()
irs.size
irs.shape
irs.count()

irs.isnull().sum()


#irs.Species.unique()
en=LabelEncoder()
y=irs['Purchased']
x=irs['EstimatedSalary']
x=en.fit_transform(x)
x
sns.scatterplot(x=x,y=y,data=irs)
train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
x_train
y_train.shape
x_test
y_test.shape
sv=SVR().fit(x_train,y_train)

x=irs.iloc[:,2].values
y=irs.iloc[:,3].values
sc=StandardScaler()