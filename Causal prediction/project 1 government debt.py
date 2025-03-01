import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
government_debt=pd.read_csv(r'C:\Users\timok\Downloads\DATA SCIENCE PRACTICE\final draft.csv')
government_debt.head()
government_debt.isnull()
sns.heatmap(government_debt.isnull(),yticklabels=True,cmap="viridis")
import sklearn as skl
from sklearn.model_selection import train_test_split
train_test_split
y=government_debt.iloc[:,0]
x=government_debt.iloc[:,[1,2,3,4,5]]
x
y
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit_transform(x_train)
ss.fit_transform(x_test)
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.1, random_state=1)
from sklearn.linear_model import LinearRegression
lg=LinearRegression()
lg.fit(x_train,y_train)
x_train
x_test
y_train
y_test
pred=lg.predict(x_test)
pred
lg.score (x_test,y_test)


