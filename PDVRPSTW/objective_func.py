import random
import copy
from read_file import customers_info
from Vhicles import Vehicle
customers = customers_info()

# def calculate_cost(individual):
#     vehicles = []
#     temp = copy.deepcopy(individual)
#     while len(temp) > 0:
#         now_take = 0
#         temp_rout = []
#         v = Vehicle()
#         for i in temp:
#             if customers[i][3] + now_take < v.load:
#                 now_take += customers[i][3]
#                 temp_rout.append(i)
#             else:
#                 break
#         for j in temp_rout:
#             v.rout.append(j)
#             if now_take - customers[j][3] + customers[j][4] <= v.load:
#                 now_take = now_take - customers[j][3] + customers[j][4]
#             else:
#                 break
#         v.rout.append(0)
#         vehicles.append(v)
#         for i in v.rout:
#             if i in temp:
#                 temp.remove(i)
#     cost = 0
#     for vehicle in vehicles:
#         vehicle.rout_cost()
#         cost += vehicle.totalcost
#     return cost

def calculate_cost(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        temp_rout = []
        v = Vehicle()
        for i in temp:
            if customers[i][3] + now_take <= v.load:
                now_take += customers[i][3]
                v.rout.append(i)
            else:
                break
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for vehicle in vehicles:
        vehicle.rout_cost()
        cost += vehicle.travel_dist
    return cost
