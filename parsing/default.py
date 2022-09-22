"""Libraries"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
from bs4 import BeautifulSoup

################# Ввод данных ##########################################################################################
"""Link"""
main_link = 'https://smp.bestsafety.tech:1443/'  # адрес

"""Authorization"""
main_login = 'admin'  # логин
main_password = 'GH1-15J-fgU-1MP'  # пароль

"""Project folder"""
main_path = 'C:\Parsing'  # папка с проектом
product_name = 'prime'  # название продукта
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

    os.chdir(element_path)  # обращение к пути

    """Collection"""
    driver.implicitly_wait(module_time)  # ожидание элемента
    search = driver.find_element(By.XPATH, xpath)  # поиск элемента, по методу XPATH
    search.click()  # нажатие
    time.sleep(screenshot_time)  # таймаут 1 секунда
    driver.save_screenshot(title_element + '.png')  # скриншот
    search = driver.page_source  # сбор данных
    soup = BeautifulSoup(search, 'html.parser')  # обработка парсером
    get = [text for text in soup.stripped_strings]  # обработка текста
    with open(artifact_path, "r") as file:  # открытие файла с артефактами
        for line in file:   # цикл текста с артефактами
            for el in get:  # цикл обработки текста
                if line.strip() in el:  # поиск совпадений
                    with open(title_element + '.txt', 'a') as f:  # открытие файла
                        f.write(el + '\n')  # запись совпадений


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
