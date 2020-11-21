import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio) 
    test_indicies = shuffled[:test_set_size]
    train_indicies = shuffled[test_set_size:]
    return data.iloc[train_indicies], data.iloc[test_indicies]

if __name__ == '__main__':

    # Read the Data
    df = pd.read_csv('data.csv')
    train, test = data_split(df, 0.2)
    print(train)
    X_train = train[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreathe']].to_numpy()
    X_test = test[['fever', 'bodyPain', 'age', 'runnyNose', 'diffBreathe']].to_numpy()
    
    Y_train = train[['infectionProb']].to_numpy().reshape(2060 ,)
    Y_test = test[['infectionProb']].to_numpy().reshape(515 ,)

    clf = LogisticRegression()
    clf.fit(X_train, Y_train)s
    inputFeatures = [102, 1, -22, 1, 1]
    infProb = clf.predict_proba([inputFeatures])[0][1]
    
    file = open('model.pkl', 'wb')

    pickle.dump(clf, file)
    file.close()