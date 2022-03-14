import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
df.rename(columns={'room assignment' : 'room number'}, inplace=True)

auditorium = df[df['room number'] == 'Auditorium']
auditorium_1 = auditorium['course name'].sort_values().unique()

for course in range(len(auditorium_1)):
    for i in range(2000):
        if df.iloc[i, 2] == auditorium_1[course]:
            df.iloc[i, 4] = 'Auditorium-%d' % (course+1)
            
large = df[df['room number'] == 'Large room']
large_1 = large['course name'].sort_values().unique()

for course in range(len(large_1)):
    for i in range(2000):
        if df.iloc[i, 2] == large_1[course]:
            df.iloc[i, 4] = 'Large-%d' % (course+1)
            
medium = df[df['room number'] == 'Medium room']
medium_1 = medium['course name'].sort_values().unique() 

for course in range(len(medium_1)):
    for i in range(2000):
        if df.iloc[i, 2] == medium_1[course]:
            df.iloc[i, 4] = 'Medium-%d' % (course+1)
            
small = df[df['room number'] == 'Small room']
small_1 = small['course name'].sort_values().unique()

for course in range(len(small_1)):
    for i in range(2000):
        if df.iloc[i, 2] == small_1[course]:
            df.iloc[i, 4] = 'Small-%d' % (course+1)
            
for i in range(2000):
    if df.iloc[i, 3] == 'not allowed':
        df.iloc[i, 4] = 'not assigned'
# 정답 출력
df