from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

import numpy as np
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

iris_data = datasets.load_iris()

X = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns=['Class'])

logistic_model = LogisticRegression(max_iter=2000)

# cv 파라미터는 몇개로 나누어 줄것인지 설정
# cross_val_score 메서드는 cv=k k개 만큼의 성능 값을 반환
cvs = cross_val_score(logistic_model, X, y.values.ravel(), cv=5)

# 반환된 값들의 평균을 구하면
np.average(cvs)

# k겹 교차 검증의 평균 성능이 출력됨
