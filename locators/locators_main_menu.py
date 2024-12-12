import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPageElements(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://komarovka.by/"

        super().__init__(web_driver, url)

    main_page_all_menu_header = ManyWebElements(xpath="//li[@class='with-submenu']")
