import os

from page.base_page import WebPage
from page.elements import WebElement

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://komarovka.by/about/rukovodstvo/"

        super().__init__(web_driver, url)

    management_foto_director = WebElement(xpath="//img[@title='Генеральный директор Хмельницкий.jpg']")
    management_foto_frst_zam = WebElement(xpath="//img[@title='Первый заместитель Бусло Н.К.1.jpg']")
    management_foto_zam_ideologia= WebElement(xpath="//img[@title='Томашевич.jpg']")
    management_foto_zam_bezopasnost = WebElement(xpath="//img[@title='Будько Александр Васильевич.jpg']")
    management_foto_zam_razvitie = WebElement(xpath="//img[@title='Ткачук Иван Алексеевич.jpg']")
    management_foto_zam_glingener = WebElement(xpath="//img[@title='IMG08322 копия.jpg']")

    management_fio_director = WebElement(xpath="//div[@class='col-md-9']//div[1]//p[1]")
    management_fio_frst_zam = WebElement(xpath="//div[@class='col-md-9']//div[2]//p[1]")
    management_fio_zam_ideologia= WebElement(xpath="//div[@class='col-md-9']//div[3]//p[1]")
    management_fio_zam_bezopasnost = WebElement(xpath="//div[@class='col-md-9']//div[4]//p[1]")
    management_fio_zam_razvitie = WebElement(xpath="//div[@class='col-md-9']//div[5]//p[1]")
    management_fio_zam_glingener = WebElement(xpath="")





