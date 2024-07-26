import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import requests
from sklearn.metrics import classification_report as cfr



def plot_confusion_matrix(y, y_predict):
    from sklearn.metrics import confusion_matrix
    cm=confusion_matrix(y,y_predict)
    ax=plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax)
    ax.set_ylabel=('True labels')
    ax.set_xlabel=('Predicted labels')
    ax.set_title=('Confusion_matrix')
    ax.xaxis.set_ticklabels('Did not land', 'landed'); ax.yaxis('did not land','landed')
    plt.show()



url=  "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"

spacexl=pd.read_csv(r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv')
spacexl

url2='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv'
spacexll=pd.read_csv(r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_3.csv')
spacexll
y=spacexl['Class'].to_numpy()
x=spacexll
scl= preprocessing.StandardScaler()
x=scl.fit_transform(x)
train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y, random_state=0, test_size=0.2)

x.shape
y.shape
x_test.shape
y_test.shape


Parameter={'C':[0.01,0.1,1],
           'penalty':['l2'],
           'solver':['lbfgs']}

lr=LogisticRegression()
logreg_cv=GridSearchCV(lr,Parameter, cv=10)

logreg_cv.fit(x_train,y_train)

print('Best hypermeter found', logreg_cv.best_params_)
print('accuracy',logreg_cv.best_score_)
yhat=logreg_cv.predict(x_test)
cfr(y_test,yhat)

plot_confusion_matrix(y_test,yhat)

sv=SVC()
parameter={'kernel':('rbf','poly','sigmoid','linear'),
           'C':np.logspace(-3,3,5),
           'gamma':np.logspace(-3,3,5)}

svc_cv=GridSearchCV(sv,parameter, cv=10)
svc_cv.fit(x_train,y_train)
print('best hypermeter',svc_cv.best_params_)
print('accuracy score', svc_cv.best_score_)

ypred=svc_cv.predict(x_test)

cfr(y_test,ypred)

plot_confusion_matrix(y_test,ypred)

drc=DecisionTreeClassifier()

parameters={'criterion':['gini','entropy'],
            'splitter':['best','random'],
            'max_depth':[2*n for n in range(1,10)],
            'max_features':['auto','sqrt'],
            'min_samples_leaf':[1,2,4],
            'min_samples_split':[2,5,10]}

drc_cv=GridSearchCV(drc,parameters,cv=10)
drc_cv.fit(x_train,y_train)
print('Best hypermeters', drc_cv.best_params_)
print('Accuracy',drc_cv.best_score_)

ypreds=drc_cv.predict(x_test)

cfr(y_test,ypreds)

plot_confusion_matrix(y_test,ypreds)

knn=KNeighborsClassifier()

param_grid={'n_neighbors':[1,2,3,4,5,6,7,8,9,10],
            'algorithm':['auto','ball_tree','kd_tree','brute'],
            'p':[1,2]}

knn_cv=GridSearchCV(knn,param_grid,cv=10)
knn_cv.fit(x_train,y_train)
print('Best main hypermeters', knn_cv.best_params_)
print('Accuracy 1',knn_cv.best_score_)
y_preds=knn_cv.predict(x_test)

cfr(y_test,y_preds)

plot_confusion_matrix(y_test,y_preds)


Total_accuracy=({'logistic_reg':.8,'support vector':.8,'Decision Tree':1,'knearest n':.75})

import matplotlib.pyplot as plt

models = list(Total_accuracy.keys())
accuracies = list(Total_accuracy.values())

plt.figure(figsize=(10, 5))
plt.bar(models, accuracies, color='skyblue')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.ylim(0, 1)  # Assuming accuracy is between 0 and 1
plt.grid(axis='y')
plt.show()
