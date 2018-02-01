import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# ワインデータ(CSV)を読み込む
wine = pd.read_csv('winequality-white.csv', delimiter=';')

# ワインのグレードを表の列だけ取り出す
y = wine['quality']

# 3Dで描画
xname = 'alcohol'
yname = 'sulphates' # 硫酸塩
zname = 'total sulfur dioxide' # 総二酸化硫黄

plt.style.use('ggplot')
fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel(xname)
ax.set_ylabel(yname)
ax.set_zlabel(zname)
ax.scatter3D(
    wine[xname],
    wine[yname],
    wine[zname],
    c=y, s=y**2, cmap='cool'
)
plt.show()
