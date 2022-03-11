import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])

print(my_df.dtypes)

# int64 : 정수     float64 : 소수
# object : 텍스트  bool : 불린(참과 거짓)
# datatime64 : 날짜와 시간
# category : 카테고리