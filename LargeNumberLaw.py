# 大数の法則
# コイントスしたときの表/裏の比率の収束を見る

import numpy as np
import random
import matplotlib.pyplot as plt

numFlips = [100, 1000]    # コイン投げ回数
numTrials = 10000         # 試行回数

# コイン投げ 1回
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(numFlips)

# コイン投げ×試行回数
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = np.std(fracHeads)
    return (fracHeads, mean, sd)

def labelPlot(numFlips, numTrials, mean, sd):
    plt.title(str(numTrials) + ' trials of ' + str(numFlips) + ' flips each')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Trials')
    plt.annotate('Mean = ' + str(round(mean, 4))\
                   + '\nSD = ' + str(round(sd, 4)), size='x-large',
                   xycoords = 'axes fraction', xy = (0.67, 0.5))

# グラフ描画
val1, mean1, sd1 = flipSim(numFlips[0], numTrials)

plt.hist(val1, bins = 20)
xmin,xmax = plt.xlim()
labelPlot(numFlips[0], numTrials, mean1, sd1)

val2, mean2, sd2 = flipSim(numFlips[1], numTrials)
plt.figure()
plt.hist(val2, bins = 20)
plt.xlim(xmin, xmax)
labelPlot(numFlips[1], numTrials, mean2, sd2)
plt.show()