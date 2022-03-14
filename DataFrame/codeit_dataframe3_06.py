import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
df['room assignment'] = 'not assigned'
counts = df['course name'].value_counts()

for i in range(0, 2000):
    if counts[df.iloc[i, 2]] >= 80:
        df.iloc[i, 4] = 'Auditorium'
    elif counts[df.iloc[i, 2]] >= 40:
        df.iloc[i, 4] = 'Large room'
    elif counts[df.iloc[i, 2]] >= 15:
        df.iloc[i, 4] = 'Medium room'
    elif counts[df.iloc[i, 2]] >= 5:
        df.iloc[i, 4] = 'Small room'
    if df.iloc[i, 3] == 'not allowed':
        df.iloc[i, 4] = 'not assigned'
# 정답 출력
df