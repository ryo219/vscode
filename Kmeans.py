# k平均法
# iris で

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# データ読み込み
data = load_iris()

# クラスタ数設定
n_clusters = 3

# k-means実行
model = KMeans(n_clusters=n_clusters)
model.fit(data.data)

print(model.labels_) # 各データの所属クラスタ 
print(model.cluster_centers_) # クラスタ重心