## sklearnのデータベースからセット持ってきて教師有学習, 決定木作成
## 今回はwineのデータセット.　　属性数13,　データ数178ヶ


import pandas as pd
import graphviz
import pydotplus

from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from IPython.display import Image


# データインポート
data= load_wine()
    # print("Dataset is below : \r\n{0}\r\n".format(data.DESCR))　:　データセットの詳細表示#




            ##　決定木の精度測定　##            

dataX = pd.DataFrame(data=data.data,columns=data.feature_names)   # 説明変数
dataY = pd.DataFrame(data=data.target)    # 目的変数
dataY = dataY.rename(columns={0: 'class'})
# dataY.head()
    # print(dataX.head())
    # print(dataY.head())





# データ分割（評価用データ＝3割）
X_train, X_test, Y_train, Y_test = train_test_split(dataX, dataY, test_size=0.5)
    #print("Train-DataX below : \r\n{0}\r\n".format(X_train))
    #print("Test-DataX below : \r\n{0}\r\n".format(X_test))
    #print("Train-DataY below : \r\n{0}\r\n".format(Y_train))
    #print("Test-DataY below : \r\n{0}\r\n".format(Y_test))


# モデル作成
clf = DecisionTreeClassifier(min_samples_split=5)
clf.fit(X_train,Y_train)




# 決定木の描画
export_graphviz(clf, out_file="tree.dot", feature_names=X_train.columns, class_names=["0","1","2"], filled=True, rounded=True)
graph = pydotplus.graph_from_dot_file(path="tree.dot")
graph.write_png('figure-decisionTree.png')
Image(graph.create_png())





# 精度
print('\r\nAccuracy of DecisionTree = ', clf.score(X_test,Y_test))

# 混同行列
df = pd.DataFrame(confusion_matrix(Y_test,clf.predict(X_test).reshape(-1,1)))
df = df.rename(columns={0: '予想(class_0)',1: '予想(class_1)',2: '予想(class_2)'}, index={0: '実際(class_0)',1: '実際(class_1)',2: '実際(class_2)'})
df




            ##　ランダムフォレストの精度　##            

## x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.5)

model = RandomForestClassifier()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

# 精度
print('\r\nAccuracy of RandomTree = ', accuracy_score(Y_pred, Y_test))