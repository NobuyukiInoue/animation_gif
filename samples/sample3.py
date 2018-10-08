# matplotlib　グラフの設定
# http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816

import matplotlib.pyplot as plt
import numpy as np

# 3x3の9個のサブプロットに分割
fig, axs = plt.subplots(3, 3, figsize=(8, 6))

t = np.linspace(0, np.pi*2, 100)
for i in range(3):
    for j in range(3):
        axs[i, j].plot(np.cos(t*(i+1)), np.sin(t*(j+1)))

plt.show()