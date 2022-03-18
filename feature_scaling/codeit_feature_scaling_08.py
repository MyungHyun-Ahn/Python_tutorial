import imp
import pandas as pd
from sklearn  import preprocessing

Age = pd.DataFrame([25, 49, 32, 35, 40], columns=['나이'])

Age.head()

scaler = preprocessing.MinMaxScaler()

scaling_data = scaler.fit_transform(Age)


scaling_df = pd.DataFrame(scaling_data, columns=['Normalized된 나이'])

scaling_df

salary = pd.DataFrame([25000000, 35000000, 30000000, 50000000, 35000000], columns=['연봉'])

salary_s = scaler.fit_transform(salary)

salary_s_df = pd.DataFrame(salary_s, columns=['Normalized된 연봉'])

salary_s_df