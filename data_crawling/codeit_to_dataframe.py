import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['period', 'rank', 'channel', 'program', 'rating'])
n=0
# 코드를 작성하세요.
for year in range(2010, 2013):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')
            
            for tr_tag in soup.select('tr')[1:]:
                td_tags = tr_tag.select('td')
                period = soup.select('select#weekSelectBox')
                row = [
                    period[0].get_text().split('\n')[1],
                    td_tags[0].get_text(), # 순위
                    td_tags[1].get_text(), # 채널
                    td_tags[2].get_text(), # 프로그램
                    td_tags[3].get_text(), # 시청률
                ]
                df.loc[n] = row
                n+=1
            
# 결과 출력
print(df.head())