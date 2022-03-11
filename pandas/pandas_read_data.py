import pandas as pd

iphone_df = pd.read_csv('pandas/data/iphone.csv', index_col=0) # 첫줄이 헤더 헤더가 없다면 ('파일 경로', header=None)
print(iphone_df)