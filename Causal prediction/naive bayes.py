import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
import sklearn as skl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as en
from sklearn.naive_bayes import MultinomialNB 
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix



iris= pd.read_csv(r'c:\Users\timok\Downloads\DATA SCIENCE PRACTICE\archive\Iris.csv')
iris.head()
iris.isnull().sum()

x=iris.drop("Species", axis=1)
y=iris['Species']
y.unique()
y=y.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
y
train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2, random_state=0)
y_train
nb=MultinomialNB()
nb.fit(x_train,y_train)
ypreds=(nb.predict(x_test))
classification_report(ypreds,y_test)
confusion_matrix(ypreds,y_test)
accuracy_score(ypreds,y_test)








train_test_split
