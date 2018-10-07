# matplotlib　グラフの設定
# http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
#fp = FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)
from matplotlib import gridspec

x = np.random.randn(1000)
y = np.random.randn(1000)

gs = gridspec.GridSpec(2, 2, width_ratios=(6, 1), height_ratios=(4, 1))
ax = [plt.subplot(gs[0, 0]), plt.subplot(gs[0, 1]), plt.subplot(gs[1, 0])]

# メインの散布図
#ax[0].set_title("散布図", fontproperties=fp)
ax[0].set_title("散布図")
ax[0].scatter(x, y, c="c", alpha=0.5) # 不透明度0.5
ax[0].grid()                          # グリッド表示

# 右側のヒストグラム
ax[1].hist(y, 50, orientation="horizontal")
ax[1].invert_xaxis()       # 左右反転
ax[1].yaxis.tick_right()   # 縦軸の目盛りを右側に配置

# 下のヒストグラム
ax[2].hist(x, 100)
ax[2].tick_params(labelbottom="off")

plt.tight_layout()
plt.show()
