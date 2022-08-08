from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open_page()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
