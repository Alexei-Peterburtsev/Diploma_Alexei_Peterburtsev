import os

from page.base_page import WebPage
from page.elements import WebElement
from page.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or "https://komarovka.by/"

        super().__init__(web_driver, url)

    header_btn_about = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'О нас')]")
    header_btn_buyer = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Покупателю')]")
    header_btn_tenant = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Арендатору')]")
    header_btn_services = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Услуги')]")
    header_btn_appeals = WebElement(xpath="//li[@class='with-submenu']//a[contains(text(),'Обращения')]")
    header_btn_ru = WebElement(xpath="//a[@class='active']")
    header_btn_by = WebElement(xpath="//a[normalize-space()='BY']")
    header_btn_facebook = WebElement(xpath="//div[@class='header-social hidden-mobile hidden-tablet']//a[1]")
    header_btn_instagram = WebElement(xpath="//div[@class='header-social hidden-mobile hidden-tablet']//a[2]")
    header_btn_tiktok = WebElement(xpath="//div[@class='header-social hidden-mobile hidden-tablet']//a[3]")
    header_btn_special_ver = WebElement(xpath="//a[@class='special-version hidden-mobile']")
    header_input_find_first = WebElement(xpath="(//input[@id='title-search-input'])[1]")
    header_btn_search_first = WebElement(xpath="(//button[@class='btn'])[1]")
    header_input_find_second = WebElement(xpath="(//input[@id='title-search-input'])[2]")
    header_btn_search_second = WebElement(xpath="(//button[@class='btn'])[2]")
    header_img = WebElement(xpath="//img[@class='img-responsive logo']")

    futer_img = WebElement(xpath="//img[@src='/include/logo_footer.svg']")
    futer_telefon = WebElement(xpath="//a[normalize-space()='+375(17)352-66-08']")
    futer_email = WebElement(xpath="//p[@class='hide-block']//a[@href='mailto:office@komarovka.by'][normalize-space()='office@komarovka.by']")
    futer_btn_about = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'О нас')]")
    futer_btn_buyer = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Покупателю')]")
    futer_btn_tenant = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Арендатору')]")
    futer_btn_services = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Услуги')]")
    futer_btn_appeals = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Обращения')]")
    futer_btn_contact = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Контакты')]")
    futer_btn_questions = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Вопросы и ответы')]")
    futer_btn_scheme = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Схема рынка')]")
    futer_btn_map = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Карта сайта')]")
    futer_btn_dining = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Столовая')]")
    futer_btn_travel = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Схема проезда')]")
    futer_btn_vacancies = WebElement(xpath="//ul[@class='bottom_main_menu']//a[contains(text(),'Вакансии')]")
    futer_btn_facebook = WebElement(xpath="//div[@class='footer-social']//a[1]")
    futer_btn_instagram = WebElement(xpath="//div[@class='footer-social']//a[2]")
    futer_btn_tiktok = WebElement(xpath="//div[@class='footer-social']//a[3]")
    futer_btn_artis = WebElement(xpath="//a[normalize-space()='ArtisMedia']")

    main_menu1_btn_open = WebElement(xpath="(//i[@class='fa fa-angle-right'])[1]")
    main_menu1_btn_today = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Рынок сегодня')]")
    main_menu1_btn_story = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'История')]")
    main_menu1_btn_management = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Руководство')]")
    main_menu1_btn_structure = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Структура предприятия')]")
    main_menu1_btn_public  = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Общественные объединения')]")
    main_menu1_btn_news = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Новости')]")
    main_menu1_btn_vacancies = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Вакансии')]")
    main_menu1_btn_gallery = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Фотогалерея')]")
    main_menu1_btn_directions = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Схема проезда')]")
    main_menu1_btn_smi = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'СМИ о нас')]")
    main_menu1_btn_contacts = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Контакты')]")
    main_menu1_btn_corruption = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Противодействие коррупции')]")

    main_menu2_btn_open = WebElement(xpath="(//i[@class='fa fa-angle-right'])[2]")
    main_menu2_btn_info = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Полезная информация')]")
    main_menu2_btn_market = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Схема рынка')]")
    main_menu2_btn_own_production = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Собственное производство')]")

    main_menu3_btn_open = WebElement(xpath="(//i[@class='fa fa-angle-right'])[3]")
    main_menu3_btn_order = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Порядок предоставления торговых объектов (мест)')]")
    main_menu3_btn_rent = WebElement(xpath="//ul[@class='sub-menu']/li/a[contains(text(),'Предлагаем в аренду')]")
