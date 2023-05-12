from selenium import webdriver
options = webdriver.ChromeOptions() # 백그라운드에서 스크래핑 시작되는 것 
options.headless = True
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')


driver = webdriver.Chrome('/Users/thisismine/Downloads/Install/chromedriver',options=options)
driver.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
driver.get(url)

detected_value = driver.find_element_by_id('detected_value')
print(detected_value.text)
driver.quit()
