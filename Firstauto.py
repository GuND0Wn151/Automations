from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\ADMIN\Desktop\codes\Selenium\Drivers\chromedriver.exe")

driver.set_page_load_timeout("5")
driver.get("http://www.youtube.com")
driver.find_element_by_name("search_query").send_keys("god of war story playstationgrenade")

driver.find_element_by_class_name("style-scope ytd-searchbox").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_id('img').click()

time.sleep(5)
