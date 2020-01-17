from scipy.interpolate import lagrange
import pandas as pd
import numpy as np

order1 = pd.read_table('Data/missing_data.csv', sep=',', encoding='gbk')
order2 = pd.read_table('Data/ele_loss.csv', sep=',', encoding='gbk')
order3 = pd.read_table('Data/alarm.csv', sep=',', encoding='gbk')
print(order1)
order1['User1']
y1 = order1['User1']
print(y1)
y2 = order1['User2']
y3 = order1['User3']
y11 = y1[y1.notnull()]
y21 = y2[y2.notnull()]
y31 = y3[y3.notnull()]
Value1 = lagrange(y11.index, list(y11))
Value2 = lagrange(y21.index[0:5], list(y21)[0:5])
Value3 = lagrange(y31.index, list(y31))
Value4 = lagrange(y21.index[6:11],list(y21)[6:11])
Value5 = lagrange(y21.index[15:21],list(y21)[15:21])
Value6 = lagrange(y31.index[6:11],list(y31)[6:11])
Value7 = lagrange(y31.index[15:21],list(y31)[15:21])
print('当User1缺失为5和12时，拉格朗日插值:', Value1([5, 12]))
print('当User2缺失为3、10、19和20时，拉格朗日插值:', Value2([3]))
print('当User2缺失为10时，拉格朗日插值:',Value4([10]))
print('当User2缺失为19、20时，拉格朗日插值:',Value5([19,20]))
print('当User3缺失为4时，拉格朗日插值:', Value3([4]))
print('当User3缺失为7、10时，拉格朗日插值:', Value6([7, 10]))
print('当User3缺失为16时，拉格朗日插值:', Value7([16]))



print(order2)
print(order3)
print(order2.shape)
print(order3.shape)
order2['date'] = order2['date'].astype('str')
order3['date'] = order3['date'].astype('str')
order2['ID'] = order2['ID'].astype('str')
order3['ID'] = order3['ID'].astype('str')
order_detail = pd.merge(order2, order3, sort=True, how='outer')
print(order_detail)


def StandardScaler(data):
    data = (data - data.mean()) / data.std()
    return data


order4 = pd.read_excel('Data/model.xls')
print(order4)
order4['电量趋势下降指标'] = StandardScaler(order4['电量趋势下降指标'])
order4['线损指标'] = StandardScaler(order4['线损指标'])
order4['告警类指标'] = StandardScaler(order4['告警类指标'])

print(order4)
