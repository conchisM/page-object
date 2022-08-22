from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)  
    page.open_page()  
    login_page = page.go_to_login_page()  
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
        
        
