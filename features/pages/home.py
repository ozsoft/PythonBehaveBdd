def clickelement(context):
    context.browser.get("http://www.cii.co.uk")
    elem = context.browser.find_element_by_id("login-link")
    elem.click()
