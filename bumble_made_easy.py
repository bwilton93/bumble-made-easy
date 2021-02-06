import random
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Function to wait for element to appear on page
def waiting_func(by_variable, attribute):
    try:
        WebDriverWait(driver, 20).until(lambda x: x.find_element(by=by_variable,  value=attribute))
    except (NoSuchElementException, TimeoutException):
        print('{} {} not found'.format(by_variable, attribute))
        exit()

# Create login values
USERNAME = input('Enter username: ')
PASSWORD = getpass.getpass('Enter password: ')

# Open bumble in Chrome browser
driver = driver = webdriver.Chrome('C:/users/bwilt/python/chromedriver')
driver.get("https://www.bumble.com/app")

# Locate and click Facebook login
waiting_func('xpath', '//*[@id="main"]/div/div/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span')
login = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div/span/span[2]/span')
login.click()

# Swap to new window
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)

# Login through Facebook
waiting_func('name', 'email')
email = driver.find_element_by_name('email')
email.send_keys(USERNAME)
password = driver.find_element_by_name('pass')
password.send_keys(PASSWORD)
login = driver.find_element_by_name('login')
login.click()

# Swap to main window
driver.switch_to_window(window_before)

i = 100

while i > 0:
    waiting_func('css selector', '[data-qa-icon-name="floating-action-yes"]')
    n = random.randint(0,1)
    # print(n)
    if(n == 0):
        swipeleft = driver.find_element_by_css_selector('[data-qa-icon-name="floating-action-no"]')
        swipeleft.click()
    elif(n == 1):
        swiperight = driver.find_element_by_css_selector('[data-qa-icon-name="floating-action-yes"]')
        swiperight.click()
    print(i)
    i = i - 1
    j = random.randint(2, 4)
    time.sleep(j)

if i == 0:
    driver.quit()
