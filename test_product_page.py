from .pages.product_page import ProductPage


class TestProductPage:
    def test_guest_can_go_to_product_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open_page()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_name_egual()

