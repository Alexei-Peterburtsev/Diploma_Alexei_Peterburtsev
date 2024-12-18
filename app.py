""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция запускает и отвечает за процесс возврата результата index.html. """

    return render_template('index.html')

@app.route('/ui_tests')
def ui_tests():
    """ Эта функция запуска всех UI авто тестов """

    cmd = ["./scriptsh/ui_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/ui_test_header_and_footer')
def ui_test_header_and_footer():
    """ Эта функция запуска UI тестов хедера и футера """

    cmd = ["./scriptsh/ui_test_header_and_footer.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/ui_test_main_menu')
def ui_test_main_menu():
    """ Эта функция запуска UI тестов главного меню сайта """

    cmd = ["./scriptsh/ui_test_main_menu.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/ui_test_search_input')
def ui_test_search_input():
    """ Эта функция запуска UI тестов инпута поиска """

    cmd = ["./scriptsh/ui_test_search_input.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/ui_test_main_page_info')
def ui_test_main_page_info():
    """ Эта функция запуска UI тестов блоков информации главной страницы """

    cmd = ["./scriptsh/ui_test_main_page_info.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/api_tests')
def api_tests():
    """ Эта функция запуска Api тестов """

    cmd = ["./scriptsh/api_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/all_allure')
def all_allure():
    """ Эта функция запуска отчетов Allure """

    cmd = ["./scriptsh/all_allure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

@app.route('/locus_tests')
def locus_tests():
    """ Эта функция запуска нагрузочного тестирования страниц сайта """

    cmd = ["./scriptsh/locus_tests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)











# @app.route("/error")
# def error():
#     """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
#     return render_template('test_error.html')
#
#
# @app.route("/runallure")
# def run_allure():
#     """ Эта функция запуская и отвечает за генерацию отчета allure. """
#
#     cmd = ["./scriptsh/runallure.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('index.html', text=out, json=out)
#
#
# @app.route("/run_ui")
# def run_ui():
#     """ Эта функция запуская и отвечает за тесты страницы /example. """
#
#     cmd = ["./scriptsh/run_aut_lk.sh"]
#     with subprocess.Popen(cmd, stdout=subprocess.PIPE,
#                           stderr=subprocess.PIPE,
#                           stdin=subprocess.PIPE,
#                           universal_newlines=True) as result:
#         out = result.communicate()
#     return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
