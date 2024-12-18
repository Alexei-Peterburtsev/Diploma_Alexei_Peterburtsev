'''Тестирование сайта КТУП Минский Комаровский рынок'''

import requests
import allure
import pytest
import pytest_check as check

@allure.feature("Апи тесты")
@pytest.mark.parametrize("url", ["/about/",
                                 "/pokupatelyu/",
                                 "/arendatoru/",
                                 "/uslugi/",
                                 "/elektronnye-obrashcheniya/"
                                 ]
                         )

def test_url(url):
    '''Этот тест проверяет статус код страниц главного меню'''

    site_response = requests.get(f"https://komarovka.by{url}", verify=False)

    with allure.step("Тест статус кода"):
        check.equal(site_response.status_code, 200, "Статус код не равен 200")

def test_url_search():
  '''Этот тест проверяет статус код страниц поиска по сайту'''

  url = "https://komarovka.by/search/?q=%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80&s=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA+%D0%BF%D0%BE+%D1%81%D0%B0%D0%B9%D1%82%D1%83"

  payload = {}
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Cookie': '_ym_uid=1716820155618093877; BX_USER_ID=b478b124f190fe38080a0ab55746bd56; _ym_d=1733734439; PHPSESSID=0URaZEpRCbE8KDFa1Z2LV3bfVLuLF1Uh',
    'Referer': 'https://komarovka.by/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  site_response = requests.request("GET", url, headers=headers, data=payload)

  with allure.step("Тест статус кода"):
    check.equal(site_response.status_code, 200, "Статус код не равен 200")
