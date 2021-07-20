#独立成分分析

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA

np.random.seed(0)
t = np.linspace(0, 8, 1000)
s1 = np.sin(2 * t)                   # 信号1: 正弦波
s2 = np.sign(np.sin(3 * t))          # 信号2: 方形波
s3 = signal.sawtooth(2 * np.pi * t)  # 信号3: のこぎり波
S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # ノイズ付加
S /= S.std(axis=0)

# 混合信号
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # 混合行列A
X = np.dot(S, A)  # 観測信号

# ICA
ica = FastICA(n_components=3)
S_ = ica.fit_transform(X)   # 独立成分
A_ = ica.mixing_            # Aの推定値
# PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)

plt.figure()
models = [X, S, S_, H]
names = ['Observations','True Sources','Signals(ICA)','Signals(PCA)']
colors = ['r','b','g']
for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()