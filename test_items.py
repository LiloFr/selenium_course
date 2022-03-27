link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_site_have_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector(".btn-primary"))
    assert button > 0, "Can't find the button!"
