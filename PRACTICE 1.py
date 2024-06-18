import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import maths

titanic_dataset=pd.read_csv(r'C:\Users\timok\Downloads\4aa5b471860321d7b47fd881898162b7-6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f/Titanic_dataset.csv')

#analysis
sns.countplot(x='Survived',data=titanic_dataset)
sns.countplot(x='Survived',hue='Sex',data=titanic_dataset)
sns.countplot(x='Survived',hue='Pclass',data=titanic_dataset)
titanic_dataset['Age'].plot.hist()
plt.show()
titanic_dataset['Fare'].plot.hist()
titanic_dataset.head()
sns.countplot(x='SibSp',data=titanic_dataset)
#data wrangling
titanic_dataset.isnull()
titanic_dataset.isnull().sum()
sns.heatmap(titanic_dataset.isnull(),yticklabels=False,cmap='viridis')
titanic_dataset.drop('Cabin', axis=1, inplace=True)
titanic_dataset.dropna(inplace=True)
sns.heatmap(titanic_dataset.isnull(),yticklabels=False,cmap='viridis')
em=pd.get_dummies(titanic_dataset['Embarked'], drop_first=True)
sex=pd.get_dummies(titanic_dataset['Sex'],drop_first=True)
titanic_dataset.info()
pcl=pd.get_dummies(titanic_dataset['Pclass'],drop_first=True)
titanic_dataset=pd.concat([titanic_dataset,em,sex,pcl],axis=1)
titanic_dataset.info()
titanic_dataset.head()
titanic_dataset.drop(['Embarked','Pclass','Sex','Ticket','Name','PassengerId'],axis=1,inplace=True)
titanic_dataset.head()
#train and testing data
import sklearn as skl
from sklearn.preprocessing import scaler
x=titanic_dataset.drop(["Survived"],axis=1)
y=titanic_dataset["Survived"]
from sklearn.model_selection import train_test_split
train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=10,random_state=1)
x_train
y_train
x_test
y_test
len(x_test)
x_train=np.array(x)
y_train=np.array(y)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
from sklearn.linear_model import LogisticRegression
lg=LogisticRegression()
pred=lg.predict(x_test)

