"""Тестирование сайта КТУП Минский Комаровский рынок"""

import requests
import allure
import pytest
import pytest_check as check

@allure.story("Апи тесты страниц 404 сайта")
@pytest.mark.parametrize("url", ["/about/asd",
                                 "/pokupately_u/",
                                 "/arendatoru!/",
                                 "/uslugii/",
                                 "/elektronnye-obrashcheniya000/"
                                 ]
                         )

def test_url(url):
    """Этот тест проверяет статус код несуществующих страниц сайта"""

    site_response = requests.get(f"https://komarovka.by{url}", verify=False)

    with allure.step("Тест статус кода"):
        check.equal(site_response.status_code, 404, "Статус код не равен 404")
