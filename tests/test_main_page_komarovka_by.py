'''Тестирование сайта КТУП Минский Комаровский рынок'''

import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story("Тест для проверки главной страницы")
@allure.feature("Проверка кнопок хедера и футера")

def test_header_btn(web_browser):
    '''Этот тест проверяет хедер на наличие логотипа, кнопки на кликабельность, отображение, орфографию, ссылку url, переход по url'''

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

def test_futer_btn(web_browser):
    '''Этот тест проверяет футер на наличие логотипа, кнопки на кликабельность, отображение, орфографию, ссылку url, переход по url'''

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

def test_first_search_input(web_browser):
    '''Этот тест проверяет первую строку поиска'''

    page = MainPage(web_browser)

    with allure.step("Проверка на ввод текста в первую строку поиска"):
        test_text_search_one = "директор"
        page.header_input_find_first.send_keys(test_text_search_one)
        page.header_btn_search_first.click(1)

def test_second_search_input(web_browser):
    '''Этот тест проверяет вторую строку поиска'''

    page = MainPage(web_browser)

    with allure.step("Проверка на ввод текста во вторую строку поиска"):
        test_text_search_two = "главный инженер"
        page.header_input_find_second.send_keys(test_text_search_two)
        page.header_btn_search_second.click(1)

def test_all_main_menu(web_browser):
    '''Этот тест проверят главное меню на открытие пунктов, их наличие, кликабельность, орфографию, ссылки, переходы по ссылкам'''

    page = MainPage(web_browser)

    # Элементы 1-го пункта главного меню:

    main_menu1_elements = [(page.main_menu1_btn_today, "Рынок сегодня", "https://komarovka.by/about/rynok-segodnya/"),
                           (page.main_menu1_btn_story, "История", "https://komarovka.by/about/istoriya/"),
                           (page.main_menu1_btn_management, "Руководство", "https://komarovka.by/about/rukovodstvo/"),
                           (page.main_menu1_btn_structure, "Структура предприятия", "https://komarovka.by/about/struktura-predpriyatiya/"),
                           (page.main_menu1_btn_public, "Общественные объединения", "https://komarovka.by/about/obshchestvennye-obedineniya/"),
                           (page.main_menu1_btn_news, "Новости", "https://komarovka.by/about/news/"),
                           (page.main_menu1_btn_vacancies, "Вакансии", "https://komarovka.by/about/vacancii/"),
                           (page.main_menu1_btn_gallery, "Фотогалерея", "https://komarovka.by/about/fotogalereya/"),
                           (page.main_menu1_btn_directions, "Схема проезда", "https://komarovka.by/about/skhema-proezda/"),
                           (page.main_menu1_btn_smi, "СМИ о нас", "https://komarovka.by/about/smi-o-nas/"),
                           (page.main_menu1_btn_contacts, "Контакты", "https://komarovka.by/about/contacts/"),
                           (page.main_menu1_btn_corruption, "Противодействие коррупции", "https://komarovka.by/about/protivodeystvie-korruptsii/")
                           ]

    # Элементы 2-го пункта главного меню:

    main_menu2_elements = [(page.main_menu2_btn_info, "Полезная информация", "https://komarovka.by/pokupatelyu/poleznaya-informatsiya/"),
                           (page.main_menu2_btn_market, "Схема рынка", "https://komarovka.by/pokupatelyu/skhema-rynka/"),
                           (page.main_menu2_btn_own_production, "Собственное производство", "https://komarovka.by/pokupatelyu/sobstvennoe-proizvodstvo/")
                           ]

    # Элементы 3-го пункта главного меню:

    main_menu3_elements = [(page.main_menu3_btn_order, "Порядок предоставления торговых объектов (мест)", "https://komarovka.by/arendatoru/torgovye-mesta/"),
                           (page.main_menu3_btn_rent, "Предлагаем в аренду", "https://komarovka.by/arendatoru/predlagaem-v-arendu/")
                           ]

    # Элементы 4-го пункта главного меню:

    main_menu4_elements = [(page.main_menu4_btn_radio_center, "Радиоузел", "https://komarovka.by/uslugi/radiouzel/"),
                           (page.main_menu4_btn_laboratory, "Лаборатория", "https://komarovka.by/uslugi/laboratoriya/"),
                           (page.main_menu4_btn_health_center, "Здравпункт", "https://komarovka.by/uslugi/zdravpunkt/")
                           ]

    # Элементы 5-го пункта главного меню:

    main_menu5_elements = [(page.main_menu5_btn_appeals, "Электронные обращения", "https://komarovka.by/elektronnye-obrashcheniya/elektronnye-obrashcheniya/"),
                           (page.main_menu5_btn_reception, "Личный прием граждан и юридических лиц", "https://komarovka.by/elektronnye-obrashcheniya/lichnyy-priem/"),
                           (page.main_menu5_btn_book, "Книга замечаний и предложений", "https://komarovka.by/elektronnye-obrashcheniya/kniga-zamechaniy-i-predlozheniy/"),
                           (page.main_menu5_btn_list, "Перечень административных процедур", "https://komarovka.by/elektronnye-obrashcheniya/perechen-administrativnykh-protsedur/")
                           ]
    # Все элементы главного меню:

    main_menu_all_elements = [main_menu1_elements, main_menu2_elements, main_menu3_elements, main_menu4_elements, main_menu5_elements]

    main_menu_click_elements = [page.main_menu1_btn_open, page.main_menu2_btn_open, page.main_menu3_btn_open, page.main_menu4_btn_open, page.main_menu5_btn_open]

    # Проверка всех элементов главного меню:

    for menu_items in range(5):
        for elements, elements_text, elements_url in main_menu_all_elements[menu_items]:
            main_menu_click_elements[menu_items].click()
            with allure.step("Тест проверки отображения на экране"):
                check.is_true(elements.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
            with allure.step("Тест проверки орфографии"):
                check.equal(elements.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")
            with allure.step("Тест проверки кликабельности"):
                check.is_true(elements.is_clickable(), f"Элемент '{elements_text}' не кликабелен")
            with allure.step("Тест проверки правильного адреса URL"):
                check.equal(elements.get_attribute("href"), elements_url, f"Элемент '{elements_text}' содержит неправильную ссылку url")
            with allure.step("Тест проверки правильного адреса при переходе"):
                elements.click()
                check.equal(page.get_current_url(), elements_url, f"Элемент '{elements_text}' переходит на неправильную ссылку url")

def test_menu_info_items(web_browser):
    '''Этот тест проверят блоки информации на главной странице на их наличие'''

    page = MainPage(web_browser)

    # Блоки информации на главной странице:

    main_page_all_info_items = [(page.main_page_info_item1, "Блок информации правый"),
                                (page.main_page_info_item2, "Блок информации центральный"),
                                (page.main_page_info_item3, "Блок информации левый")
                                ]

    for elements, elements_text in main_page_all_info_items:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")

def test_menu_greetings(web_browser):
    '''Этот тест проверят приветствие на главной странице на наличие, орфографию'''

    page = MainPage(web_browser)

    main_page_greetings = [(page.main_page_greetings, "Добро пожаловать на главный рынок столицы!")]

    for elements, elements_text in main_page_greetings:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
        with allure.step("Тест проверки орфографии"):
            check.equal(elements.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")
