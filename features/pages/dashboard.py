from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def checkDashboardPin(context):
    wait = WebDriverWait(context.browser, 10)
    pinelem = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div[1]/aside/header/p')))
    pin = pinelem.text
    print(pin)
    assert pin == "001705261A"
    context.browser.quit()
