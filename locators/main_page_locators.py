from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")  # Кнопка «да все привыкли» в баннере куки
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")  # Кнопка «Заказать» в шапке
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")  # Кнопка «Заказать» внизу страницы
    FAQ_SECTION = (By.CLASS_NAME, "accordion")  # Блок «Вопросы о важном»

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"  # Вопрос в списке «Вопросы о важном»

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"  # Ответ на вопрос в списке «Вопросы о важном»


class HeaderLocators:
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Логотип «Самоката»
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Логотип Яндекса
