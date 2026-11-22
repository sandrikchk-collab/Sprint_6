import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_customer_form(self, data):
        self.type(OrderPageLocators.NAME_INPUT, data["name"])
        self.type(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.type(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.metro_option(data["metro"]))
        self.type(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму «Про аренду»")
    def fill_rent_form(self, data):
        date_input = self.find(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(data["date"])
        date_input.send_keys(Keys.ENTER)  # закрываем календарь
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.rent_option(data["rent"]))
        self.click(OrderPageLocators.color_checkbox(data["color"]))
        if data["comment"]:
            self.type(OrderPageLocators.COMMENT_INPUT, data["comment"])

    @allure.step("Нажать «Заказать» и подтвердить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить окно «Заказ оформлен»")
    def is_success_modal_visible(self):
        return self.is_visible(OrderPageLocators.SUCCESS_HEADER)
