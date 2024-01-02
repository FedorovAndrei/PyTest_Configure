import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):

    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)

    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), "Кнопка для добавления в корзину не найдена"