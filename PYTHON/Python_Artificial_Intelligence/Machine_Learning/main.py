import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets #linear_model
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
# Dataset for diabetes
diabetes = datasets.load_diabetes()


diabetes_x = diabetes.data[:, np.newaxis, 2]
print("diabetes_x")
print(diabetes_x)
diabetes_x_train = diabetes_x[:-30]
print("diabetes_x_train")
print(diabetes_x_train)
diabetes_x_test = diabetes_x[-20:]
print("diabetes_x_test")
print(diabetes_x_test)

diabetes_y_train = diabetes.target[:-30]
print("diabetes_y_train")
print(diabetes_y_train)
diabetes_y_test = diabetes.target[-20:]
print("diabetes_y_test")
print(diabetes_y_test)

model = linear_model.LinearRegression()

model.fit(diabetes_x_train, diabetes_y_train)

diabetes_y_predict = model.predict(diabetes_x_test)

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predict))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
# print(diabetes)
plt.scatter(diabetes_x_test, diabetes_y_test)
plt.plot(diabetes_x_test, diabetes_y_predict)
plt.show()