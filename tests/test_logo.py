import allure

from data import Urls


@allure.feature("Логотипы в шапке")
class TestLogo:

    @allure.title("Клик по логотипу «Самоката» открывает главную страницу")
    def test_scooter_logo_opens_main_page(self, order_page):
        order_page.click_scooter_logo()

        assert order_page.wait_url_contains(Urls.MAIN) == Urls.MAIN

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новом окне")
    def test_yandex_logo_opens_dzen(self, main_page):
        main_page.click_yandex_logo_and_switch()

        assert Urls.DZEN in main_page.wait_url_contains(Urls.DZEN)
