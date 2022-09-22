"""libraries"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup

################# вводим данные ########################################################################################
"""link"""
main_link = 'https://smp.bestsafety.tech:1443/'  # доменное имя

"""authorization"""
main_login = 'admin'  # логин
main_password = 'GH1-15J-fgU-1MP'  # пароль

"""main_folder"""
main_path = 'C:\Parsing'  # папка с проектом
product_name = 'prime'  # название продукта

"""artifact_file"""
artifact_name = 'artifact.txt'   # файл с артефактами
artifact_path = os.path.join(main_path, artifact_name)   # путь хранения файла с артефактами

"""main_time"""
module_time = 20  # максимальное время на появление элемента
screenshot_time = 1  # время на создание скриншота

########################################################################################################################

"""driver"""
driver = webdriver.Chrome(".\chromedriver.exe")  # инициализация веб-драйвера
driver.maximize_window()  # работа браузера в максимальном окне

"""project_folder"""
product_path = os.path.join(main_path, product_name)  # папка с проектом
if not os.path.exists(product_path):  # проверка (создана папка или нет)
    os.mkdir(product_path)  # создание папки с названием продукта


def request_xpath(xpath, header_module,  # переход на элемент и сбор данных
                  header_module_element,  # пример ("//*[@class='navigation-panel']//*[@class='ng-star-inserted'][1]",
                  title_element):  # 'main_module', 'organization', 'organization_add')

    """module_folder"""
    module_name = header_module  # название модуля
    module_path = os.path.join(product_path, module_name)  # папка с модулем
    if not os.path.exists(module_path):
        os.mkdir(module_path)  # создание папки с названием модуля (в папке с названием продукта)

    """element_folder"""
    element_name = header_module_element  # название элемента
    element_path = os.path.join(module_path, element_name)  # папка с элементом
    if not os.path.exists(element_path):
        os.mkdir(element_path)  # создание папки с названием элемента (в папке с названием модуля)

    os.chdir(element_path)  # обращение к пути

    """collection"""
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

    """module_folder"""
    module_name = header_module  # название модуля
    module_path = os.path.join(product_path, module_name)  # папка с модулем
    if not os.path.exists(module_path):
        os.mkdir(module_path)  # создание папки с названием модуля (в папке с названием продукта)

    """element_folder"""
    element_name = header_module_element  # название элемента
    element_path = os.path.join(module_path, element_name)  # папка с элементом
    if not os.path.exists(element_path):
        os.mkdir(element_path)  # создание папки с названием элемента (в папке с названием модуля)

    os.chdir(element_path)  # обращение к пути

    """response"""
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.clear()  # очистка строки
    search.send_keys(title_window)  # ввод данных


def click_xpath(xpath):  # переход на элемент и нажатие
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.click()  # нажатие


try:
    ################# browser ##########################################################################################
    driver.implicitly_wait(module_time)
    driver.get(main_link)  # открытие ссылки бразуера

    ################# authorization_window #############################################################################
    """authorization_main"""
    request_xpath(
        "//*[@class='dropdown-toggle language-dropdown-toggle']",
        'window_module', 'authorization_window', 'authorization_main'
    )

    """authorization_username"""
    response_xpath(
        "//*[@id='UserName']", 'window_module', 'authorization_window', main_login
    )

    """authorization_password"""
    response_xpath(
        "//*[@id='Password']", 'window_module', 'authorization_window', main_password
    )

    """authorization_button"""
    click_xpath(
        "//*[@id='login-button']"
    )

########################################################################################################################
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
