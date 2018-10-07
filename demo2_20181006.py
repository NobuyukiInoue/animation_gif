# 早く知っておきたかったmatplotlibの基礎知識、あるいは見た目の調整が捗るArtistの話
# https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xtick = np.array(["-π", "-1/2π", "0", "1/2π", "π"])
locs = np.linspace(-np.pi, np.pi, 5)
fig = plt.figure()
x = np.arange(-np.pi, np.pi, 0.1)
values = np.arange(-np.pi, np.pi, 0.1)

ims = []
flag_legend = True  #凡例描画のフラグ

for a in values:
    y1 = np.sin(x - a)
    y2 = np.sin(x + a)
    y3 = y1 + y2
    im1 = plt.plot(x, y1, "r", label='y1=sin(x-a)', color="red")
    im2 = plt.plot(x, y2, "r", label='y2=sin(x+a)', color="blue")
    im3 = plt.plot(x, y3, "r", label='y1+y2', color="green")

    if flag_legend:#一回のみ凡例を描画
        plt.legend()
        #plt.title("揺動運動", loc="center", fontproperties=fp)
        plt.title("sin curves", loc="center")
        plt.xticks(locs, xtick, color="c", fontsize=14, rotation=30)
        #ax = plt.gca()                        # get current axis
        #ax.spines["right"].set_color("none")  # 右枠消し
        #ax.spines["top"].set_color("none")    # 上枠消し
        #ax.spines["left"].set_color("m")      # 左枠をマゼンダに
        #ax.spines["bottom"].set_color("c")    #　下枠をシアンに
        plt.vlines(np.linspace(-np.pi, np.pi, 5), -2.1, 2.1, "c",linestyle=":", lw=1)
        plt.hlines([0], -np.pi, np.pi*1.1, "m", linestyle=":", lw=1)
        flag_legend = False

    ims.append(im1 + im2 + im3) #グラフを配列に追加

#plt.show()
ani = animation.ArtistAnimation(fig, ims, interval=100) #100msごとに表示
ani.save("sin_curves.gif", writer="imagemagick")
