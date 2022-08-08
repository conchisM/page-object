import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_should_see_login_link(self, browser): #fixtures are described in the file conftest.py
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
