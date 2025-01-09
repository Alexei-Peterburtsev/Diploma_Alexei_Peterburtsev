"""Тестирование сайта КТУП Минский Комаровский рынок"""

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

@allure.story("Проверка хедера")

def test_header_btn(web_browser):
    """Этот тест проверяет хедер на наличие логотипа, кнопки на кликабельность, отображение, орфографию, ссылку url, переход по url"""

    page = MainPage(web_browser)

    # Элементы хедера с текстом:

    header_elements_menu = [(page.header_btn_about, "О нас", "https://komarovka.by/about/"),
                            (page.header_btn_buyer, "Покупателю", "https://komarovka.by/pokupatelyu/"),
                            (page.header_btn_tenant, "Арендатору", "https://komarovka.by/arendatoru/"),
                            (page.header_btn_services, "Услуги", "https://komarovka.by/uslugi/"),
                            (page.header_btn_appeals, "Обращения", "https://komarovka.by/elektronnye-obrashcheniya/"),
                            (page.header_btn_ru, "RU", "https://komarovka.by/"),
                            (page.header_btn_by, "BY", "https://komarovka.by/by/"),
                            ]

    # Элементы хедера без текста:

    header_special_elements = [(page.header_btn_special_ver, "Версия для слабовидящих"),
                               (page.header_img, "Логотип"),
                               (page.header_input_find_first, "Поиск по сайту первое поле ввода"),
                               (page.header_btn_search_first, "Поиск по сайту первая кнопка")
                               ]

    # Элементы хедера с переходом на другой сайт:

    header_btn_elements = [(page.header_btn_facebook, "facebook", "https://www.facebook.com/komarovka.by/"),
                           (page.header_btn_instagram, "instagram", "https://www.instagram.com/komarovka.by/"),
                           (page.header_btn_tiktok, "tiktok", "https://www.tiktok.com/@komarovka.by")
                           ]

    # Проверка элементов хедера с переходом на другой сайт:

    switch_window_header = 1
    for btn_elements, text_btn_elements, url_btn_elements in header_btn_elements:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(btn_elements.is_visible(), f"Элемент '{text_btn_elements}' отсутствует на экране")
        with allure.step("Тест проверки кликабельности"):
            check.is_true(btn_elements.is_clickable(), f"Элемент '{text_btn_elements}' не кликабелен")
            with allure.step("Тест проверки правильного адреса URL"):
                check.equal(btn_elements.get_attribute("href"), url_btn_elements, f"Элемент '{text_btn_elements}' содержит неправильную ссылку url")
        with allure.step("Тест проверки правильного адреса при переходе"):
            btn_elements.click()
            page.switch_to_window(switch_window_header)
            check.equal(page.get_current_url(), url_btn_elements, f"Элемент '{text_btn_elements}' переходит на неправильную ссылку url")
            page.switch_to_window(0)
        switch_window_header += 1

    # Проверка элементов хедера без текста:

    for special_elements, text_special_elements in header_special_elements:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(special_elements.is_visible(), f"Элемент '{text_special_elements}' отсутствует на экране")
        with allure.step("Тест проверки кликабельности"):
            check.is_true(special_elements.is_clickable(), f"Элемент '{text_special_elements}' не кликабелен")

    # Проверка элементов хедера с текстом:

    for elements, elements_text, elements_url in header_elements_menu:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
        with allure.step("Тест проверки кликабельности"):
            check.is_true(elements.is_clickable(), f"Элемент '{elements_text}' не кликабелен")
        with allure.step("Тест проверки орфографии"):
            check.equal(elements.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")
        with allure.step("Тест проверки правильного адреса URL"):
            check.equal(elements.get_attribute("href"), elements_url, f"Элемент '{elements_text}' содержит неправильную ссылку url")
        with allure.step("Тест проверки правильного адреса при переходе"):
            elements.click()
            check.equal(page.get_current_url(), elements_url, f"Элемент '{elements_text}' переходит на неправильную ссылку url")
