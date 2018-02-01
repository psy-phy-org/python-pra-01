"""SVM."""
import numpy as np

from sklearn.datasets import load_digits
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.externals import joblib

digits = load_digits(10)

X_train = digits.data[:1500]
y_train = digits.target[:1500]

X_test = digits.data[1500:]
y_test = digits.target[1500:]

# Pipelineを作成
# データの正規化とSVMを定義
pipeline = Pipeline([
    ('standard_scaler', StandardScaler()),
    ('svm', SVC())])

# パラメータの探索範囲を指定
# Grid Search用のパラメータは本来であればもっと細かくやったほうがいい
params = {
    'svm__C': np.logspace(0, 2, 5),
    'svm__gamma': np.logspace(-3, 0, 5)
}

# Grid Searchを行う
clf = GridSearchCV(pipeline, params)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)

# 結果のレポーティング
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

# モデルの保存
# APIなどで利用する際はjoblib.loadで保存したモデルを読み込んで、入力されたデータに対してpredictを行えば良い
joblib.dump(clf, 'clf.pkl')
