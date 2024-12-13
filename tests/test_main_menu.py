'''Тестирование сайта КТУП Минский Комаровский рынок'''

import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser
from locators.locators_main_page import ManyWebElements

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story("Тест для проверки главной страницы")
@allure.feature("Проверка главного меню")

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
