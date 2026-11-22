import allure
import pytest

from data import ORDER_DATA
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize(
        "entry_point, order_data",
        [("top", ORDER_DATA[0]), ("bottom", ORDER_DATA[1])],
        ids=["top_button_data_set_1", "bottom_button_data_set_2"],
    )
    def test_order_scooter_success(self, driver, main_page, entry_point, order_data):
        main_page.click_order_button(entry_point)
        order_page = OrderPage(driver)
        order_page.fill_customer_form(order_data)
        order_page.fill_rent_form(order_data)
        order_page.submit_order()

        assert order_page.is_success_modal_visible()
