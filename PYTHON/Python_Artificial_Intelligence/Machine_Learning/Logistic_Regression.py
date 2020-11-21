# Train a logistic regression to predict flower iris virginca or not 
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()
feature = iris.data
label = iris.target
# print(iris['data'])
# print(iris['target'])
# print(iris['DESCR'])
x = iris['data'][:, 3:]
y = (iris['target'] == 2).astype(np.int)
clf = LogisticRegression()
clf.fit(x,y)
example = clf.predict([[2.6]])
print(example)
x_new = np.linspace(0, 3, 1000).reshape(-1,1)
y_prob = clf.predict_proba(x_new)
plt.plot(x_new, y_prob[:,1], "g-", label='virginica')
plt.show()
# print(x)
# print(y)