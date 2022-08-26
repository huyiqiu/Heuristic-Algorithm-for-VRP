import random
import numpy as np
import copy
from read_file import customers_info
#from GA_PDVRPTW import GA
from initSolution import Vehicle
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号#有中文出现的情况，需要u'内容'

#route = GA()
#routepd = [120, 10, 65, 64, 138, 196, 18, 87, 37, 79, 140, 46, 93, 114, 158, 39, 154, 68, 151, 175, 76, 141, 56, 134, 107, 26, 199, 103, 96, 12, 123, 104, 112, 130, 66, 144, 13, 53, 180, 3, 189, 23, 84, 153, 160, 49, 16, 80, 129, 42, 170, 54, 148, 168, 187, 70, 43, 30, 34, 51, 99, 185, 32, 98, 15, 173, 200, 164, 171, 159, 179, 45, 17, 88, 69, 115, 78, 177, 137, 163, 59, 111, 195, 131, 110, 116, 55, 194, 161, 63, 94, 62, 162, 186, 83, 165, 19, 31, 145, 5, 21, 149, 156, 86, 178, 82, 97, 91, 106, 192, 184, 127, 150, 155, 128, 27, 2, 188, 35, 172, 181, 71, 81, 41, 29, 8, 60, 25, 40, 47, 132, 191, 121, 75, 67, 20, 92, 52, 24, 142, 125, 190, 198, 74, 7, 101, 139, 174, 4, 133, 124, 77, 182, 73, 126, 105, 152, 108, 109, 193, 169, 6, 38, 89, 44, 72, 57, 14, 85, 33, 102, 176, 36, 9, 122, 197, 118, 157, 11, 146, 95, 183, 136, 117, 147, 143, 119, 113, 135, 167, 28, 166, 58, 50, 48, 90, 61, 22, 100] #最优个体： [120, 10, 65, 64, 138, 196, 18, 87, 37, 79, 140, 46, 93, 114, 158, 39, 154, 68, 151, 175, 76, 141, 56, 134, 107, 26, 199, 103, 96, 12, 123, 104, 112, 130, 66, 144, 13, 53, 180, 3, 189, 23, 84, 153, 160, 49, 16, 80, 129, 42, 170, 54, 148, 168, 187, 70, 43, 30, 34, 51, 99, 185, 32, 98, 15, 173, 200, 164, 171, 159, 179, 45, 17, 88, 69, 115, 78, 177, 137, 163, 59, 111, 195, 131, 110, 116, 55, 194, 161, 63, 94, 62, 162, 186, 83, 165, 19, 31, 145, 5, 21, 149, 156, 86, 178, 82, 97, 91, 106, 192, 184, 127, 150, 155, 128, 27, 2, 188, 35, 172, 181, 71, 81, 41, 29, 8, 60, 25, 40, 47, 132, 191, 121, 75, 67, 20, 92, 52, 24, 142, 125, 190, 198, 74, 7, 101, 139, 174, 4, 133, 124, 77, 182, 73, 126, 105, 152, 108, 109, 193, 169, 6, 38, 89, 44, 72, 57, 14, 85, 33, 102, 176, 36, 9, 122, 197, 118, 157, 11, 146, 95, 183, 136, 117, 147, 143, 119, 113, 135, 167, 28, 166, 58, 50, 48, 90, 61, 22, 100]
#routepd = [69, 27, 154, 128, 174, 152, 156, 68, 181, 56, 149, 86, 6, 46, 163, 24, 131, 119, 63, 134, 48, 58, 166, 110, 151, 82, 88, 175, 74, 148, 64, 97, 71, 36, 65, 73, 180, 177, 49, 26, 200, 165, 19, 54, 34, 20, 32, 92, 184, 41, 193, 8, 83, 47, 11, 127, 179, 29, 195, 81, 153, 117, 112, 78, 98, 188, 118, 146, 173, 75, 197, 115, 161, 111, 123, 164, 50, 28, 35, 89, 191, 143, 18, 136, 91, 52, 5, 132, 9, 60, 185, 155, 61, 10, 84, 126, 194, 190, 44, 4, 93, 135, 140, 133, 94, 142, 125, 169, 178, 33, 196, 124, 101, 12, 145, 116, 53, 187, 25, 104, 107, 114, 171, 21, 167, 160, 147, 2, 158, 162, 40, 13, 157, 159, 90, 77, 199, 198, 130, 39, 182, 108, 121, 99, 51, 168, 122, 22, 55, 16, 85, 17, 139, 23, 67, 176, 129, 45, 183, 95, 170, 14, 189, 96, 186, 62, 137, 79, 105, 7, 120, 103, 109, 106, 31, 192, 150, 87, 138, 100, 30, 141, 37, 3, 43, 72, 80, 102, 172, 144, 59, 70, 15, 66, 1, 76, 38, 57, 42, 113]

#routepd = [13, 11, 7, 12, 9, 14, 4, 6, 8, 2, 15, 16, 3, 10, 5]
#routep = [6, 10, 16, 9, 5, 12, 7, 4, 15, 2, 3, 13, 14, 8, 11]
#routed = [7, 12, 5, 9, 10, 4, 16, 14, 6, 11, 8, 13, 3, 2, 15]
#50
routepd = [50, 18, 38, 42, 17, 31, 7, 23, 45, 14, 30, 3, 37, 43, 1, 15, 35, 28, 33, 10, 4, 24, 6, 46, 48, 44, 36, 27, 22, 39, 40, 13, 2, 21, 25, 41, 29, 11, 47, 8, 32, 20, 34, 19, 26, 49, 12, 9, 5, 16]
customers = customers_info()

