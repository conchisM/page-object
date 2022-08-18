from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks = pytest.mark.xfail), 8, 9])
def test_guest_can_go_to_product_page(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    page.open_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_name_egual()

