#参考サイト
#https://note.com/okonomiyaki011/n/nad38fb8c8544


from NeuralNetwork_moon import X_test, X_train
from sklearn.datasets import load_breast_cancer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mglearn

cancer = load_breast_cancer()

#print('Cancer data per-feature maxima: \n{}'.format(cancer.data.max(axis=0)))
# 入力特徴量　スケールがバラバラなので，このまま学習させると精度悪化．

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

mean_on_train = X_train.mean(axis=0)
std_on_train = X_train.std(axis=0)


X_train_scaled = (X_train - mean_on_train)/std_on_train
X_test_scaled = (X_test - mean_on_train)/std_on_train

mlp = MLPClassifier(max_iter=1000, random_state=0)      #max_iter : 繰り返し学習回数を増やす
mlp.fit(X_train_scaled, y_train)

print("訓練セットの精度: {:.3f}".format(mlp.score(X_train_scaled, y_train)))
print("テストセットの精度: {:.3f}".format(mlp.score(X_test_scaled, y_test)))


plt.figure(figsize=(30,5))
plt.imshow(mlp.coefs_[0], interpolation='none', cmap='viridis')
plt.yticks(range(30), cancer.feature_names)
plt.xlabel('Column in weight matrix')
plt.ylabel('Input feature')
plt.colorbar()
plt.show()