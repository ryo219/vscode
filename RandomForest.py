from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
    
# データ読み込み
data = load_wine()
# データ分割（評価用データ＝3割）
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

# モデル作成
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 精度
print('Accuracy = ', accuracy_score(y_pred, y_test))