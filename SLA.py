#潜在意味解析 (Latent Semantic Analysis)

from sklearn.decomposition import TruncatedSVD

# カウントマトリクス
data = [[1, 0, 0, 0],
[1, 0, 0, 0],
[1, 1, 0, 0],
[0, 1, 0, 0],
[0, 0, 1, 1],
[0, 0, 1, 0],
[0, 0, 1, 1],
[0, 0, 0, 1]]

# 特異値分解
model = TruncatedSVD(n_components=2)
model.fit(data)

# 次元削減後のマトリクス
print(model.transform(data)) 

# 寄与率 
print(model.explained_variance_ratio_)
# 累積寄与率
print(sum(model.explained_variance_ratio_))

