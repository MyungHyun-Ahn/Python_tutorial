import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

# 코드를 작성하세요.
dict_m = {
    'day' : samsong_df['요일'],
    'samsong' : samsong_df['문화생활비'],
    'hyundee' : hyundee_df['문화생활비']
}

df = pd.DataFrame(dict_m)

df