# matplotlib　グラフの設定
# http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

# 2x3の6個のサブプロットに分割
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.plot(x, x**i)
    plt.title("y=x^{}".format(i))
plt.tight_layout()
plt.show()
