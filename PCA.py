#主成分分析

#今回は sklearnの irisデータを使用

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# データ読込み
dataset = load_iris()
features = dataset.data
targets = dataset.target

# PCA実行
model = PCA(n_components=4)             # irisデータでは特徴量は 0~4
model.fit(features)
yi = model.fit_transform(features)

# 寄与率
print('\nContribution rate: {0}'.format(model.explained_variance_ratio_))

# グラフ描画
plt.scatter(yi[:,0],yi[:,1])            #第 1/2 主成分についてplot
plt.title('principal component')
plt.xlabel('pc1')
plt.ylabel('pc2')
plt.show()