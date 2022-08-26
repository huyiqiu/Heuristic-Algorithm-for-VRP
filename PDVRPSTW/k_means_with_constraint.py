# -*- coding: utf-8 -*-
import random
import copy
import math
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
node_info = pd.read_csv('large_scale_500_02.csv')
data = pd.DataFrame(node_info)
X = []
D = []
P = []
for index in data.index:
    customer_info = list(data.loc[index].values[1:3])
    X.append(customer_info)
    D.append(data.loc[index][3])
    P.append(data.loc[index][4])
#print(X)
X.remove(X[0])
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
print(D)
print(P)
def calDistance(centers, nodes):
    '''
    计算节点间距离
    输入：centers-中心，nodes-节点；
    输出：距离矩阵-dis_matrix
    '''
    dis_matrix = pd.DataFrame(data=None, columns=range(len(centers)), index=range(len(nodes)))
    for i in range(len(nodes)):
        xi, yi = nodes[i][0], nodes[i][1]
        for j in range(len(centers)):
            xj, yj = centers[j][0], centers[j][1]
            dis_matrix.iloc[i, j] = round(math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2), 2)

    return dis_matrix


def scatter_diagram(clusters, nodes):
    '''
    #画路径图
    输入：nodes-节点坐标；
    输出：散点图
    '''
    for cluster in clusters:
        x, y = [], []
        for Coordinate in cluster:
            x.append(Coordinate[0])
            y.append(Coordinate[1])
        plt.scatter(x, y, alpha=0.8, marker='.', s=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def distribute(center, nodes, K, demand, pickup, d_limit):
    '''
    将节节点分给最近的中心
    输入：center-中心,nodes-节点,K-类数量,demand-需求,d_limit-一个簇的满足需求的能力
    输出：新的簇-clusters，簇的需求-clusters_d
    '''
    clusters = [[] for i in range(K)]  # 簇
    label = [None for i in range(len(nodes))]
    clusters_d = [0 for i in range(K)]  # 簇需求
    clusters_p = [0 for i in range(K)]
    dis_matrix = calDistance(center, nodes).astype('float64')

    for i in range(len(dis_matrix)):
        row, col = dis_matrix.stack().idxmin()
        node = nodes[row]
        j = 1
        while clusters_d[col] + demand[row] > d_limit:  # 检验约束
            if j < K:
                j += 1
                dis_matrix.loc[row, col] = math.pow(10, 10)
                col = dis_matrix.loc[row, :].idxmin()
            else:  # 所有类都不满足需求量约束
                print("K较小")
                scatter_diagram(clusters, nodes)
                return None

        # 满足约束正常分配
        clusters[col].append(node)
        label[row] = col
        clusters_d[col] += demand[row]
        dis_matrix.loc[row, :] = math.pow(10, 10)

    return clusters, clusters_d, label


def cal_center(clusters):
    '''
    计算簇的中心
    输入：clusters-类坐标；
    输出：簇中心-new_center
    '''
    new_center = []
    for cluster in clusters:
        x, y = [], []
        for Coordinate in cluster:
            x.append(Coordinate[0])
            y.append(Coordinate[1])
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        new_center.append((round(x_mean, 2), round(y_mean, 2)))

    return new_center

# 参数
d_limit = 150  # 一个区的约束
demand = copy.deepcopy(D)
pickup = copy.deepcopy(P)
print(sum(demand))
print(sum(pickup))
K = max(math.ceil(sum(demand) / d_limit), math.ceil(sum(pickup) / d_limit)) # 簇的最小边界
print(K)
def k_clustering():
    # 输入数据
    nodes = X

    #scatter_diagram([list(nodes)], nodes)  # 初始位置分布图

    # 历史最优参数
    best_s = -1
    best_center = 0
    best_clusters = 0
    best_labels = 0
    best_clusters_d = 0

    for n in range(20):  # 多次遍历，kmeans对初始解敏感
        # 初始化随机生成簇中心
        index = random.sample(list(range(len(nodes))), K)
        new_center = [nodes[i] for i in index]
        i = 1
        center_list = []
        while True:
            # 节点——> 簇
            center = new_center.copy()
            center_list.append(center)  # 保留中心，避免出现A生成B，B生成C，C有生成A的情况
            clusters, cluster_d, label = distribute(center, nodes, K, demand, pickup, d_limit)
            new_center = cal_center(clusters)
            if (center == new_center) | (new_center in center_list):
                break
            i += 1

        s = silhouette_score(nodes, label, metric='euclidean')  # 计算轮廓系数，聚类的评价指标
        #scatter_diagram(clusters,nodes)#当前最优图

        if best_s < s:
            best_s = s
            best_clusters_d = cluster_d
            best_center = center.copy()
            best_clusters = clusters.copy()
            best_labels = label.copy()

    #scatter_diagram(best_clusters, nodes)  # 历史最优图
    #print("各类需求量：",best_clusters_d)
    #print(best_clusters)
    print(best_labels)
    return best_labels

cus_label = k_clustering()
#print(len(cus_label))

#clusters
def clustering():
    clusters = []
    for i in range(0,K):
        clusters.append([])
    for i in range(1, len(X)):
        clusters[cus_label[i-1]].append(i)
    #print(clusters)
    return clusters

print(clustering())
