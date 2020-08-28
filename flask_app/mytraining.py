import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


def data_split(data,ratio):
    np.random.seed(42)
    shuffled=np.random.permutation(len(data))
    test_set_size=int(len(data)*ratio)
    test_indicies=shuffled[:test_set_size]
    train_indicies=shuffled[test_set_size:]
    return data.iloc[train_indicies],data.iloc[test_indicies]

def model(inputfeature):
    df=pd.read_csv("/home/Kalashkalwani/mysite/data2.csv")
    train, test=data_split(df,0.2)
    x_train=train[['fever','bodypain','age','runnynose','diffBreadth']].to_numpy()
    x_test=test[['fever','bodypain','age','runnynose','diffBreadth']].to_numpy()
    y_train=train[['infectionprob']].to_numpy().reshape(8000,)
    y_test=test[['infectionprob']].to_numpy().reshape(1999,)
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    infprob = clf.predict_proba([inputfeature])[0][1]
    return infprob


