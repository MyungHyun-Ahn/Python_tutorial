import pandas as pd

TITANIC_FILE_PATH = 'feature_scaling/data/titanic.csv'

titanic_df = pd.read_csv(TITANIC_FILE_PATH)

titanic_df.head()

titanic_sex_embarked = titanic_df[['Sex', 'Embarked']]

titanic_sex_embarked

one_hot_encoded_df = pd.get_dummies(titanic_sex_embarked)

one_hot_encoded_df.head()

# 원하는 열들만 on hot encoding

one_hot_encoded_df2 = pd.get_dummies(data=titanic_df, columns=['Sex', 'Embarked'])

one_hot_encoded_df2.head()