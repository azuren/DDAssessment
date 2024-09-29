from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#login button at welcome page
login_welcome_page_button = driver.find_element(by=By.TAG_NAME, "button")

#email textfield
email_textfield = driver.find_element(By.ID, "username")

#password textfield
password_textfield = driver.find_element(By.ID, "passowrd")

#login button at login page
login_button = driver.find_element(By.CSS_SELECTOR, "#login")
