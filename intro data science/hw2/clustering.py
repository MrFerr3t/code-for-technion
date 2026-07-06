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

    
    transformed_data = np.array(df[features], dtype = float)

    for i in range(transformed_data.shape[1]):
        min_val = np.min(transformed_data[:, i])
        max_val = np.max(transformed_data[:, i])
        transformed_data[:, i] = (transformed_data[:, i] - min_val) / (max_val - min_val)

    transformed_data =  add_noise(transformed_data)

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

    prev_centroids = np.zeros_like(centroids)
    centroids = recompute_centroids(data,labels,k)
    labels = assign_to_clusters(data, centroids)
    while not (np.array_equal(centroids,prev_centroids)):
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

    k = len(centroids)

    colors = plt.get_cmap('gist_rainbow', k)

    for i in range(k):
        cluster_points_x = []
        cluster_points_y = []
        for j in range(len(data)):
            if (labels[j] == i):
                cluster_points_x.append(data[j][0])
                cluster_points_y.append(data[j][1])
        plt.scatter(cluster_points_x, cluster_points_y, color=colors(i), label=f'Cluster {i}')

    plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='X', s=100, label='Centroids')

    plt.legend()
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
    labels = np.zeros(data.shape[0], dtype=int)
    for point in range(len(data)):
        min_val = dist(data[point], centroids[0])
        min_index = 0
        for i in range(1, len(centroids)):
            temp_val = dist(data[point],centroids[i])
            if(temp_val < min_val):
                min_val = temp_val
                min_index = i
        labels[point] = min_index
    return labels


def recompute_centroids(data, labels, k):
    """
    Recomputes new centroids based on the current assignment
    :param data: data as numpy array of shape (n, 2)
    :param labels: current assignments to clusters for each data point, as numpy array of size n
    :param k: number of clusters
    :return: numpy array of shape (k, 2)
    """
    centroids = np.zeros((k, 2))
    for i in range(k):
        sum_x = 0
        sum_y = 0
        point_counter = 0
        for j in range(len(labels)):
            if (labels[j] == i):
                sum_x += data[j][0]
                sum_y += data[j][1]
                point_counter += 1

        if (point_counter > 0):
            centroids[i] = [sum_x / point_counter, sum_y / point_counter]

    return centroids
        


        
    

