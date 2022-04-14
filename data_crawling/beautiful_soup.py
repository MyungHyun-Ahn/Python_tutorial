import requests
from bs4 import BeautifulSoup

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

tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('td')

print(td_tags)