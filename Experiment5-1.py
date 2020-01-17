import pandas as pd

# 数据和标签分离
wine = pd.read_csv('Data\\wine.csv')
wine_target = wine['Class']
wine_data = wine.drop(labels='Class',axis=1)

# 数据分为训练集和测试集
from sklearn.model_selection import train_test_split
wine_data_train,wine_data_test,wine_target_train,wine_target_test= \
train_test_split(wine_data,wine_target)
print('将wine.csv的数据分为训练集和测试集')
print('wine数据集的测试集形状：',wine_data_test.shape)
print('wine数据集的训练集形状：',wine_data_train.shape)


from sklearn.preprocessing import MinMaxScaler  # 离差标准化
Scaler = MinMaxScaler().fit(wine_data_train)  # 生成规则
wine_data_trainScaler = Scaler.transform(wine_data_train)
wine_data_testScaler = Scaler.transform(wine_data_test)


# 进行PCA降维(降到10)
from sklearn.decomposition import PCA
pca_model = PCA(n_components=10).fit(wine_data_trainScaler)
wine_data_trainPca = pca_model.transform(wine_data_trainScaler)
wine_data_testPca = pca_model.transform(wine_data_testScaler)


# 构建聚类数目为3的K-Means模型
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3,random_state=123).fit(wine_data_trainScaler)

# 进行FMI评价
from sklearn.metrics import fowlkes_mallows_score
score = fowlkes_mallows_score(wine_target_train,kmeans.labels_)
print('FMI评价分值',score)

# 轮廓系数寻找最优
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
silhouetteScore = []

for i in range(2,11):
    kmeans = KMeans(n_clusters=i,random_state=123).fit(wine_data_trainPca)
    score = silhouette_score(wine_data_trainPca,kmeans.labels_)
    silhouetteScore.append(score)

#Calinski-Harabasz指数寻找最优
from sklearn.metrics import calinski_harabasz_score
calinskiarabaszScore = []

for i in range(2,11):
    kmeans = KMeans(n_clusters=i,random_state=123).fit(wine_data_trainPca)
    score = calinski_harabasz_score(wine_data_trainPca,kmeans.labels_)
    calinskiarabaszScore.append(score)


p1 = plt.figure(figsize=(10,6))
ax1 = p1.add_subplot(2,1,1)
ax2 = p1.add_subplot(2,1,2)

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.sca(ax1)
plt.plot(range(2,11),silhouetteScore,linewidth=1)
plt.title('silhouette分数')
plt.sca(ax2)
plt.plot(range(2,11),calinskiarabaszScore,linewidth=1)
plt.title('Calinski-Harabasz分数')

plt.show()
plt.savefig("轮廓系数折线图")

#SVM模型
from sklearn.svm import SVC
svm =SVC().fit(wine_data_trainScaler,wine_target_train)
wine_target_pre = svm.predict(wine_data_testScaler)

#检测评估
from sklearn.metrics import classification_report
print("使用SVM预测Wine数据的分类报告：\n",classification_report(wine_target_test,wine_target_pre))