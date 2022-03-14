import pandas as pd
    
df = pd.read_csv('data/toeic.csv')

# 코드를 작성하세요.
boolean_df = (df['LC'] + df['RC'] >= 600) & ((df['LC'] >= 250) & (df['RC'] >= 250))
df['합격 여부'] = boolean_df
# 정답 출력
df