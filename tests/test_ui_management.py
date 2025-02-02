"""Тестирование сайта КТУП Минский Комаровский рынок"""

import allure
import pytest_check as check
from locators.locators_management import MainPage
from conftest import web_browser

@allure.epic("Тестирование сайта https://komarovka.by")
@allure.feature("UI тесты")
@allure.story("Проверка страницы руководства")
@allure.label("owner", "Алексей Петербурцев")

def test_management(web_browser):

    """Этот тест проверят наличие фотографий руководителей, должности, фамилии"""

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

    page = MainPage(web_browser)

    management_fio = [(page.management_fio_director, "Генеральный директор: Хмельницкий Николай Михайлович"),
                      (page.management_fio_frst_zam, "Первый заместитель генерального директора: Бусло Николай Кириллович"),
                      (page.management_fio_zam_ideologia, "Заместитель генерального директора по идеологической работе и социальным вопросам: \nТомашевич Людмила Михайловна"),
                      (page.management_fio_zam_razvitie, "Заместитель генерального директора по развитию: Ткачук Иван Алексеевич"),
                      (page.management_fio_zam_bezopasnost, "Заместитель генерального директора по безопасности: Будько Александр Васильевич")
                      ]

    for elements_fio, elements_text in management_fio:
        with allure.step("Тест проверки отображения на экране"):
            check.is_true(elements_fio.is_visible(), f"Элемент '{elements_text}' отсутствует на экране")
        with allure.step("Тест проверки орфографии"):
            check.equal(elements_fio.get_text(), elements_text, f"Текст элемента '{elements_text}' содержит ошибку")
