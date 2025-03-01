#suv_prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
suv_prediction=pd.read_csv(r'C:/Users/timok/Downloads/suv_data.csv')
suv_prediction.head(10)
#analysis data
sns.countplot(x='Gender',data=suv_prediction)
sns.countplot(x='EstimatedSalary',hue='Age',data=suv_prediction)
sns.countplot(x='EstimatedSalary',data=suv_prediction)
suv_prediction['Age'].plot.hist()
plt.show()
sns.countplot(x='Gender',hue='EstimatedSalary',data=suv_prediction)
sns.countplot(x='Gender',hue='Purchased',data=suv_prediction)
#wrangling the data
suv_prediction.isnull()
suv_prediction.isnull().sum()
sns.heatmap(suv_prediction.isnull(),yticklabels=False,cmap="viridis")
#train and test
x=suv_prediction.iloc[:,[2,3]].values
y= suv_prediction.iloc[:,4].values
x
y
import sklearn as skl
from sklearn.model_selection import train_test_split
train_test_split
X_test,X_train,y_test,y_train =train_test_split(x,y, test_size=.25, random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)
from sklearn.linear_model import LogisticRegression
classifier= LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)*100

