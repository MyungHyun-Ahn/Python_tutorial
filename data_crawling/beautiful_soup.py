import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import csv

# write_only=True : 파일 쓰기 모드
"""
wb = Workbook(write_only=True)

ws = wb.create_sheet('TV Rating')
ws.append(['순위', '채널', '프로그램', '시청률'])
"""

response = requests.get('https://workey.codeit.kr/ratings/index')

rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

program_title_tags = soup.select('td.program')

"""
program_list = []
for tag in program_title_tags:
    program_list.append(tag.get_text())
print(program_list)

print(soup.select_one('td.program'))
"""

"""
td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())
"""

"""
tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('td')

print(td_tags)
"""

# .attrs를 사용하면 태그의 모든 속성을 확인 가능 / 딕셔너리 형태로 저장
# print(soup.select_one('img').attrs)

'''
tr_tags = soup.select('tr')[1:]
for tr_tag in tr_tags:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(), # 순위
        td_tags[1].get_text(), # 채널
        td_tags[2].get_text(), # 프로그램
        td_tags[3].get_text(), # 시청률
    ]
    ws.append(row)

wb.save('data_crawling/시청률_2010년1월1주차.xlsx')
'''

# CSV 파일 생성
csv_file = open('data_crawling/시청률_2010년1월1주차.csv','w', newline="")
csv_writer = csv.writer(csv_file)

# 헤더 행 추가
csv_writer.writerow(['순위', '채널', '프로그램', '시청률'])

for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text().strip(),
        td_tags[1].get_text().strip(),
        td_tags[2].get_text().strip(),
        td_tags[3].get_text().strip()
    ]
    # 데이터 행 추가
    csv_writer.writerow(row)

# CSV 파일 닫기
csv_file.close()