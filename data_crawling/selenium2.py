from selenium import webdriver
import time
driver = webdriver.Chrome('data_crawling/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

popular_artists = []

for artist in driver.find_elements_by_css_selector('ul.popular__order li'):
    popular_artists.append(artist.text.strip())

print(popular_artists)