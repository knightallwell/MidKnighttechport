
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
import math
titanic_dataset=pd.read_csv(r'C:\Users\timok\Downloads\4aa5b471860321d7b47fd881898162b7-6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f/titanic_dataset.csv')
#analysis
sns.countplot(x='Survived', data=titanic_dataset)
sns.countplot(x='Survived', hue='Sex',data=titanic_dataset)
sns.countplot(x='Survived', hue='Pclass',data=titanic_dataset)
titanic_dataset['Age'].plot.hist()
titanic_dataset['Fare'].plot.hist()
sns.countplot(x='Survived', hue='Embarked', data=titanic_dataset)
titanic_dataset.isnull()
titanic_dataset.isnull().sum()
sns.heatmap(titanic_dataset.isnull(),yticklabels=False,cmap='viridis')
titanic_dataset.drop('Cabin', axis=1,inplace=True)

sns.heatmap(titanic_dataset.isnull(),yticklabels=False,cmap='viridis')
titanic_dataset.dropna(inplace=True)
sns.heatmap(titanic_dataset.isnull(),yticklabels=False,cmap='viridis')
Emb=pd.get_dummies(titanic_dataset['Embarked'],drop_first=True)
Emb.head(10)
SEX=pd.get_dummies(titanic_dataset['Sex'],drop_first=True)
SEX.head()
PCL=pd.get_dummies(titanic_dataset['Pclass'],drop_first=True)
PCL.head()
titanic_dataset=pd.concat([titanic_dataset,SEX,PCL,Emb,],axis=1)
titanic_dataset.drop(['Pclass','PassengerId','Ticket','Sex','Embarked'],axis=1,inplace=True)
titanic_dataset.info()
titanic_dataset.drop(['Name'],axis=1,inplace=True)
titanic_dataset.head
titanic_dataset=pd.get_dummies(titanic_dataset,drop_first=True)
titanic_dataset.info()
#test and train
y=titanic_dataset['Survived']
x= titanic_dataset.drop(["Survived"], axis=1)
y.head()
x.head()
titanic_dataset.head()
import sklearn as skl
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2,random_state=1) 
train_test_split
np.array(y_test)
np.array(x_test)
np.array(y_train)
np.array(x_train)
x_train
from sklearn.linear_model import LinearRegression
lgmodel= LinearRegression()
lgmodel.fit(x_train,y_train)
preds=lgmodel.predict(x_test)
from sklearn.metrics import classification_report
classification_report(y_train,preds)

