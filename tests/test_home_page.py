import allure
import pytest

import data


class TestHomePage:

    @pytest.mark.parametrize("index, expected_text", data.question_answer)
    @allure.title("Проверка списка в разделе 'О важном'")
    @allure.description("Для каждого вопроса в разделе открываем его текст и проверяем на соответствие")
    def test_faq_question_shows_correct_answer(self, index, expected_text, home_page):
        text = home_page.get_faq_text_by_index(index)

        assert text == expected_text, \
            f"Ошибка в тексте элемента {index}"
