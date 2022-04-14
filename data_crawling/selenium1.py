from selenium import webdriver
import time
driver = webdriver.Chrome('data_crawling/chromedriver.exe')
# 웹사이트가 로딩이 완료되기까지 최대 몇초 기다려줄 것인지 정하는 매소드
driver.implicitly_wait(3)

'''
element_to_be_clickable() : 웹 요소가 클릭 가능한 상태일 때까지 기다림.
visibility_of_element_located() : 웹 요소가 실제로 보일 때까지 기다림.
text_to_be_present_in_element() : 웹 요소 안에 텍스트가 로딩될 때까지 기다림.
invisibility_of_element_located() : 웹 요소가 안 보일 때까지 기다림.
'''


driver.get('https://workey.codeit.kr/costagram/index')
# 1초 멈춤
time.sleep(1)

driver.find_element_by_css_selector('#app > nav > div > a').click()
time.sleep(1)

driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('#app > div > div > div > form > input.login-container__login-button').click()

