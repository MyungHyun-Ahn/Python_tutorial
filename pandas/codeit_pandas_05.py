import pandas as pd

# 코드를 작성하세요.
name_list = ['Taylor Swift', 'Aaron Sorkin', 'Harry Potter', 'Ji-Sung Park']
birthday_list = ['December 13, 1989', 'June 9, 1961', 'July 31, 1980', 'February 25, 1981']
occupation_list = ['Singer-songwriter', 'Screenwriter', 'Wizard', 'Footballer']

dict1 = {
    'name' : pd.Series(name_list),
    'birthday' : pd.Series(birthday_list),
    'occupation' : pd.Series(occupation_list)
}

df = pd.DataFrame(dict1)
# 정답 출력
print(df)
