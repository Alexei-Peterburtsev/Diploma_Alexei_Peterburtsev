import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://nhl.ru/'

        super().__init__(web_driver, url)

    header_btn_start = WebElement(xpath='//a[@id="mi_0_0"]')
    header_btn_team = WebElement(xpath='//a[@id="mi_0_1"]')
    header_btn_read = WebElement(xpath='//a[@id="mi_0_37"]')
    header_btn_findout = WebElement(xpath='//a[@id="mi_0_40"]')
    header_btn_look = WebElement(xpath='//a[@id="mi_0_67"]')
    header_btn_play = WebElement(xpath='//a[@id="mi_0_71"]')
    header_btn_communicate = WebElement(xpath='//a[@id="mi_0_79"]')

    footer_btn_support = WebElement(xpath='//area[@alt="Поддержи NHL.RU"]')
    footer_btn_pay = WebElement(xpath='//area[@alt="Платные услуги"]')
    footer_btn_ad = WebElement(xpath='//area[@alt="Реклама на NHL.RU"]')
    footer_btn_contacts = WebElement(xpath='//area[@alt="Контакты"]')