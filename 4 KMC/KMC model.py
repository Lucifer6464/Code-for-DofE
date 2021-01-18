import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
# the .data if the features, this scales them down to the
# range of 0 - 1, this saves time in computations
data = scale(digits.data)
y = digits.target

# dynamic way in case the data is changed
# k = len(np.unique(y))

# or you can use this
k = 10
samples, features = data.shape

# this scores the algorithm


def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))


# amount of clusters
clf = KMeans(n_clusters=k, init="random", n_init=10)
# bench_k_means takes the parameters of classifier, name, data
bench_k_means(clf, "1", data)

