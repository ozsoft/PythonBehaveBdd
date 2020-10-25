from selenium import webdriver


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path=r"/Users/ozgur/Downloads/chromedriverpy")


def after_scenario(context, scenario):
    context.browser.quit()

