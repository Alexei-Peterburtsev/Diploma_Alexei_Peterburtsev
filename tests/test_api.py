'''Тестирование сайта КТУП Минский Комаровский рынок'''

import requests
import allure
import pytest
import pytest_check as check

@allure.feature("Апи тесты")
@pytest.mark.parametrize("url", ["/about/",
                                 "/pokupatelyu/",
                                 "/arendatoru/",
                                 "/uslugi/",
                                 "/elektronnye-obrashcheniya/"
                                 ]
                         )

def test_url(url):
    '''Этот тест проверяет статус код страниц главного меню'''

    respons = requests.get(f"https://komarovka.by{url}", verify=False)

    with allure.step("Тест статус кода"):
        check.equal(respons.status_code, 200, "Статус код не равен 200")
