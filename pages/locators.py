from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div')
