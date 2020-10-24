from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def login(context, pin, password):
    wait = WebDriverWait(context.browser, 10)
    loginemail = wait.until(EC.element_to_be_clickable((By.ID, 'LoginEmail')))
    loginpassword = context.browser.find_element_by_id("LoginPassword")
    loginsubmit = context.browser.find_element_by_id("login")
    loginemail.send_keys(pin)
    loginpassword.send_keys(password)
    loginsubmit.click()