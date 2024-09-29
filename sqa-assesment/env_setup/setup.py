from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://vsmonitor.com/welcome")

driver.quit()
