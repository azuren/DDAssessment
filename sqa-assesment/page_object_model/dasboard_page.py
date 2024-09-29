from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#page title
dashboard_title = driver.find_element(By.TAG_NAME, "h2")