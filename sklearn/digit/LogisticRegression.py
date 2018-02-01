# coding=utf-8
# pylint: disable=invalid-name
"""LogisticRegression"""

from sklearn.datasets import load_digits

# 手書きデータを読み込む
digits = load_digits(10)

# 今回は1500件を学習データ、残りの297件をテストデータにする
train_X = digits.data[:1500]
train_Y = digits.target[:1500]

test_X = digits.data[1500:]
test_Y = digits.target[1500:]

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
# fit関数で学習を行う
lr.fit(train_X, train_Y)

# predict関数で予測を行う
pred = lr.predict(test_X)
print(pred)

# confusion matrixを出力する
from sklearn.metrics import confusion_matrix
cf = confusion_matrix(test_Y, pred, labels=digits.target_names)
print(cf)
