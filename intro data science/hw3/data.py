import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
np.random.seed(41)

def load_data(path):
    """get path of data in files and return the stored data"""
    data = pd.read_csv(path)
    return data


def adjust_labels(y):
    """adjust labels of season from {0,1,2,3} to {0,1}"""
    new_arr = y
    for i in range(len(new_arr)):
        if new_arr[i] == 1:
            new_arr[i] = 0
        elif new_arr[i] > 1:
            new_arr[i] = 1
    return new_arr
             
class StandardScaler:
    def __init__(self):
        """ object instantiation """
        self.mean = None
        self.std = None
    def fit(self, X):
        """ fit scaler by learning the mean and standard deviation per feature """
        self.mean = np.mean(X, axis = 0)
        self.std = np.std(X, axis = 0)
        return self    

    def transform(self, X):
        """ transform X by learned mean and standard deviation, and return it """
        return (X - self.mean) / self.std
    
    def fit_transform(self, X):
        """ fit scaler by learning the mean and standard deviation per feature, and then transform X """
        self.fit(X)
        return self.transform(X)
        


def add_noise(data):
    """
    :param data: dataset as np.array of shape (n, d) with n observations and d features
    :return: data + noise, where noise~N(0,0.0002^2)
    """
    noise = np.random.normal(loc=0, scale=0.0002, size=data.shape)
    return data + noise


def get_folds():
    """
    :return: sklearn KFold object that defines a specific partition to folds
    """
    return KFold(n_splits=5, shuffle=True, random_state=41)
