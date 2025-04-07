# from sklearn.cluster import MiniBatchKMeans, KMeans
# from sklearn.metrics.pairwise import pairwise_distances_argmin
# from sklearn.datasets import make_blobs
# import numpy as np
#
# # Load data in X
# batch_size = 45
# centers = [[1, 1], [-2, -1], [1, -2], [1, 9]]
# n_clusters = len(centers)
# X, labels_true = make_blobs(n_samples = 3000,
#                             centers = centers,
#                             cluster_std = 0.9)
#
# # perform the mini batch K-means
# mbk = MiniBatchKMeans(init ='k-means++', n_clusters = 4,
#                       batch_size = batch_size, n_init = 10,
#                       max_no_improvement = 10, verbose = 0)
#
# mbk.fit(X)
# mbk_means_cluster_centers = np.sort(mbk.cluster_centers_, axis = 0)
# mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
#
# # print the labels of each data
# print(mbk_means_labels)

import numpy as np
import time
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin
from multiprocessing import Pool


class MiniBatchKMeans:
    def __init__(self, k=10, batch_size=100, max_iters=10):
        self.k = k
        self.batch_size = batch_size
        self.max_iters = max_iters
        self.centroids = None

    def fit(self, data):
        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]
        print(f"Initial centroids: {data.shape[0]}")

        for _ in range(self.max_iters):
            batch = shuffle(data)[:self.batch_size]
            cluster_indices = pairwise_distances_argmin(batch, self.centroids)

            new_centroids = np.zeros_like(self.centroids)
            counts = np.zeros(self.k)

            for i in range(self.batch_size):
                new_centroids[cluster_indices[i]] += batch[i]
                counts[cluster_indices[i]] += 1

            for j in range(self.k):
                if counts[j] > 0:
                    self.centroids[j] = new_centroids[j] / counts[j]

    def predict(self, data):
        return pairwise_distances_argmin(data, self.centroids)


# Load MNIST dataset from txt files
def load_dataset(image_file, label_file):
    images = np.loadtxt(image_file)
    labels = np.loadtxt(label_file)
    return images, labels


def parallel_fit(data):
    model = MiniBatchKMeans(k=10, batch_size=100, max_iters=10)
    model.fit(data)


if __name__ == "__main__":
    image_file = "mnist-images.txt"  # Update with actual path
    label_file = "mnist-labels.txt"  # Update with actual path
    dataset, labels = load_dataset(image_file, label_file)

    k = 10
    batch_size = 100
    max_iters = 10

    model = MiniBatchKMeans(k, batch_size, max_iters)

    start = time.time()
    model.fit(dataset)
    model.predict(dataset)
    end = time.time()
    print(f"Sequential execution time: {end - start:.4f} seconds")

    start = time.time()
    with Pool(processes=4) as pool:
        pool.map(parallel_fit, np.array_split(dataset, 4))
    end = time.time()
    print(f"Parallel execution time: {end - start:.4f} seconds")
