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
    '''Этот тест проверяет кнопки меню хедера на наличие логотипа, кнопки на кликабельность, отображение, орфографию, ссылку url, переход по url'''

    page = MainPage(web_browser)

    header_elements_menu = [(page.header_btn_about, "О нас", "https://komarovka.by/about/"),
                            (page.header_btn_buyer, "Покупателю", "https://komarovka.by/pokupatelyu/"),
                            (page.header_btn_tenant, "Арендатору", "https://komarovka.by/arendatoru/"),
                            (page.header_btn_services, "Услуги", "https://komarovka.by/uslugi/"),
                            (page.header_btn_appeals, "Обращения", "https://komarovka.by/elektronnye-obrashcheniya/"),
                            (page.header_btn_ru, "RU", "https://komarovka.by/"),
                            (page.header_btn_by, "BY", "https://komarovka.by/by/")
                            ]

    with allure.step("Тест проверки отображения логотипа"):
        check.is_true(page.header_img.is_visible(), "Логотип отсутствует")

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
