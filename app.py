""" Импортирование библиотеки для работы с Flask и запусков субпроцессов """

import subprocess
import webbrowser
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    """ Эта функция запускает и отвечает за процесс возврата результата index.html. """

    return render_template('index.html')

@app.route("/error")
def error():
    """ Эта функция запускает и отвечает за процесс возврата результата test_error.html. """
    return render_template('test_error.html')

@app.route('/run_ui')
def run_ui():
    """ Эта функция запуска всех UI тестов """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_header')
def run_ui_header():
    """ Эта функция запуска UI тестов хедера """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_header.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_footer')
def run_ui_footer():
    """ Эта функция запуска UI тестов футера """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_footer.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_mainmenu')
def run_ui_mainmenu():
    """ Эта функция запуска UI тестов главного меню сайта """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_mainmenu.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_search')
def run_ui_search():
    """ Эта функция запуска UI тестов инпута поиска """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_mainpage_info')
def run_ui_mainpage_info():
    """ Эта функция запуска UI тестов блоков информации главной страницы """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_mainpage_info.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_ui_management')
def run_ui_management():
    """ Эта функция запуска UI тестов блоков информации главной страницы """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_ui_management.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_api')
def run_api():
    """ Эта функция запуска Api тестов """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_api_page')
def run_api_page():
    """ Эта функция запуска Api тестов статуса кода страниц сайта """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_api_page.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_api_search')
def run_api_search():
    """ Эта функция запуска Api тестов статуса кода строки поиска """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_api_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_api_page_404')
def run_api_page_404():
    """ Эта функция запуска Api тестов статуса кода строк 404 """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_api_page_404.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_locust')
def run_locust():
    """ Эта функция запуска нагрузочного тестирования страниц сайта """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_locust.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/run_allure')
def run_allure():
    """ Эта функция запуска отчета Allure """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scriptsh/run_allure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
