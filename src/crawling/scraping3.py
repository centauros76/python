from selenium import webdriver
import time

driver = webdriver.Chrome('../../chromedriver')
driver.get('http://python.org')

menus = driver.find_elements_by_css_selector('#top ul.menu li')

pypi = None
for m in menus:
    if m.text == 'PyPI':
        pypi = m
    print(m.text)

pypi.click()

time.sleep(5)
driver.quit()