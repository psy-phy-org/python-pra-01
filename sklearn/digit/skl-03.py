# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets
from sklearn import model_selection
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# 手書き数字データを読み込む
digits = datasets.load_digits(2)


# トレーニングデータとテストデータの準備（学習:テスト = 9:1に分割）
X_train, X_test, y_train, y_test = model_selection.train_test_split(digits.data, digits.target, test_size=0.1, random_state=0)

# X_train: トレーニング用の特徴行列
# X_test: テスト用の特徴行列
# y_train: トレーニング用の目的変数
# y_test: テスト用の目的変数


# 識別器の作成
classifier = svm.SVC(kernel='rbf', C=1, gamma=0.1)
# classifier = svm.SVC(kernel='rbf', C=100, gamma=0.001)


# fit関数で学習する
# X_train、y_trainで学習させて、
classifier.fit(X_train, y_train)


# predict関数で予測する
# X_testのラベルを予測する。
predicted = classifier.predict(X_test)


# 予測
print('predict:\n', predicted)


# テスト用の目的変数
print('X_train:\n', y_test)


# confusion matrix（混同行列）を出力
cfm = confusion_matrix(y_test, predicted, labels=digits.target_names)
print('matrix\n', cfm)


# accuracy_score（正答率）を出力
acs = accuracy_score(predicted, y_test)
print('score', acs)
