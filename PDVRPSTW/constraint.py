import pandas as pd
import matplotlib.pyplot as plt
import random
from operator import itemgetter, attrgetter
centers = [[0, 96.2,  154.37142857]
 ,[1, 177.41176471,  95.26470588]
 ,[2, 264.73170732, 245.70731707]
 ,[ 3, 56.45714286, 275.14285714]
 ,[4, 196.25641026, 267.25641026]
 ,[5, 269.825     ,  52.5       ]
 ,[ 6, 40.36363636,  26.18181818]
 ,[7, 167.        , 158.        ]
 ,[ 8, 31.52941176, 202.20588235]
 ,[9, 253.90384615, 147.01923077]
 ,[10, 129.67346939, 234.44897959]
 ,[11, 112.9375    ,  51.625     ]
 ,[ 12, 44.03448276, 110.03448276]
 ,[13, 193.83333333,  28.06666667]]
def distance(a, b):
    x1, y1 = a[1], a[2]
    x2, y2 = b[1], b[2]
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist
node_info = pd.read_csv('large_scale_500_02.csv')
data = pd.DataFrame(node_info)
#data = data.drop(['id'], axis=1)
customers = []
for index in data.index:
    customer_info = list(data.loc[index].values[0:])
    customers.append(customer_info)
#print(len(customers))
limit = 150
clusters = []
load = []
for i in range(14):
    cluster = []
    temp = [limit, limit]
    clusters.append(cluster)
    load.append(temp)
# print(load)
# print(clusters)
for i in range(1, len(customers)):
    dist_sort = []
    for j in range(len(centers)):
        dist = distance(centers[j], customers[i])
        dist_sort.append([dist, j])
    dist_sort = sorted(dist_sort, key=itemgetter(0))
    #print(dist_sort)
    for k in range(len(dist_sort)):
        if load[dist_sort[k][1]][0] - customers[i][3] >= 0 and load[dist_sort[k][1]][1] - customers[i][4] >= 0:
            load[dist_sort[k][1]][0] -= customers[i][3]
            load[dist_sort[k][1]][1] -= customers[i][4]
            clusters[dist_sort[k][1]].append(customers[i][0])
            break

print(clusters)
is_d_ok = []
is_p_ok = []
for c in clusters:
    totalp = 0
    totald = 0
    for indi in c:
        totald += customers[indi][3]
        totalp += customers[indi][4]
    is_d_ok.append(totald)
    is_p_ok.append(totalp)
print(is_d_ok)
print(is_p_ok)


