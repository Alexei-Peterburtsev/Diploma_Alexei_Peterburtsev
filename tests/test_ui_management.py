"""Тестирование сайта КТУП Минский Комаровский рынок"""

import allure
import pytest_check as check
from locators.locators_management import MainPage
from conftest import web_browser

@allure.story("Проверка страницы руководства")

def test_management_foto(web_browser):
    """Этот тест проверят наличие фотографий руководителей"""

    page = MainPage(web_browser)

    management_foto = [(page.management_foto_director, "Фото генерального директора"),
                       (page.management_foto_frst_zam, "Фото первого заместителя"),
                       (page.management_foto_zam_ideologia, "Фото заместителя по идеологии"),
                       (page.management_foto_zam_razvitie, "Фото заместителя по развитию"),
                       (page.management_foto_zam_bezopasnost, "Фото заместителя по безопасности"),
                       (page.management_foto_zam_glingener, "Фото главного инженера")
                       ]

    for foto_elements, text_foto_elements in management_foto:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(foto_elements.is_visible(), f"Элемент '{text_foto_elements}' отсутствует на экране")

def test_management_fio(web_browser):
    """Этот тест проверят фамилии руководителей"""

    page = MainPage(web_browser)

    management_fio = [(page.management_fio_director, "Хмельницкий Николай Михайлович"),
                      (page.management_fio_frst_zam, "Бусло Николай Кириллович"),
                      (page.management_fio_zam_ideologia, "Томашевич Людмила Михайловна"),
                      (page.management_fio_zam_razvitie, "Ткачук Иван Алексеевич"),
                      (page.management_fio_zam_bezopasnost, "Будько Александр Васильевич")
                      ]

    for elements_fio, elements_text in management_fio:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements_fio.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
        # with allure.step("Тест проверки орфографии"):
        #     check.equal(elements_fio.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")