from behave import *
from page_object_model import welcome_page, dasboard_page
from env_setup.credential import login_credential
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://vsmonitor.com/welcome")
    return context.driver

def teardown(context):
    context.driver.quit()

@given('I login with correct credentials')
def step_login(context):
    driver = setup(context)
    
    # Assert the page title
    assert driver.title == "VS Monitor", "Unexpected title on welcome page"
    
    # Perform login action
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, welcome_page.login_welcome_page_button)))
    welcome_page.login_welcome_page_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, welcome_page.email_textfield)))
    welcome_page.email_textfield.send_keys(login_credential.valid_username)
    welcome_page.password_textfield.click()
    welcome_page.password_textfield.send_keys(login_credential.valid_password)
    welcome_page.login_button.click()

    # Assert login was successful by checking title and URL
    WebDriverWait(driver, 10).until(EC.url_to_be("https://vsmonitor.com/dashboard"))
    assert driver.current_url == "https://vsmonitor.com/dashboard", "Login failed or incorrect URL"
    assert dasboard_page.dashboard_title == "Dashboard", "Incorrect page title"

@then('I close the browser')
def step_close_browser(context):
    teardown(context)










