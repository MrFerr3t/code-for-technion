import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(2)


def add_noise(data):
    """
    :param data: dataset as numpy array of shape (n, 2)
    :return: data + noise, where noise~N(0,0.00001^2)
    """
    noise = np.random.normal(loc=0, scale=1e-5, size=data.shape)
    return data + noise


def choose_initial_centroids(data, k):
    """
    :param data: dataset as numpy array of shape (n, 2)
    :param k: number of clusters
    :return: numpy array of k random items from dataset
    """
    n = data.shape[0]
    indices = np.random.choice(range(n), k, replace=False)
    return data[indices]


# ====================
def transform_data(df, features):
    """
    Performs the following transformations on df:
        - selecting relevant features
        - scaling
        - adding noise
    :param df: dataframe as was read from the original csv.
    :param features: list of 2 features from the dataframe
    :return: transformed data as numpy array of shape (n, 2)
    """
    data = pd.read_csv(path)
    
    transformed_data = np.array(data[features], dtype = float)
    min_val0 = min(data[features[0]])
    min_val1 = min(data[features[1]])
    max_val0 = max(data[features[0]])
    max_val1 = max(data[features[1]])
    transform_data[:, 0] = (transform_data[:, 0] - min_val0)/(max_val0 - min_val0)
    transform_data[:, 1] = (transform_data[:, 1] - min_val1)/(max_val1 - min_val1)
    add_noise(transformed_data)

    return transformed_data



def kmeans(data, k):
    """
    Running kmeans clustering algorithm.
    :param data: numpy array of shape (n, 2)
    :param k: desired number of cluster
    :return:
    * labels - numpy array of size n, where each entry is the predicted label (cluster number)
    * centroids - numpy array of shape (k, 2), centroid for each cluster.
    """

    centroids = choose_initial_centroids(data, k)
    labels = assign_to_clusters(data, centroids)
    prev_centroids = centroids
    centroids = recompute_centroids(data,labels,k)
    labels = assign_to_clusters(data, centroids)
    while(not np.array_equal(centroids,prev_centroids)):
        prev_centroids = centroids
        centroids = recompute_centroids(data,labels,k)
        labels = assign_to_clusters(data, centroids)


    return labels, centroids


def visualize_results(data, labels, centroids, path):
    """
    Visualizing results of the kmeans model, and saving the figure.
    :param data: data as numpy array of shape (n, 2)
    :param labels: the final labels of kmeans, as numpy array of size n
    :param centroids: the final centroids of kmeans, as numpy array of shape (k, 2)
    :param path: path to save the figure to.
    """


    for i in range(len(centroids)):
        current_cluster = []
        current_counter = 0
        for j in range(len(labels)):
            if (labels[j] == centroids[i]):
                current_cluster[current_counter] = data[j]
                current_counter += 1
        plt.scatter(*current_cluster.T)

    plt.savefig(path)
    plt.close('all')


def dist(x, y):
    """
    Euclidean distance between vectors x, y
    :param x: numpy array of size n
    :param y: numpy array of size n
    :return: the euclidean distance
    """
    distance = np.sqrt(np.sum(np.square(x - y)))
    return distance


def assign_to_clusters(data, centroids):
    """
    Assign each data point to a cluster based on current centroids
    :param data: data as numpy array of shape (n, 2)
    :param centroids: current centroids as numpy array of shape (k, 2)
    :return: numpy array of size n
    """
    labels = np.zeros(data.shape[0])
    for point in range(len(data)):
        min_val = dist(data[point],centroids[0])
        min_index = 0
        for i in range(len(centroids)):
            temp_val = dist(data[point],centroids[i])
            if(temp_val < min_val):
                min_val = temp_val
                min_index = i
        labels[point] = centroids[min_index]        
    return labels


def recompute_centroids(data, labels, k):
    """
    Recomputes new centroids based on the current assignment
    :param data: data as numpy array of shape (n, 2)
    :param labels: current assignments to clusters for each data point, as numpy array of size n
    :param k: number of clusters
    :return: numpy array of shape (k, 2)
    """
    centroids = np.shape(k, 2)
    for i in range(len(centroids)):
        sum_x = 0
        sum_y = 0
        point_counter = 0
        for j in range(len(labels)):
            if (labels[j] == centroids[i]):
                sum_x += data[j][0]
                sum_y += data[j][1]
                point_counter += 1
            
        centroids[i] = (sum_x / point_counter, sum_y / point_counter)
    return centroids
        


        
    

