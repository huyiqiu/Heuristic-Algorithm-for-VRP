import pandas as pd
import matplotlib.pyplot as plt
import random

def customers_info():
    node_info = pd.read_csv('30_30.csv')
    data = pd.DataFrame(node_info)
    data = data.drop(['id'], axis=1)
    customers = []
    for index in data.index:
        customer_info = list(data.loc[index].values[0:])
        customers.append(customer_info)
    return customers

print(customers_info())


