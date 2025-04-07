import numpy as np
from sklearn.cluster import MiniBatchKMeans

from sklearn.datasets import fetch_openml
X, y = fetch_openml("mnist_784", as_frame=False, return_X_y=True)

np.savetxt('mnist-images.txt', X, fmt='%d')
np.savetxt('mnist-labels.txt', y, fmt='%s')
model = MiniBatchKMeans(k=10, batch_size=100, max_iters=10)
model.fit(X)

