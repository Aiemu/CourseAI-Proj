import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random

from sklearn.cluster import Birch
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
from sklearn import metrics

class KMeans():
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters

    # compute Euc distance
    def getEucDis(self, item):
        eucDis = np.sqrt(np.sum((self.core - item) ** 2, axis=1))
        return eucDis

    # return Euc distance and clustering with EucDis
    def clustering(self, item):
        eucDis = np.argmin(self.getEucDis(item))
        return eucDis

    # get model
    def fit(self, data):
        # set random cluster center
        self.core = np.array(random.sample(list(data), self.n_clusters))

        # get new cluster
        last = None
        while 1:
            now = [self.clustering(item) for item in data]

            # stop loop
            if now == last:
                self.new_cluster = now
                return

            for i in range(self.n_clusters):
                datapoints = data[np.where(np.array(now) == i)]
                self.core[i] = datapoints.mean(axis=0)

            last = now

    # show result
    def display(self, data):
        print('Calinski-Harabaz Index:', metrics.calinski_harabasz_score(data, self.new_cluster))
        print('Silhouette Coefficient:', metrics.silhouette_score(data, self.new_cluster, metric='euclidean'))
        plt.figure(figsize=(12,10))
        plt.title("Result of Clustering KMeans")
        plt.scatter(data[:, 0], data[:, 1], marker='o', c=self.new_cluster)
        plt.show()

if __name__ == "__main__":
    # load data
    path = "./data/clustering/Frogs_MFCCs.csv"
    dataset = pd.read_csv(path)
    
    attri_group = [
        ["MFCCs_ 2", "MFCCs_ 3", "MFCCs_ 4", "MFCCs_ 5"],
        ["MFCCs_18", "MFCCs_19", "MFCCs_20", "MFCCs_21", "MFCCs_22"]
        ]

    # change y: Family into num
    y = dataset['Family']
    y = y.replace("Bufonidae", 0).replace("Dendrobatidae", 1).replace("Hylidae", 2).replace("Leptodactylidae", 3)

    for group_idx in range(0, len(attri_group)):
        print("\n============Group %d============\n" % group_idx)
        data = dataset[attri_group[group_idx]]

        # reduce dime of dataset and get X
        print("PCA reducing dimension...\n")
        tsne = TSNE(learning_rate=100)
        tsne.fit_transform(data)
        data = pd.DataFrame(tsne.embedding_, index=data.index)
        X = data.values

        # compute silhouette_score and choose best k
        print("Computing silhouette_score to choose best k...\n")
        SilScore = []
        for k in range(2, 7):
            birch_tmp = Birch(n_clusters=k)
            SilScore.append(silhouette_score(data, birch_tmp.fit_predict(data, y=y)))
        k = SilScore.index(max(SilScore)) + 2

        # show silhouette_score-k image
        print("Displaying silhouette_score-k image...\n")
        plt.title("Silhouette Score of k")
        plt.xlabel('k')
        plt.ylabel('SilScore')
        plt.plot(range(2, 7), SilScore, 'o-')
        plt.show()

        print('Best Num of Clusters(k):', k)

        # reset k to 4(num of Families)
        k = 4
        print('Test Num of Clusters(k):', k, '\n')

        # clustering Birch
        print('Birch fitting...\n')
        bi = Birch(n_clusters=k)
        bi.fit(X)
        print('    Calinski-Harabaz Index:', metrics.calinski_harabasz_score(X, bi.labels_))
        print('    Silhouette Coefficient:', metrics.silhouette_score(X, bi.labels_, metric='euclidean'), '\n')

        # display result of Birch
        print("Displaying result of Birch...\n")
        plt.figure(figsize=(12,10))
        plt.title("Result of Clustering Birch")
        plt.scatter(X[:, 0], X[:, 1], marker='o', c=bi.labels_)
        plt.show()

        # clustering KMeans
        print("KMeans fitting...\n")
        km = KMeans(n_clusters=k)
        km.fit(X)

        # display result of KMeans
        print("Diaplaying result KMeans...\n")
        km.display(X)