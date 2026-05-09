from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB

X,y=load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=20,random_state=30)

print("高斯朴素贝叶斯")
model1=GaussianNB()
model1.fit(X_train,y_train)

y_pred1=model1.predict(X_test)
print("zhun que lv",accuracy_score(y_test,y_pred1))

print("伯努利")
model2=BernoulliNB()
model2.fit(X_train,y_train)
y_pred2=model2.predict(X_test)
print("zhun que lv 2 :",accuracy_score(y_test,y_pred2))

print("多项式贝叶斯 ")
model3=MultinomialNB()
model3.fit(X_train,y_train)
y_pred3=model3.predict(X_test)
print("zhunquelv:",accuracy_score(y_test,y_pred3))

print("补集朴素贝叶斯")
model4=ComplementNB()
model4.fit(X_train,y_train)
y_pred4=model4.predict(X_test)
print("zhunquelv:",accuracy_score(y_test,y_pred4))