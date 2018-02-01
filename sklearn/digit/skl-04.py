# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import classification_report


# 手書き数字データを読み込む
digits = datasets.load_digits(10)


# トレーニングデータとテストデータの準備（学習:テスト = 9:1に分割）
X_train, X_test, y_train, y_test = model_selection.train_test_split(digits.data, digits.target, test_size=0.9, random_state=0)


# 識別器の作成
classifier = svm.SVC(kernel='rbf', C=100, gamma=0.001)


# fit関数で学習する
classifier.fit(X_train, y_train)


# predict関数で予測する
predicted = classifier.predict(X_test)


# classification_report（分類レポート）を出力
print(classification_report(y_test, predicted))
