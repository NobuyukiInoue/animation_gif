# matplotlib　グラフの設定
# http://python-remrin.hatenadiary.jp/entry/2017/05/27/114816

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
#fp = FontProperties(fname='C:\WINDOWS\Fonts\msgothic.ttc', size=14)

x = np.linspace(-np.pi, np.pi*1.1, 100)
plt.plot(x, np.cos(x), "r", label="y=cos(x)")
plt.plot(x, np.sin(x), "olive", label="y=sin(x)")
#plt.title("三角関数", loc="center", fontproperties=fp)
plt.title("三角関数", loc="center")

plt.xlim(xmin=-np.pi)
plt.ylim(-1.1, 1.1)
xtick = np.array(["-π", "-1/2π", "0", "1/2π", "π"])
locs = np.linspace(-np.pi, np.pi, 5)
plt.xticks(locs, xtick, color="c", fontsize=14, rotation=30)
plt.yticks([-1, 0, 1])

ax = plt.gca()                        # get current axis
ax.spines["right"].set_color("none")  # 右枠消し
ax.spines["top"].set_color("none")    # 上枠消し
ax.spines["left"].set_color("m")      # 左枠をマゼンダに
ax.spines["bottom"].set_color("c")    #　下枠をシアンに
         
plt.vlines(np.linspace(-np.pi, np.pi, 5),
           -1.1, 1.1, "c",linestyle=":", lw=1)
plt.hlines([0], -np.pi, np.pi*1.1, "m", linestyle=":", lw=1)

plt.legend()    # 凡例の表示
plt.show()
