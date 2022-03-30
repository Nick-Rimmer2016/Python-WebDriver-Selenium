import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
#chrome_options.add_argument('window-size=1920x1080')
#chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)


driver.get('http://www.google.com/')
print(driver.title)
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('ChromeDriver')
search_box.submit()
driver.implicitly_wait(3)
driver.get_screenshot_as_file('googleHomePage.png')
time.sleep(5) # Let the user actually see something!
driver.quit()