import pandas as pd

winequality = pd.read_csv('Data\\winequality.csv',sep=';')
target = winequality['quality']   #标签
data = winequality.drop('quality',axis=1)   #数据

# 训练集和测试集
from sklearn.model_selection import train_test_split
data_train,data_test,target_train,target_test = train_test_split(data,target)

#构建模型
from sklearn.ensemble import GradientBoostingRegressor
GBR_quality = GradientBoostingRegressor().fit(data_train,target_train)
quality_pre = GBR_quality.predict(data_test)

#评估模型
from sklearn.metrics import mean_squared_error,median_absolute_error,explained_variance_score
print("梯度提升回归模型的均方误差：",mean_squared_error(target_test,quality_pre))
print("中值误差：",median_absolute_error(target_test,quality_pre))
print("可解释方差值：",explained_variance_score(target_test,quality_pre))

#展示
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(15,6))
plt.plot(range(target_test.shape[0]),target_test,linewidth=1.5,linestyle='-')
plt.plot(range(target_test.shape[0]),quality_pre,linewidth=1.5,linestyle='-.')
plt.legend(["真实值","预测值"])
plt.show()