from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
import csv

driver = webdriver.Chrome('data_crawling/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
sleep(1)

driver.find_element_by_css_selector('#app > nav > div > a').click()
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__password-input').send_keys('datascience')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-button').click()

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 새로운 내용 로딩될때까지 기다림
    sleep(0.5)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

post_list = driver.find_elements_by_css_selector('div.post-list__post.post')

post_infos = []

# 하나씩 열고 닫기
for post in post_list:
    post.click()
    sleep(1)
    post_info = []
    image_tag = driver.find_element_by_css_selector('div.post-container__image').get_attribute('style')
    main_text = driver.find_element_by_css_selector('span.content__text').text
    hashtag = driver.find_elements_by_css_selector('div.content__tag-cover')
    hashtags = hashtag[0].text
    for i in range(1, len(hashtag)):
        hashtags = hashtags + hashtag[i].text

    like_count = driver.find_element_by_css_selector('span.content__like-count').text
    comment_count = driver.find_element_by_css_selector('span.content__comment-count').text

    post_info.append(image_tag.split('\"')[1])
    post_info.append(main_text)
    post_info.append(hashtags)
    post_info.append(like_count)
    post_info.append(comment_count)

    post_infos.append(post_info)

    driver.find_element_by_css_selector('button.close-btn').click()
    sleep(0.1)


driver.quit()

csv_file = open('data_crawling/코스타그램.csv','w', newline="", encoding='cp949')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['이미지 주소', '내용', '해시태그', '좋아요 수', '댓글 수'])
csv_writer.writerows(post_infos)

csv_file.close()
"""
이미지를 자동으로 다운로드하는 코드

for i in range(len(image_urlList)):
    image_url = image_urlList[i]
    response = requests.get(image_url)
    filename = 'data_crawling/codeit_test_img/image{}.jpg'.format(i)
    with open(filename, 'wb+') as f:
        f.write(response.content)
"""