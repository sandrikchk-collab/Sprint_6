from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1 — «Для кого самокат»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле «Имя»
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле «Фамилия»
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле «Адрес»
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле «Станция метро»
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле «Телефон»
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # Кнопка «Далее»

    # Шаг 2 — «Про аренду»
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле «Когда привезти самокат»
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")  # Выпадающий список «Срок аренды»
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Поле «Комментарий для курьера»
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")  # Кнопка «Заказать» под формой

    # Модальные окна
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")  # Кнопка «Да» в окне «Хотите оформить заказ?»
    SUCCESS_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")  # Заголовок «Заказ оформлен»

    @staticmethod
    def metro_option(station):
        return By.XPATH, f"//div[contains(@class, 'Order_Text') and text()='{station}']"  # Станция в списке метро

    @staticmethod
    def rent_option(period):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"  # Срок аренды в выпадающем списке

    @staticmethod
    def color_checkbox(color):
        return By.ID, color  # Чекбокс цвета самоката: black или grey
