from random import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris_data = load_iris()

print(iris_data.DESCR)

X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# 옵셔널 파라미터 max_depth=4  얼마나 깊은 결정트리를 만들것인지 결정
model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)

model.predict(X_test)

model.score(X_test, y_test)

# 90프로 확률로 분류

importances = model.feature_importances_

indices_sorted = np.argsort(importances)

plt.figure()
plt.title("Feature importances")
plt.bar(range(len(importances)), importances[indices_sorted])
plt.xticks(range(len(importances)), X.columns[indices_sorted], rotation=90)
plt.show()