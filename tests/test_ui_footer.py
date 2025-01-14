"""Тестирование сайта КТУП Минский Комаровский рынок"""

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

@allure.epic("Тестирование сайта https://komarovka.by")
@allure.feature("UI тесты")
@allure.story("Проверка футера")
@allure.label("owner", "Алексей Петербурцев")

def test_futer_btn(web_browser):
    """Этот тест проверяет футер на наличие логотипа, кнопки на кликабельность, отображение, орфографию, ссылку url, переход по url"""

    page = MainPage(web_browser)

    # Элементы футера с текстом:

    futer_btn_elements = [(page.futer_btn_about, "О нас", "https://komarovka.by/about/"),
                          (page.futer_btn_buyer, "Покупателю", "https://komarovka.by/pokupatelyu/"),
                          (page.futer_btn_tenant, "Арендатору", "https://komarovka.by/arendatoru/"),
                          (page.futer_btn_services, "Услуги", "https://komarovka.by/uslugi/"),
                          (page.futer_btn_appeals, "Обращения", "https://komarovka.by/elektronnye-obrashcheniya/"),
                          (page.futer_btn_contact, "Контакты", "https://komarovka.by/about/contacts/"),
                          (page.futer_btn_questions, "Вопросы и ответы", "https://komarovka.by/faq/"),
                          (page.futer_btn_scheme, "Схема рынка", "https://komarovka.by/pokupatelyu/skhema-rynka/"),
                          (page.futer_btn_map, "Карта сайта", "https://komarovka.by/sitemap/"),
                          (page.futer_btn_dining, "Столовая", "https://komarovka.by/pokupatelyu/sobstvennoe-proizvodstvo/stolovaya-komarovka/"),
                          (page.futer_btn_travel, "Схема проезда", "https://komarovka.by/about/skhema-proezda/"),
                          (page.futer_btn_vacancies, "Вакансии", "https://komarovka.by/about/vacancii/")
                          ]

    # Элементы футера с переходом на другой сайт:

    futer_btn_elements_new_site = [(page.futer_btn_artis, "ArtisMedia", "http://www.artismedia.by/"),                   # в дереве http без 's'
                                   (page.futer_btn_facebook, "facebook", "https://www.facebook.com/komarovka.by/"),
                                   (page.futer_btn_instagram, "instagram", "https://www.instagram.com/komarovka.by/"),
                                   (page.futer_btn_tiktok, "tiktok", "https://www.tiktok.com/@komarovka.by")            # в дереве href без ссылки
                                   ]

    # Элементы футера без текста:

    futer_special_elements = [(page.futer_img, "Логотип"),
                              (page.futer_telefon, "Номер телефона"),
                              (page.futer_email, "Электронная почта")
                              ]

    # Проверка элементов футера без текста:

    for special_elements, text_special_elements in futer_special_elements:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(special_elements.is_visible(), f"Элемент '{text_special_elements}' отсутствует на экране")

    # Проверка элементов футера с текстом:

    for elements, elements_text, elements_url in futer_btn_elements:
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

    # Проверка элементов футера с переходом на другой сайт:

    switch_window_futer = 1
    for btn_elements, text_btn_elements, url_btn_elements in futer_btn_elements_new_site:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(btn_elements.is_visible(), f"Элемент '{text_btn_elements}' отсутствует на экране")
        with allure.step("Тест проверки кликабельности"):
            check.is_true(btn_elements.is_clickable(), f"Элемент '{text_btn_elements}' не кликабелен")
        with allure.step("Тест проверки правильного адреса URL"):
                check.equal(btn_elements.get_attribute("href"), url_btn_elements, f"Элемент '{text_btn_elements}' содержит неправильную ссылку url")
        with allure.step("Тест проверки правильного адреса при переходе"):
            btn_elements.click()
            page.switch_to_window(switch_window_futer)
            check.equal(page.get_current_url(), url_btn_elements, f"Элемент '{text_btn_elements}' переходит на неправильную ссылку url")
            page.switch_to_window(0)
        switch_window_futer += 1
