import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
Titanic_data= pd.read_csv(r'C:\Users\timok\Downloads\4aa5b471860321d7b47fd881898162b7-6907bb3a38bfbb6fccf3a8b1edfb90e39714d14f\titanic_dataset.csv')
print(Titanic_data.head(10))
##Data analysis
#analysis how many survivals in the ship
sns.countplot(x="Survived",data=Titanic_data)
plt.show()
sns.countplot(x="Survived",hue="Sex", data=Titanic_data)
plt.show()
sns.countplot(x="Survived",hue="Pclass", data=Titanic_data)
plt.show()
Titanic_data["Age"].plot.hist()
plt.show()
Titanic_data.info()
Titanic_data["Fare"].plot.hist()
sns.countplot(x="SibSp",data=Titanic_data)
##data wrangling
Titanic_data.isnull()
Titanic_data.isnull().sum()
sns.heatmap(Titanic_data.isnull(), yticklabels=False, cmap="viridis")
sns.boxplot(x='Pclass',y='Age',data=Titanic_data)
Titanic_data.drop("Cabin", axis=1, inplace=True)
Titanic_data.head(5)
Titanic_data.dropna(inplace=True)
sns.heatmap(Titanic_data.isnull(),yticklabels=False)
Titanic_data.isnull().sum()
sex=pd.get_dummies(Titanic_data["Sex"], drop_first=True)
sex.head()
embark=pd.get_dummies(Titanic_data["Embarked"], drop_first=True)
embark.head(5)
plc=pd.get_dummies(Titanic_data["Pclass"], drop_first=True)
plc.head(5)
Titanic_data=pd.concat([Titanic_data,sex,embark,plc],axis=1)
Titanic_data.head(10)
Titanic_data.drop(['Sex','Embarked','PassengerId','Ticket'],axis=1,inplace=True)
Titanic_data.head(10)
Titanic_data.drop(['Name','Pclass'],axis=1,inplace=True)
Titanic_data.head(5)
#training and testing 
#train
 import sklearn as skl
 x= Titanic_data.drop(['Survived'], axis=1) 
 y= Titanic_data["Survived"]
 
 from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=1)
#X_train=np.array(Titanic_data)
y_train=np.array(Titanic_data["Survived"])
X_test=np.array(Titanic_data)
y_test=np.array(Titanic_data)
X_train
y_train
y_test
X_test
len(X_test)
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
prediction=logmodel.predict(X_test)
prediction=logmodel.predict(y_test)
from sklearn.metrics import classification_report 
classification_report(y_train,prediction)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_train,prediction)
from sklearn.metrics import accuracy_score
accuracy_score (y_train,prediction)

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
import sklearn as skl
from sklearn.model_selection import train_test_split
X_test,X_train,y_test,y_train = train_test_split( x,y, test_size=.3, random_state=10)
X_test