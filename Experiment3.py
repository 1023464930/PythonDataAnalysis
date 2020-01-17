import pandas as pd

order1 = pd.read_table('Data/Training_logInfo.csv', sep=',')
print('######Training_logInfo.csv######')
print(order1)
print("维度：", order1.ndim)
print("大小：", order1.shape)
print("占用内存：\n", order1.memory_usage())
print("describe:\n", order1.describe())
print('Idx频数统计结果前十为：')
print(order1['Idx'].value_counts()[0:10])
print('进行时间格式转换前的类型：', order1["LogInfo3"].dtype)
order1["LogInfo3"] = pd.to_datetime(order1["LogInfo3"])
print('进行时间格式转换后的类型：', order1["LogInfo3"].dtype)
print(order1["LogInfo3"])

dateIndex = pd.DatetimeIndex(order1["LogInfo3"])
print('转换后类型：', dateIndex.dtype)
periodIndex = pd.PeriodIndex(order1["LogInfo3"], freq='Y')
print(periodIndex)

userGroup = order1[['Idx', 'LogInfo3']].groupby(by='Idx')
print('每个用户的最晚登陆时间如下：')
print(userGroup.max())  #agg要使用哪个函数？
print('每个用户的最早登陆时间如下：')
print(userGroup.min())
print('每个用户的更新次数：')
print(userGroup.size())

time = pd.to_datetime(order1['Listinginfo1'])-pd.to_datetime(order1['LogInfo3'])
print(time)



print('\n######Training_Userupdate.csv######')
order2 = pd.read_table('Data/Training_Userupdate.csv', sep=',')
print(order2)
print(order2.describe())
time2 = pd.to_datetime(order2['ListingInfo1'])-pd.to_datetime(order2['UserupdateInfo2'])
print(time2)
userGroup2 = order2[['Idx', 'UserupdateInfo2']].groupby(by='Idx')
print('每个用户的最晚登陆时间如下：')
print(userGroup2.max())
print('每个用户的最早登陆时间如下：')
print(userGroup2.min())
print('每个用户的更新次数：')
print(userGroup2.size())

