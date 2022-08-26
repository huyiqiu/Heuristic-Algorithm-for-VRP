from read_file import customers_info
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号#有中文出现的情况，需要u'内容'
centers = [[60.77777778,81.88888889],
 [ 5.33333333,40.55555556],
 [66.4,       57.1       ],
 [39.875,      9.375     ],
 [40.58333333,67.5       ],
 [89.44444444,31.66666667],
 [30.,        32.15384615],
 [19.625,     80.        ],
 [25.18181818,52.54545455],
 [48.72727273,34.54545455]]
def draw(dots):
    plt.figure(figsize=(10,10))
    # plt.xlim(0,30)
    # plt.ylim(0,30)
    plt.text(dots[0][1] + 1, dots[0][2] + 1, '配送中心', color='red', size=10)
    plt.plot(dots[0][1], dots[0][2], '.',markersize=8, color = 'red')
    for i in range(1, len(dots)):
        if dots[i][3] == 0:
            plt.plot(dots[i][1], dots[i][2], '^',markersize=4, color = '#0085c3')
        elif dots[i][4] == 0:
            plt.plot(dots[i][1], dots[i][2], 's',markersize=4, color = '#0085c3')
        else:
            plt.plot(dots[i][1], dots[i][2], '.', markersize=4, color='#0085c3')
    # for i in range(len(centers)):
    #     plt.plot(centers[i][0], centers[i][1], '.', color = 'green')
    plt.show()


draw(customers_info())