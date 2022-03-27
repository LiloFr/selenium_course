link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_site_have_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-primary")
    assert button, "Can't find the button!"