import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'

def test_check_add_to_basket_button(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')) > 0
