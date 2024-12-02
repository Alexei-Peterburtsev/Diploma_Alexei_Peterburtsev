import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://komarovka.by/"

        super().__init__(web_driver, url)

    header_img = WebElement(xpath="//img[@class='img-responsive logo']")

    header_btn_about = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'О нас')]")
    header_btn_buyer = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Покупателю')]")
    header_btn_tenant = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Арендатору')]")
    header_btn_services = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Услуги')]")
    header_btn_appeals = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Обращения')]")
