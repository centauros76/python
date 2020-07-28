from selenium import webdriver
browers = webdriver.Chrome("/Users/rene.kwak/Private/source/study/python/chromedriver")
browers.get("https://tech.kakaoenterprise.com/category/Tech%20Log")
print(browers.page_source)
browers.quit()
exit()