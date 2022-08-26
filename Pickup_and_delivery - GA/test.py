# import pandas as pd
# import matplotlib.pyplot as plt
# import random
#
# # info = pd.read_csv('test_file.csv')
# # data=pd.DataFrame(info)
# # #print(data)
# # for i in data.index:
# #     a = data.loc[i].values[0:]
# #     print(a)
#
# import random
# import copy
# from read_file import customers_info
#
# customers = customers_info()
#
#
# def distance(a, b):
#     x1, y1 = a[0], a[1]
#     x2, y2 = b[0], b[1]
#     dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     return dist
#
# def rout_lenth(rout):
#     total = 0
#     for i in range(len(rout)-1):
#         total += distance(customers[rout[i]], customers[rout[i+1]])
#     total += distance(customers[rout[len(rout)-1]], customers[rout[0]])
#     return total
#
#
# class Vehicle():
#     def __init__(self):
#         self.startcost = 150
#         self.load = 250
#         self.cost_per_km = 8
#         self.speed = 40
#         self.rout = [0]
#         self.totalcost = 0
#         self.punish_coef = 10
#         self.starttime = 6
#
#     def calculate_cost(self):
#         #travel cost
#         travel_cost = self.cost_per_km * rout_lenth(self.rout)
#         #punish_cost
#         punish_cost = 0
#         h = self.starttime
#         temp = copy.deepcopy(self.rout)
#         for i in range(1, len(temp)):
#             h += distance(customers[temp[i]], customers[temp[i-1]]) / self.speed
#             if h < customers[temp[i]][4]:
#                 punish_cost += self.punish_coef * (customers[temp[i]][4] - h)
#             elif h > customers[temp[i]][5]:
#                 punish_cost += self.punish_coef * (h - customers[temp[i]][5])
#             else:
#                 punish_cost += 0
#             h += customers[temp[i]][6]
#         #calculate total cost
#         self.totalcost = self.startcost + punish_cost + travel_cost
#
#
# class Population():
#     def __init__(self, S, nodes_num):
#         self.S = S
#         self.nodes_num = nodes_num
#
#     def init_indi(self):
#         individual = list(range(1, self.nodes_num + 1))
#         random.shuffle(individual)
#         return individual
#
#     def init_pop(self):
#         self.pop = []
#         for i in range(self.S):
#             self.pop.append(self.init_indi())
#
# def calculate_fitness(individual):
#     vehicles = []
#     temp = copy.deepcopy(individual)
#     while len(temp) > 0:
#         now_take = 0
#         temp_rout = []
#         v = Vehicle()
#         for i in temp:
#             if customers[i][2] + now_take < v.load:
#                 now_take += customers[i][2]
#                 temp_rout.append(i)
#             else:
#                 break
#         for j in temp_rout:
#             if now_take - customers[j][2] + customers[j][3] < v.load:
#                 v.rout.append(j)
#                 now_take = now_take - customers[j][2] + customers[j][3]
#         v.rout.append(1)
#         v.rout.append(0)
#         vehicles.append(v)
#         for i in v.rout:
#             if i in temp:
#                 temp.remove(i)
#     cost = 0
#     for i in vehicles:
#         print(i.rout)
#         i.calculate_cost()
#         cost += i.totalcost
#     fit = 1/cost
#     return fit, cost
#
#
# a = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# a2 = [2,4,6,8,10,12,14,16,15,13,11,9,7,5,3]
# b = calculate_fitness(a)
# print(b)

a = [1,2,3,4,5]
b = sum(a)
#c = a/b
print(b)

