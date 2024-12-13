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
@allure.feature("Проверка элементов на главной странице")

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

    main_page_greetings = [(page.main_page_greetings, "Добро пожаловать на главный рынок столицы!")] # Заглавные буквы

    for elements, elements_text in main_page_greetings:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
        with allure.step("Тест проверки орфографии"):
            check.equal(elements.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")