def calculate_fitness_withPD(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        temp_rout = []
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take <= v.load:
                now_take += customers[i][2]
                temp_rout.append(i)
            else:
                break
        for j in temp_rout:
            if now_take - customers[j][2] + customers[j][3] <= v.load:
                v.rout.append(j)
                now_take = now_take - customers[j][2] + customers[j][3]
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for i in vehicles:
        i.calculate_cost()
        cost += i.totalcost
    fit = 1 / cost
    return vehicles, cost

def calculate_fitness_withP(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take < v.load:
                now_take += customers[i][2]
                v.rout.append(i)
            else:
                break
        v.rout.append(1)
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for i in vehicles:
        i.calculate_cost()
        cost += i.totalcost
    fit = 1 / cost
    return vehicles, cost

def calculate_fitness_withD(individual):
    vehicles = []
    temp = copy.deepcopy(individual)
    while len(temp) > 0:
        now_take = 0
        v = Vehicle()
        for i in temp:
            if customers[i][2] + now_take < v.load:
                now_take += customers[i][3]
                v.rout.append(i)
            else:
                break
        #v.rout.append(1)
        v.rout.append(0)
        vehicles.append(v)
        for i in v.rout:
            if i in temp:
                temp.remove(i)
    cost = 0
    for i in vehicles:
        i.calculate_cost()
        cost += i.totalcost
    fit = 1 / cost
    return vehicles, cost

vehicles_with_pd, cost_with_pd = calculate_fitness_withPD(routepd)
#vehicles_with_p, cost_with_p = calculate_fitness_withP(routep)
#vehicles_with_d, cost_with_d = calculate_fitness_withD(routed)

#vehicles_with_pd =[[0,6, 24, 27, 36, 46, 48, 56, 58, 63, 64, 65, 68, 69, 71, 73, 74, 82, 86, 88, 97, 110, 119, 128, 131, 134, 148, 149, 151, 152, 154, 156, 163, 166, 174, 175, 180, 181,0], [0,8, 11, 19, 20, 26, 29, 32, 34, 41, 47, 49, 54, 75, 78, 81, 83, 92, 98, 112, 115, 117, 118, 127, 146, 153, 165, 173, 177, 179, 184, 188, 193, 195, 197, 200,0], [0,4, 5, 9, 10, 18, 28, 33, 35, 44, 50, 52, 60, 61, 84, 89, 91, 93, 94, 111, 123, 124, 125, 126, 132, 133, 135, 136, 140, 142, 143, 155, 161, 164, 169, 178, 185, 190, 191, 194, 196,0], [0,2, 12, 13, 21, 22, 25, 39, 40, 51, 53, 55, 77, 90, 99, 101, 104, 107, 108, 114, 116, 121, 122, 130, 145, 147, 157, 158, 159, 160, 162, 167, 168, 171, 182, 187, 198, 199,0], [0,7, 14, 16, 17, 23, 31, 45, 62, 67, 79, 85, 87, 95, 96, 103, 105, 106, 109, 120, 129, 137, 138, 139, 150, 170, 176, 183, 186, 189, 192,0], [0,1, 3, 15, 30, 37, 38, 42, 43, 57, 59, 66, 70, 72, 76, 80, 100, 102, 113, 141, 144, 172,0]]

def print_info(vehicles):
    t = 0
    td = 0
    for vehicle in vehicles:
        print("路径：")
        print(vehicle.rout)
        print(vehicle.rout[0], end=" ")
        for i in range(1, len(vehicle.rout)):
            print("->", vehicle.rout[i], end=" ")
        vehicle.calculate_cost()
        t+=vehicle.totalcost
        td+=vehicle.totaldist
        print("行驶成本：", vehicle.travel_cost," 总成本：", vehicle.totalcost)
    print("配送总成本：", t, "总路程：", td)

def draw(dots, vehicles):
    plt.figure(figsize=(10,10))
    plt.xlim(0,30)
    plt.ylim(0,30)
    plt.plot(dots[0][0], dots[0][1], 'o', color = 'red')
    for i in range(1, len(dots)):
        if dots[i][2] == 0:
            plt.plot(dots[i][0], dots[i][1], '^', color='#0085c3')
        elif dots[i][3] == 0:
            plt.plot(dots[i][0], dots[i][1], 's', color='#0085c3')
        else:
            plt.plot(dots[i][0], dots[i][1], 'o', color='#0085c3')
    colors = ["blue", "green", "orange", "purple","yellow",'orange', 'pink']
    nc = 0
    for vehicle in vehicles:
        for i in range(len(vehicle.rout)-1):
            start = (customers[vehicle.rout[i]][0], customers[vehicle.rout[i+1]][0])
            end = (customers[vehicle.rout[i]][1], customers[vehicle.rout[i+1]][1])
            plt.plot(start, end, color=colors[nc])
        nc += 1
    plt.show()

draw(customers_info(), vehicles_with_pd)
print_info(vehicles_with_pd)

# draw(customers_info(), vehicles_with_p)
# print_info(vehicles_with_p)
#
# draw(customers_info(), vehicles_with_d)
# print_info(vehicles_with_d)
