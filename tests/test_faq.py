import allure
import pytest

from data import FAQ


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("По клику на вопрос открывается соответствующий ответ")
    @pytest.mark.parametrize("index, expected_answer", FAQ)
    def test_faq_question_opens_answer(self, main_page, index, expected_answer):
        main_page.open_faq_question(index)

        assert main_page.get_faq_answer(index) == expected_answer
