import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Reading the data using pandas
df = pd.read_csv('data.csv')
#Function for Train Test Splitting
def split_data(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indicies = shuffled[:test_set_size]
    train_indicies = shuffled[test_set_size:]
    return data.iloc[train_indicies], data.iloc[test_indicies]

train, test = split_data(df, 0.2)

X_train = train[['bloodPreasure', 'Age']].to_numpy()
X_test = test[['bloodPreasure', 'Age']].to_numpy()

Y_train = train[['disProb']].to_numpy().reshape(820, )
Y_test = test[['disProb']].to_numpy().reshape(204, )

clf = LogisticRegression()
clf.fit(X_train, Y_train)

inputFeatures = [120, 45]
infProb = clf.predict_proba([inputFeatures])[0][1]

file = open('model.pkl', 'wb')

pickle.dump(clf, file)
file.close()

print(infProb)