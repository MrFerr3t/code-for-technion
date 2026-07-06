import numpy as np
from statistics import mode
from abc import abstractmethod, ABC
from data import StandardScaler


class KNN(ABC):
    def __init__(self, k):
        """ object instantiation, save k and define a scaler object """
        self.k = k
        self.scaler = StandardScaler()
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        """ fit scaler and save X_train and y_train """
        self.X_train = self.scaler.fit_transform(X_train)
        self.y_train = y_train
        return self
    
    @abstractmethod
    def predict(self, X_test):
        """ predict labels for X_test and return predicted labels """

    def neighbours_indices(self, x):
        """ for a given point x, find indices of k closest points in the training set """
        distances = np.array([dist(x, y) for y in self.X_train])
        k_indices = np.argsort(distances)[:self.k]
        return k_indices


    @staticmethod
    def dist(x1, x2):
        """returns Euclidean distance between x1 and x2"""
        return np.sqrt(np.sum((a - b) ** 2 for a, b in zip(x1, x2)))

class ClassificationKNN(KNN):
    def __init__(self, k):
        """ object instantiation, parent class instantiation """
        super().__init__(k)

    def predict(self, X_test):
        """ predict labels for X_test and return predicted labels """
        return [(self.neighbours_indices(x)).mode for x in X_test]



