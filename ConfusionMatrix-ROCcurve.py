#混合行列 ・ ROC曲線


from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score 

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# データ読込み
data = load_breast_cancer()
X = data.data
y = 1 - data.target  # ラベルの0と1を反転
X = X[:, :10]

# ロジスティック回帰
model_lor = LogisticRegression()
model_lor.fit(X, y)
y_pred = model_lor.predict(X)

# 混同行列
cm = confusion_matrix(y, y_pred)
print('\nConfusion Matrix')
print(cm)

# 正解率，適合率，再現率
Acc = accuracy_score(y, y_pred)
Pre = precision_score(y, y_pred)
Rec = recall_score(y, y_pred)
Fsc = f1_score(y, y_pred)

print('\nAccuracy, Precision, Recall, F-score')
print([Acc,Pre,Rec,Fsc])


        #以下, ROC曲線描写
probas = model_lor.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

fig, ax = plt.subplots()
ax.step(fpr, tpr, 'gray')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
plt.grid(True)
ax.grid(color='lightgray')
plt.show()

# AUC
roc_auc_score(y, probas[:, 1])