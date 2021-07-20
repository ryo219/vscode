#雑な回帰
#適当な X データセットをsklearnの回帰モデルに掛けて Y-pred を算出
#用意した Y との比較


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



X = [[10.0], [8.0], [13.0], [9.0], [11.0], [14.0], [6.0], [4.0], [12.0], [7.0], [5.0]]
Y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
model = LinearRegression()      # sklearn から持ってきた謎の回帰モデル作成
model.fit(X, Y)                 # データ Xを上で作成したモデルに入れる ⇒ X の回帰モデルに対応する Y の値を出しとく. 二行前のは x-y対応ではない！


print('a =', model.intercept_)      #　切片
print('b =', model.coef_)           #　傾き

#x=1, 2, 3 ... に対する予測結果 (を値として格納)
Y_pred = model.predict([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
np.set_printoptions(precision=2, floatmode='fixed')
print('Reg_Y =', Y_pred)
print('True_Y =', Y)



# グラフ描写
plt.scatter(X, Y)
[X_min, X_max] = min(X), max(X)
X_est = np.arange(X_min[0], X_max[0])
Y_est = model.intercept_ + model.coef_[0]*X_est
plt.plot(X_est, Y_est)
plt.show()