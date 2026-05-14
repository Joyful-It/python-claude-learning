from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import  LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#from sklearn.preprocessing import 
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd

A = pd.read_csv("c:/Project/python/machine-Learning/telco-churn-7k/telco_churn_7k.csv")
A['TotalCharges']=pd.to_numeric(A['TotalCharges'],errors='coerce')
A = A.drop('customerID', axis=1)#清洗数据，第一步读取，第二步将格式不对数据改正，
#第三步将不需要的数据删掉

y=A['Churn']
X=A.drop('Churn',axis=1)
X=pd.get_dummies(X,drop_first=True)
X=X.dropna()
y=y.loc[X.index]
print(X.shape)
print(X.head())
y=y.map({'Yes':1,'No':0})#将文字修改为0，1

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=30)
base_model=[
    ('lr',LogisticRegression(max_iter=5000,class_weight='balanced')),
    ('dt',DecisionTreeClassifier()),
    ('rf',RandomForestClassifier(n_estimators=200))
]
model=StackingClassifier(estimators=base_model,final_estimator=LogisticRegression())
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("zhun que lv :",accuracy_score(y_test,y_pred))
print(classification_report(y_test, y_pred))
