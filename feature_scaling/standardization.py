from locale import normalize
import pandas as pd
import numpy as np
from pygments import highlight

from sklearn import preprocessing

NBA_FILE_PATH = 'feature_scaling/data/NBA_player_of_the_week.csv'

pd.set_option('display.float_format', lambda x: '%.5f' % x)

nba_player_of_the_week = pd.read_csv(NBA_FILE_PATH)

height_weight_age_df = nba_player_of_the_week[['Height CM', 'Weight KG', 'Age']]


scaler = preprocessing.StandardScaler()

standardized_data = scaler.fit_transform(height_weight_age_df)

standardized_df = pd.DataFrame(standardized_data, columns=['Height', 'Weight', 'Age'])

standardized_df.head()