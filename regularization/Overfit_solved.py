import imp
from sklearn.linear_model import LinearRegression
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

model = LinearRegression()
model.fit(X_train, y_train)

y_train_predict = model.predict(X_train)

y_test_predict = model.predict(X_test)

mse = mean_squared_error(y_train, y_train_predict) ** 0.5
print('training set에서의 성능')
mse
# 과소적합
mse = mean_squared_error(y_test, y_test_predict) ** 0.5
print('test set에서의 성능')
mse
# 과적합