from selenium import webdriver

driver = webdriver.Chrome('data_crawling/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/orangebottle/index')

branch_infos = []

for phoneNum in driver.find_elements_by_css_selector('div.branch'):
    branch_name = phoneNum.find_element_by_css_selector('p.city').text.strip()
    address = phoneNum.find_element_by_css_selector('p.address').text.strip()
    phone_number = phoneNum.find_element_by_css_selector('span.phoneNum').text.strip()
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)

driver.quit()