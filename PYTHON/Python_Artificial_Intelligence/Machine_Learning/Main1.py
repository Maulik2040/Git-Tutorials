from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
features = iris.data
label = iris.target
clf = KNeighborsClassifier()
clf.fit(features, label)
preds = clf.predict([[1,2,3,10]])
print(preds)
print(iris.DESCR)