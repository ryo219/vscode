#赤池情報量規準


import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# データ作成（sin関数）
X_size = 50

X = np.random.uniform(low=0, high=1.2, size=X_size)
X = np.sort(X)
Y = np.sin(X * 2 * np.pi) + np.random.normal(0, 0.5, X_size)

Max_M = 20  # 最大モデル次数
for M in range(1, Max_M+1):
    # 線形回帰モデル
    poly = PolynomialFeatures(M)    # M次多項式
    poly_X = poly.fit_transform(X.reshape(X_size, 1))
    model = LinearRegression()
    model.fit(poly_X, Y)
    pred_Y = model.predict(poly_X)
    pred_E = mean_squared_error(pred_Y, Y)  # 推定誤差

    # AIC
    AIC = X_size*np.log(pred_E/X_size) + 2*M    
    print([M, pred_E, AIC])

    # グラフ描画
    plt.scatter(X,Y)
    plt.plot(X,pred_Y,c='red')
    plt.show()