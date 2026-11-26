import allure
from selenium.webdriver.common.keys import Keys

from data import METRO_LOAD_TIMEOUT
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить форму «Для кого самокат»")
    def fill_customer_form(self, data):
        self.type(OrderPageLocators.NAME_INPUT, data["name"])
        self.type(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.type(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self.select_metro(data["metro"])
        self.type(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать станцию метро «{station}»")
    def select_metro(self, station):
        self.click(OrderPageLocators.METRO_INPUT)
        self.type(OrderPageLocators.METRO_INPUT, station)  # фильтруем список станций
        self.wait_for_element(OrderPageLocators.metro_option(station), METRO_LOAD_TIMEOUT)
        self.click(OrderPageLocators.metro_option(station))

    @allure.step("Заполнить форму «Про аренду»")
    def fill_rent_form(self, data):
        self.type(OrderPageLocators.DATE_INPUT, data["date"])
        self.press_key(OrderPageLocators.DATE_INPUT, Keys.ENTER)  # закрываем календарь
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
