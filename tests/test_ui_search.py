'''Тестирование сайта КТУП Минский Комаровский рынок'''

import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser
from locators.locators_main_page import ManyWebElements

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story("Проверка инпута поиска")

def test_first_search_input(web_browser):
    '''Этот тест проверяет первую строку поиска'''

    page = MainPage(web_browser)

    with allure.step("Проверка на ввод текста в первую строку поиска"):
        test_text_search_one = "директор"
        page.header_input_find_first.send_keys(test_text_search_one)
        page.header_btn_search_first.click(1)
        time.sleep(2)
        text_search_one = page.main_search_input_results.get_text()
        check.not_equal(text_search_one.find(f'{test_text_search_one}'), text_search_one, "Результаты поиска не соответствуют запросу")


def test_second_search_input(web_browser):
    '''Этот тест проверяет вторую строку поиска'''

    page = MainPage(web_browser)

    with allure.step("Проверка на ввод текста во вторую строку поиска"):
        test_text_search_two = "главный инженер"
        page.header_input_find_second.send_keys(test_text_search_two)
        page.header_btn_search_second.click(1)
        time.sleep(2)
        text_search_two = page.main_search_input_results.get_text()
        check.not_equal(text_search_two.find(f'{test_text_search_two}'), text_search_two, "Результаты поиска не соответствуют запросу")
