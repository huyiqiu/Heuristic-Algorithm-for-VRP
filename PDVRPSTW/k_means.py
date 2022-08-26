#使用k-means++对节点进行分类
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import math
node_info = pd.read_csv('c101_notw.csv')
data = pd.DataFrame(node_info)
cluster_num = 10
X = []
#D = []
for index in data.index:
    customer_info = list(data.loc[index].values[1:3])
    X.append(customer_info)
#     D.append(data.loc[index][3])
#cluster_num = math.ceil(sum(D)/150)

#print(X)
X.remove(X[0])
kmeans = KMeans(n_clusters=cluster_num, random_state=0).fit(X)
#print(kmeans.cluster_centers_)

cus_label = kmeans.labels_
# #print(len(cus_label))
#
#clusters
def clustering():
    clusters = []
    for i in range(cluster_num):
        clusters.append([])
    for i in range(1, len(X)):
        clusters[cus_label[i-1]].append(i)
    #print(clusters)
    return clusters
#
# c = clustering()
# print(c)