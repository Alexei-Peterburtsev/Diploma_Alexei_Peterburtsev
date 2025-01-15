"""Тестирование сайта КТУП Минский Комаровский рынок"""

import requests
import allure
import pytest_check as check

@allure.epic("Тестирование сайта https://komarovka.by")
@allure.feature("API тесты")
@allure.story("Проверка страниц сайта")
@allure.label("owner", "Алексей Петербурцев")

def test_url():
    """Этот тест проверяет статус код страниц главного меню"""

    site_response = requests.get("https://komarovka.by/about/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/about/"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")

    site_response = requests.get("https://komarovka.by/pokupatelyu/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/pokupatelyu/"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")

    site_response = requests.get("https://komarovka.by/arendatoru/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/arendatoru/"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")

    site_response = requests.get("https://komarovka.by/uslugi/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/uslugi/"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")

    site_response = requests.get("https://komarovka.by/elektronnye-obrashcheniya/", verify=False)
    with allure.step("Тест статус кода страницы: https://komarovka.by/elektronnye-obrashcheniya/"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")
