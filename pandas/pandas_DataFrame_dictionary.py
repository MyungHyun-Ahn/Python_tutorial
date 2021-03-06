import numpy as np
import pandas as pd

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

# 리스트
dict1 = {
    'name': names, 
    'english_score': english_scores, 
    'math_score': math_scores
}

# 넘파이 배열
dict2 = {
    'name': np.array(names), 
    'english_score': np.array(english_scores), 
    'math_score': np.array(math_scores)
}

# pandas Series
dict3 = {
    'name': pd.Series(names), 
    'english_score': pd.Series(english_scores), 
    'math_score': pd.Series(math_scores)
}


df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)
print()
print(df2)
print()
print(df3)