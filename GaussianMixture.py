#混合正規分布

from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

# データ読み込み
data = load_iris()

# 分布の数(クラスタ数)設定
n_components = 3 

# 混合正規分布の最尤推定
model = GaussianMixture(n_components=n_components)
model.fit(data.data) 

# クラス予測
print(model.predict(data.data)) 

# 各正規分布のパラメータ 
print(model.means_) # 平均 
print(model.covariances_) # 分散