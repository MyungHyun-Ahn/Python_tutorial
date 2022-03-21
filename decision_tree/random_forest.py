from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris_data = load_iris()
X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

# n_estimators=a 결정트리를 a개 만들어서 예측을 함 / 안쓰면 기본 값 100
# max_depth=a 트리의 최대 깊이
model = RandomForestClassifier(n_estimators=100, max_depth=4)

model.fit(X_train, y_train)

y_test_predict = model.predict(X_test)

model.score(X_test, y_test)

# 90 프로 확률로 제대로 분류
# 랜덤 포레스트도 평균 지니 감소로 속성 중요도 계산 가능

importances = model.feature_importances_

indices_sorted = np.argsort(importances)

plt.figure()
plt.title("Feature importances")
plt.bar(range(len(importances)), X.columns[indices_sorted])
plt.xticks(range(len(importances)), X.columns[indices_sorted], rotation=90)
plt.show()
