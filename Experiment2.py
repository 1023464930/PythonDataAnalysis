import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data_load = np.load('Data/populations.npz', allow_pickle=True)
data = data_load['data']
feature_names = data_load['feature_names']
p = plt.figure(figsize=(19.2, 10.8))

ax1 = p.add_subplot(2, 5, 1)
plt.plot(range(20, 0, -1), data[:20, 1], linestyle='-', marker='o', c='r')
plt.xticks(range(20, 0, -1), data[range(0, 20, 1), 0], rotation=45)
plt.ylabel('年末总人口(万人)')

ax2 = p.add_subplot(2, 5, 2)
plt.plot(range(20, 0, -1), data[:20, 2]/data[:20, 3], linestyle='-', marker='o', c='r')
plt.plot(range(20, 0, -1), data[:20, 4]/data[:20, 5], linestyle='-', marker='*', c='b')
plt.legend(['男女人口比例（男性/女性）', '城乡人口比例（城镇/乡村）'])
plt.xticks(range(20, 0, -1), data[range(0, 20, 1), 0], rotation=45)

ax3 = p.add_subplot(2, 5, 3)
x = range(20, 0, -1)
plt.bar(x, data[:20, 2], width=0.3)
plt.bar([i + 0.3 for i in x], data[:20, 3], width=0.3)
plt.legend(['男性人口', '女性人口'])
plt.xticks([i + 0.1 for i in x], data[range(0, 20, 1), 0], rotation=45)

ax4 = p.add_subplot(2, 5, 4)
plt.bar(x, data[:20, 4], width=0.3)
plt.bar([i + 0.3 for i in x], data[:20, 5], width=0.3)
plt.legend(['城镇人口', '乡村人口'])
plt.xticks([i + 0.1 for i in x], data[range(0, 20, 1), 0], rotation=45)

ax5 = p.add_subplot(2, 5, 6)
label = ['男性', '女性']
explode = [0.01, 0.01]
plt.pie(data[0, 2:4], explode=explode, labels=label, autopct='%1.1f%%')
print(data[0, 2:3])
plt.title('2015年男女人口比例饼图')

ax6 = p.add_subplot(2, 5, 7)
label = ['男性', '女性']
explode = [0.01, 0.01]
plt.pie(data[19, 2:4], explode=explode, labels=label, autopct='%1.1f%%')
print(data[19, 2:3])
plt.title('1996年男女人口比例饼图')

ax7 = p.add_subplot(2, 5, 8)
label = ['城镇人口', '乡村人口']
explode = [0.01, 0.01]
plt.pie(data[0, 4:6], explode=explode, labels=label, autopct='%1.1f%%')
print(data[0, 4:6])
plt.title('2015年城乡人口比例饼图')

ax8 = p.add_subplot(2, 5, 9)
label = ['城镇人口', '乡村人口']
explode = [0.01, 0.01]
plt.pie(data[19, 4:6], explode=explode, labels=label, autopct='%1.1f%%')
print(data[19, 4:6])
plt.title('1996年城乡人口比例饼图')

ax9 = p.add_subplot(2, 5, 5)
label = ['男性', '女性']
number = (data[:20, 2], data[:20, 3])
plt.boxplot(number, notch=True, labels=label, meanline=True)
plt.title('1996-2015年男女人口箱线图')

ax10 = p.add_subplot(2, 5, 10)
label = ['城镇人口', '乡村人口']
number = (data[:20, 4], data[:20, 5])
plt.boxplot(number, notch=True, labels=label, meanline=True)
plt.title('1996-2015年城乡箱线图')

plt.savefig('Experiment2.png')
print(data_load['feature_names'])
print(data[range(0, 20)])
plt.show()
