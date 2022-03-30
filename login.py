from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

usernameStr = 'test'
passwordStr = 'password'

browser = webdriver.Chrome()
browser.get(('https://blah'))

# fill in username and hit the next button

username = browser.find_element('username')
username.send_keys(usernameStr)

password = browser.find_element(By.ID,'value')
password.send_keys(passwordStr)

LoginButton = browser.find_element_by_id('j_id_1o')
LoginButton.click()