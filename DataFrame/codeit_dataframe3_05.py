import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
bool1 = (df['course name'] == 'information technology') & (df['year'] == 1)
bool2 = (df['course name'] == 'commerce') & (df['year'] == 4)

bool3 = df['course name'].value_counts() < 5
bool3_1 = bool3[bool3]
bool3_2 = bool3_1.index

df['status'] = 'allowed'

df.loc[(bool1 | bool2) == True, 'status'] = 'not allowed'

for i in range(0, 2000):
    if df.iloc[i, 2] in bool3_2:
        df.iloc[i, 3] = 'not allowed'

# 정답 출력
df