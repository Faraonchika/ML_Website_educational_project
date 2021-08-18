import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import os
import random



def i_cluster(file, n_clusters, affinity):
    X = pd.read_excel(file, 0)
    cluster = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage='average')
    cluster.fit_predict(X)

    pd.DataFrame(cluster.labels_).to_excel("static/i_cluster.xlsx")



    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=cluster.labels_, cmap='rainbow')
    plt.savefig('static/cluster_scatter.png')
    plt.close()

    linked = linkage(X, 'single')

    plt.figure(figsize=(10, 7))
    dendrogram(linked,
               orientation='top',
               distance_sort='descending',
               show_leaf_counts=True)


    plt.savefig('static/cluster_dendrogram.png')
    plt.close()

    r = str(random.randint(1, 10000000))

    return list(X.columns), 'static/cluster_dendrogram.png?' + r, 'static/cluster_scatter.png?' + r, "/static/i_cluster.xlsx?" + r
