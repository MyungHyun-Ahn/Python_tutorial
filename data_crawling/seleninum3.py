from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

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
    sleep(1)

    # 새로운 내용 로딩됐는지 확인
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

post_list = driver.find_elements_by_css_selector('div.post-list__post.post')

# 하나씩 열고 닫기
for post in post_list:
    post.click()
    sleep(1)
    # 에러
    image_tag = driver.find_element_by_class_name('div.post-container__image').get_attribute('style')
    print(image_tag.split("")[1])
    driver.find_element_by_css_selector('button.close-btn').click()
    sleep(0.1)

driver.quit()