from read_file import customers_info
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号#有中文出现的情况，需要u'内容'

def draw(dots):
    plt.figure(figsize=(10,10))
    plt.xlim(-1,30)
    plt.ylim(-1,30)
    plt.text(dots[0][0] + 1, dots[0][1] + 1, '配送中心', color='red', size=5)
    plt.plot(dots[0][0], dots[0][1], 'o', color = 'red')
    # plt.text(dots[1][0] + 1, dots[1][1] + 1, '回收检测中心', color='red', size=5)
    # plt.plot(dots[1][0], dots[1][1], 'o', color = 'yellow')
    for i in range(1, len(dots)):
        if dots[i][2] == 0:
            plt.plot(dots[i][0], dots[i][1], '^', color='#0085c3')
        elif dots[i][3]==0:
            plt.plot(dots[i][0], dots[i][1], 's', color = '#0085c3')
        else:
            plt.plot(dots[i][0], dots[i][1], 'o', color='#0085c3')
    plt.show()


draw(customers_info())