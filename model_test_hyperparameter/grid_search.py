from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from math import sqrt

import numpy as np
import pandas as pd

# 데이터 준비

ADMISSION_FILE_PATH = 'model_test_hyperparameter/data/admission_data.csv'
admission_df = pd.read_csv(ADMISSION_FILE_PATH)

X = admission_df.drop('Chance of Admit ', axis=1)

polynomial_transformer = PolynomialFeatures(2)
polynomial_features = polynomial_transformer.fit_transform(X.values)

features = polynomial_transformer.get_feature_names(X.columns)

X = pd.DataFrame(polynomial_features, columns=features)
y = admission_df[['Chance of Admit ']]

hyper_parameter = {
    'alpha' : [0.01, 0.1, 1, 10],
    'max_iter' : [100, 500, 1000, 1500, 2000]
}

lasso_model = Lasso()

hyper_parameter_tuner = GridSearchCV(lasso_model, hyper_parameter, cv=5)
hyper_parameter_tuner.fit(X, y)

hyper_parameter_tuner.best_params_

# alpha = 1, max_iter = 100

