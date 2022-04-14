import requests
from bs4 import BeautifulSoup
import csv

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

csv_file = open('data_crawling/오렌지_보틀.csv','w', newline="")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['지점 이름', '주소', '전화번호'])
csv_writer.writerows(branch_infos)

csv_file.close()