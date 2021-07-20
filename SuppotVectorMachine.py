# サポートベクトルマシンを用いた分類
#　SVM : 教師有学習, 分類と回帰が可能　　教師データ少なくても高い汎化性能. 計算も早いし過学習も起こりにくい
# 仕組み : パーセプトロンに カーネル関数・マージン最大化 を加える　　(つまり次元増やしてクラス間距離最大化して無理やり線形分割する)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
        #クラスタリング用の等方性ガウス分布の塊を作製
        #引数は {サンプル数 / 特徴量 / クラスタのセンター数 / クラスタの標準偏差 /   }
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# データ生成
centers = [(-1, -1), (0.5, 0.5), (-1, 0.5), (0.5, -1), (0,0)]                              # centers : 引数()の個数=データの塊(class)
X, y = make_blobs(n_samples=1000, n_features=2, centers=centers, cluster_std=0.1)   # 特徴量 = 2, cluster_std : クラスタの標準偏差(ばらつき。でかいほど精度低下)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)            # 教師 / テストデータの分割
model = LinearSVC()

# 学習
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 分類精度
print(accuracy_score(y_pred, y_test))


# グラフ描画
plt.scatter(X_test[:,0], X_test[:,1], c=y_pred)     # scatter:散布図　　X_testの一列目をx軸に、二列目をy軸に設定
plt.show()