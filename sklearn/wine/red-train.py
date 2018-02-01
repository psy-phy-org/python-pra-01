# coding: utf-8

import pandas as pd
import numpy as np

wine = pd.read_csv("winequality-white.csv", sep=";")
wine.head

# sklearn.linear_model.LinearRegression クラスを読み込み
from sklearn import linear_model
clf = linear_model.LinearRegression()

# 説明変数に "density (濃度)" を利用
X = wine.loc[:, ['density']].as_matrix()

# 目的変数に "alcohol (アルコール度数)" を利用
Y = wine['alcohol'].as_matrix()

# 予測モデルを作成
clf.fit(X, Y)

# 回帰係数
print(clf.coef_)

# 切片 (誤差)
print(clf.intercept_)

# 決定係数
print(clf.score(X, Y))

# matplotlib パッケージを読み込み
import matplotlib.pyplot as plt

# 散布図
plt.scatter(X, Y)

# 回帰直線
plt.plot(X, clf.predict(X))
plt.show()
