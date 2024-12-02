import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story('Тест для проверки главной страницы')
@allure.feature('Проверки кнопок хедара и футера')

def test_btn_header_page(web_browser):
    ''''это тест проверяет меню хедера на кликабельность, отображение, орфографию'''

    page = MainPage(web_browser)

    header_elements = [(page.header_btn_start, 'Начало', 'https://nhl.ru/index.php'),
                       (page.header_btn_team, 'Команды', 'https://nhl.ru/null'),
                       (page.header_btn_read, 'Читай', 'https://nhl.ru/null'),
                       (page.header_btn_findout, 'Узнай', 'https://nhl.ru/null'),
                       (page.header_btn_look, 'Смотри', 'https://nhl.ru/null'),
                       (page.header_btn_play, 'Играй', 'https://nhl.ru/null'),
                       (page.header_btn_communicate, 'Общайся', 'https://nhl.ru/null')
                       ]

    for elements, elements_text, elements_url in header_elements:

        with allure.step('Тест проверки отображения на экране'):
            check.is_true(elements.is_visible())

        with allure.step('Тест проверки кликабельности'):
            check.is_true(elements.is_clickable())

        with allure.step('Тест проверки орфографии'):
            check.equal(elements.get_text(), elements_text)

        with allure.step('Тест проверки правильного адреса URL'):
            check.equal(elements.get_attribute('href'), elements_url)

        # with allure.step('Тест проверки правильного адреса при переходе'):
        #     elements.click()
        #     check.equal(page.get_current_url(), elements_url)


# def test_btn_footer_page(web_browser):
#     ''''это тест проверяет меню футера на кликабельность, отображение, орфографию'''
#
#     page = MainPage(web_browser)
#
#     footer_elements = [page.footer_btn_support,
#                        page.footer_btn_pay,
#                        page.footer_btn_ad,
#                        page.footer_btn_contacts
#                        ]
#
#     for ele_footer in footer_elements:
#
#         with allure.step('Тест проверки отображения на экране'):
#             check.is_true(ele_footer.is_visible())