import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 코드를 작성하세요.
df.loc[:, 'JTBC'] # 명확한 위치를 나타내 주어야함
df['JTBC'] # 한 column에 대한 인덱싱