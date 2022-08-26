import copy
from read_file import customers_info
customers = customers_info()

#计算两点距离
def distance(a, b):
    x1, y1 = a[1], a[2]
    x2, y2 = b[1], b[2]
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist

#计算路径长度
def rout_lenth(rout):
    total = 0
    for i in range(len(rout)-1):
        total += distance(customers[rout[i]], customers[rout[i+1]])
    total += distance(customers[rout[len(rout)-1]], customers[rout[0]])
    return total

class Vehicle():
    def __init__(self):
        self.startcost = 600
        self.load = 200
        self.cost_per_km = 3
        self.speed = 50
        self.rout = [0]
        self.totalcost = 0
        #self.punish_coef = 0.5
        #self.starttime = 0

    #计算一条路径的成本
    def rout_cost(self):
        #travel cost
        travel_cost = self.cost_per_km * rout_lenth(self.rout)
        #punish_cost
        #punish_cost = 0
        #h = self.starttime
        #temp = copy.deepcopy(self.rout)
        # for i in range(1, len(temp)):
        #     h += distance(customers[temp[i]], customers[temp[i-1]])
        #     #
        #     if h < customers[temp[i]][4]:
        #         punish_cost += self.punish_coef * (customers[temp[i]][4] - h)
        #     elif h > customers[temp[i]][5]:
        #         punish_cost += self.punish_coef * (h - customers[temp[i]][5])
        #     else:
        #         punish_cost += 0
        #     h += customers[temp[i]][6]
        #calculate total cost
        #self.totalcost = self.startcost + punish_cost + travel_cost
        self.totalcost = self.startcost + travel_cost
        self.travel_cost = travel_cost
        #self.punish_cost = punish_cost
        self.travel_dist = rout_lenth(self.rout)
