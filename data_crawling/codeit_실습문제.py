import requests
from bs4 import BeautifulSoup

### 코드를 작성하세요 ###
response = requests.get('https://workey.codeit.kr/orangebottle/index')
phoneNum_page = response.text
soup = BeautifulSoup(phoneNum_page, 'html.parser')

branch_tags = soup.select('div.branch')
branch_infos = []
for tag in branch_tags:
    branch_info = []
    city = tag.select('p.city')[0]
    address = tag.select('p.address')[0]
    phoneNum = tag.select('span.phoneNum')[0]
    branch_info.append(city.get_text())
    branch_info.append(address.get_text())
    branch_info.append(phoneNum.get_text())
    branch_infos.append(branch_info)


# 출력 코드
print(branch_infos)