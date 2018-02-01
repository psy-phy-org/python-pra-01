# Scikit learnのサンプル学習データを取り込む
from sklearn import datasets
from sklearn import model_selection


# 手書き数字データを読み込む
digits = datasets.load_digits(2)


# トレーニング（学習）データとテストデータの準備（学習:テスト = 9:1に分割）
X_train, X_test, y_train, y_test = model_selection.train_test_split(digits.data, digits.target, test_size=0.1, random_state=0)

# X_train: トレーニング用の特徴行列
# X_test: テスト用の特徴行列
# y_train: トレーニング用の目的変数
# y_test: テスト用の目的変数


# 学習データとテストデータのサイズ
print('X_train size:', X_train.shape[0])
print('X_test size:', X_test.shape[0])
print('y_train size:', y_train.shape[0])
print('y_test size:', y_test.shape[0])

print('X_train\n', X_train)
print('y_train\n', y_train)
print('X_test\n', X_test)
print('y_test\n', y_test)
