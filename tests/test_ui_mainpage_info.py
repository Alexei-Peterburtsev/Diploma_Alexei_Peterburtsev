'''Тестирование сайта КТУП Минский Комаровский рынок'''

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser
from locators.locators_main_menu_many import MainPageElements

@allure.story("Проверка элементов на главной странице")

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

def test_all_menu_header(web_browser):
    '''Этот тест проверят количество пунктов в главном меню'''

    page = MainPageElements(web_browser)

    with allure.step("Тест количества пунктов в главном меню"):
        check.equal(page.main_page_all_menu_header.count(), 5, "Количество пунктов в главном меню не 5")
