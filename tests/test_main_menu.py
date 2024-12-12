'''Тестирование сайта КТУП Минский Комаровский рынок'''

import time

import allure
import pytest_check as check
from conftest import web_browser
from locators.locators_main_menu import MainPageElements

from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.story("Тест для проверки главной страницы")
@allure.feature("Проверка количества пунктов в главном меню")

def test_all_menu_header(web_browser):

    page = MainPageElements(web_browser)

    with allure.step("Тест количества пунктов в главном меню"):
        check.equal(page.main_page_all_menu_header.count(), 5, "Количество пунктов в главном меню не 5")