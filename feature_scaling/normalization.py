from locale import normalize
import pandas as pd
import numpy as np
from sklearn import preprocessing

NBA_FILE_PATH = 'feature_scaling/data/NBA_player_of_the_week.csv'

nba_player_of_the_week = pd.read_csv(NBA_FILE_PATH)

nba_player_of_the_week.head()

nba_player_of_the_week.describe()

# cm / kg feature scaling

height_weight_age_df = nba_player_of_the_week[['Height CM', 'Weight KG', 'Age']]

height_weight_age_df.head()

# min-max normalization

# 0 - 1 로 바꾸어주는 도구
scaler = preprocessing.MinMaxScaler()
normalized_data = scaler.fit_transform(height_weight_age_df)

normalized_df = pd.DataFrame(normalized_data, columns=['Height', 'Weight', 'Age'])

normalized_df.head()

