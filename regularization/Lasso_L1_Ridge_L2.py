import imp
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

from math import sqrt

import pandas as pd
import numpy as np

# 대학원 합격 파일

ADMISSON_FILE_PATH = 'regularization/data/admission_data.csv'
admisson_df = pd.read_csv(ADMISSON_FILE_PATH).drop('Serial No.', axis=1)

admisson_df.head()

# Chance of Admit 아웃풋 변수 나머지 인풋 변수

X = admisson_df.drop(['Chance of Admit '], axis=1)

polynomial_transformer = PolynomialFeatures(6)

polynomial_features = polynomial_transformer.fit_transform(X.values)

features = polynomial_transformer.get_feature_names(X.columns)

X = pd.DataFrame(polynomial_features, columns=features)

X.head()

y = admisson_df[['Chance of Admit ']]

y.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)

# 람다의 역할을 해주는 파라미터 alpha
# 경사하강을 몇번 해줄지 정하는 파라미터 max_iter=
# feature scaling 을 해줄지 결정하는 파라미터 normalize=True
# L1 정규화를 쓰고 싶다면 Lasso
# L2 정규화를 쓰고 싶가면 Ridge

model = Ridge(alpha=0.001, max_iter=1000, normalize=True)
model.fit(X_train, y_train)

y_train_predict = model.predict(X_train)

y_test_predict = model.predict(X_test)

mse = mean_squared_error(y_train, y_train_predict) ** 0.5
print('training set에서의 성능')
mse

mse = mean_squared_error(y_test, y_test_predict) ** 0.5
print('test set에서의 성능')
mse
