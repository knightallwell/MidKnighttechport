import pandas as pd
import  math
import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn as skl
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report as cfr
from sklearn.metrics import accuracy_score as asc
from sklearn.metrics import confusion_matrix as cmx
from sklearn.naive_bayes import MultinomialNB as mnb
#DATA SET
bc= pd.read_csv(r'C:\Users\timok\Downloads\archive (1)\breast-cancer.csv')
bc.head()
bc.isnull().sum()
bc.head()
 #test and train
target= bc['diagnosis']
 x=bc.drop('diagnosis', axis=1)
 sc= StandardScaler()
 en=LabelEncoder()
 y=en.fit_transform(target)
 y
 x=sc.fit_transform(x)
 x
 knn=KNeighborsClassifier(n_neighbors=3)
 train_test_split
 x_train,x_test,y_train,y_test=train_test_split(x,y, train_size=0.2, random_state=0)
 knn.fit(x_train,y_train)
 y_preds=knn.predict(x_test)
 y_preds
 cfr(y_test,y_preds)
 cmx(y_test,y_preds)
 asc(y_test,y_preds)
 
 
