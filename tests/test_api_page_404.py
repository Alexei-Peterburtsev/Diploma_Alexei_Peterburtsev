"""Тестирование сайта КТУП Минский Комаровский рынок"""

import requests
import allure
import pytest
import pytest_check as check

@allure.epic("Тестирование сайта https://komarovka.by")
@allure.feature("API тесты")
@allure.story("Проверка страниц 404 сайта")
@allure.label("owner", "Алексей Петербурцев")

def test_url():
    """Этот тест проверяет статус код несуществующих страниц сайта"""

    site_response = requests.get("https://komarovka.by/abooout/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/abooout/"):
        check.equal(site_response.status_code, 404, "Статус код не равен 404")

    site_response = requests.get("https://komarovka.by/poookupatelyu/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/poookupatelyu/"):
        check.equal(site_response.status_code, 404, "Статус код не равен 404")

    site_response = requests.get("https://komarovka.by/arendatoooru/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/arendatoooru/"):
        check.equal(site_response.status_code, 404, "Статус код не равен 404")
