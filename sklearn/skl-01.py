# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets
from sklearn import svm
from matplotlib import pyplot as plt


# 手書き数字データを読み込む
# 引数の最大値は10で0から9となる
digits = datasets.load_digits(2)


# 1797個のサンプルデータが入っている
# 説明変数（予測に利用するデータ）
print('data:\n', digits.data)
print('data-size:', digits.data.shape[0])
# 目的変数（予測したい値）
print('target:', digits.target)
print('target-size:\n', digits.target.shape[0])
# 0番目のピクセルデータ
print('pixel data\n', digits.images[0])


# 画像の表示
plt.subplot(141), plt.imshow(digits.images[0], cmap = 'gray')
plt.title('number 0'), plt.xticks([]), plt.yticks([])
plt.show()
