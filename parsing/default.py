"""Libraries"""
import re
import string
import xlsxwriter as xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
from bs4 import BeautifulSoup

################# Ввод данных ##########################################################################################
"""Link"""
main_link = 'https://google.com'  # адрес

"""Authorization"""
main_login = 'admin'  # логин
main_password = '123123123'  # пароль

"""Project folder"""
main_path = 'C:\Parsing'  # папка с проектом
product_name = 'google'  # название продукта
product_path = os.path.join(main_path, product_name)  # папка с проектом
if not os.path.exists(product_path):  # проверка (создана папка или нет)
    os.mkdir(product_path)  # создание папки с названием продукта

"""Artifact file"""
artifact_name = 'artifact.txt'   # файл с артефактами
artifact_path = os.path.join(main_path, artifact_name)   # путь хранения файла с артефактами

"""Time"""
module_time = 20  # максимальное время на появление элемента
screenshot_time = 1  # время на создание скриншота

"""Driver"""
driver_name = 'chromedriver.exe'  # драйвер
driver_path = os.path.join(main_path, driver_name)
driver_service = Service(driver_path)
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()  # работа браузера в максимальном окне

################# Функции ##############################################################################################


def request_xpath(xpath, header_module,  # переход на элемент и сбор данных
                  header_module_element,  # пример ("//*[@class='navigation-panel']//*[@class='ng-star-inserted'][1]",
                  title_element):  # 'main_module', 'organization', 'organization_add')

    """Module folder"""
    module_name = header_module  # название модуля
    module_path = os.path.join(product_path, module_name)  # папка с модулем
    if not os.path.exists(module_path):
        os.mkdir(module_path)  # создание папки с названием модуля (в папке с названием продукта)

    """Element folder"""
    element_name = header_module_element  # название элемента
    element_path = os.path.join(module_path, element_name)  # папка с элементом
    if not os.path.exists(element_path):
        os.mkdir(element_path)  # создание папки с названием элемента (в папке с названием модуля)

    """Collection"""
    os.chdir(main_path)
    driver.implicitly_wait(module_time)  # ожидание элемента
    search = driver.find_element(By.XPATH, xpath)  # поиск элемента, по методу XPATH
    search.click()  # нажатие
    time.sleep(screenshot_time)  # таймаут 1 секунда
    os.chdir(element_path)
    driver.save_screenshot(title_element + '.png')  # скриншот
    os.chdir(main_path)
    search = driver.page_source
    soup = BeautifulSoup(search, 'html.parser')
    get = set([str.lower(text) for text in soup.stripped_strings])
    with open('artifact.txt', encoding='utf-8', mode='r') as file:
        os.chdir(element_path)
        output = {}
        for line in file:
            for el in get:
                if el == "":
                    continue
                line = line.strip()
                for i in ['.', '+', '*', '?', '^', '$', '(', ')', '[', ']', '{', '}', '|']:
                    line = line.replace(i, '\\{}'.format(i))
                for i in list(string.punctuation):
                    el = el.replace(i, '')
                reg = re.compile(r"\s{2,}")
                el = el.replace("\n", " ").replace("\t", " ")
                el = re.sub(reg, " ", el)
                el = el.lstrip()

                if re.compile(r'\b{}\b'.format(line.lower())).search(el):
                    value = output.get(el, None)
                    if value is not None:
                        output[el] += [line.strip()]
                    else:
                        output[el] = [line.strip()]

        if len(output) == 0:
            return

        book = xlsxwriter.Workbook(title_element + '.xlsx')  # создание xlsx
        sheet = book.add_worksheet()  # страница в xlsx
        red = book.add_format({"bold": True, "color": "red"})  # окрашивание текста в красный цвет
        r = 0
        for key, value in output.items():
            sheet.write_string(r, 0, ", ".join(set(value)))  # текст артефактов
            array = []
            for k in key.split(' '):
                for v in value:
                    if k == v:
                        array += [red]
                        break
                array += [k, " "]
            sheet.write_rich_string(r, 1, *array)  # найденные артефакты
            sheet.write_string(r, 2, driver.current_url)  # ссылка на найденный элемент
            r += 1
        book.close()  # закрытие xlsx


def response_xpath(xpath, header_module,  # переход на элемент и ввод данных
                   header_module_element,  # пример ("//*[@class='navigation-panel']//*[@class='ng-star-inserted'][1]",
                   title_window):  # 'main_module', 'organization', 'ввод текста')

    """Module folder"""
    module_name = header_module
    module_path = os.path.join(product_path, module_name)
    if not os.path.exists(module_path):
        os.mkdir(module_path)

    """Element folder"""
    element_name = header_module_element
    element_path = os.path.join(module_path, element_name)
    if not os.path.exists(element_path):
        os.mkdir(element_path)

    os.chdir(element_path)

    """Response"""
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.clear()  # очистка строки
    search.send_keys(title_window)  # ввод данных


def click_xpath(xpath):  # переход на элемент и нажатие

    """Click"""
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.click()  # нажатие

########################################################################################################################


try:
    ################# Browser ##########################################################################################
    driver.implicitly_wait(module_time)
    driver.get(main_link)  # открытие ссылки бразуера

    ################# Authorization Window #############################################################################
    """Authorization Main"""
    request_xpath(
        "//*[@class='dropdown-toggle language-dropdown-toggle']",
        'Window Module', 'Authorization Window', 'Authorization Main'
    )

    """Authorization Username"""
    response_xpath(
        "//*[@id='UserName']", 'Window Module', 'Authorization Window', main_login
    )

    """Authorization Password"""
    response_xpath(
        "//*[@id='Password']", 'Window Module', 'Authorization Window', main_password
    )

    """Authorization Button"""
    click_xpath(
        "//*[@id='login-button']"
    )

########################################################################################################################
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
