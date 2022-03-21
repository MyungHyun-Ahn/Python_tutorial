import imp
from multiprocessing.spawn import import_main_path
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

iris_data = load_iris()

X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['class'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
y_train = y_train.values.ravel()

# n_estimators=a 결정 스텀프를 몇개 만들지 설정
model = AdaBoostClassifier(n_estimators=100)
model.fit(X_train, y_train)
model.predict(X_test)

model.score(X_test, y_test)

# 87 프로 확률

importances = model.feature_importances_

indices_sorted = np.argsort(importances)

plt.figure()
plt.title("Feature importances")
plt.bar(range(len(importances)), importances[indices_sorted])
plt.xticks(range(len(importances)), importances[indices_sorted], rotation=90)
plt.show()
