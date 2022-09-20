"""libraries"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup

################# вводим данные ########################################################################################
"""link"""
main_link = 'https://protelion.local/'  # доменное имя

"""authorization"""
main_login = 'admin'  # логин
main_password = '123123123'  # пароль

"""main_folder"""
main_path = 'C:\Parsing'  # папка с проектом
product_name = 'prime'  # название продукта

"""main_time"""
module_time = 20  # максимальное время на появление элемента
screenshot_time = 1  # время на создание скриншота

########################################################################################################################

"""driver"""
driver = webdriver.Chrome("./chromedriver.exe")  # инициализация веб-драйвера
driver.maximize_window()  # работа браузера в максимальном окне


def request_xpath(xpath, header_module,  # переход на элемент и сбор данных
                  header_module_element,  # пример ("//*[@class='navigation-panel']//*[@class='ng-star-inserted'][1]",
                  title_element):  # 'main_module', 'organization', 'organization_add')

    """project_folder"""
    product_path = os.path.join(main_path, product_name)  # папка с проектом
    if os.path.exists(product_path):  # проверка (создана папка или нет)
        pass  # 0 значение
    else:
        os.mkdir(product_path)  # создание папки с названием продукта

    """module_folder"""
    module_name = header_module  # название модуля
    module_path = os.path.join(product_path, module_name)  # папка с модулем
    if os.path.exists(module_path):
        pass
    else:
        os.mkdir(module_path)  # создание папки с названием модуля (в папке с названием продукта)

    """element_folder"""
    element_name = header_module_element  # название элемента
    element_path = os.path.join(module_path, element_name)  # папка с элементом
    if os.path.exists(element_path):
        pass
    else:
        os.mkdir(element_path)  # создание папки с названием элемента (в папке с названием модуля)
    os.chdir(element_path)  # обращение к пути

    """collection"""
    driver.implicitly_wait(module_time)  # ожидание элемента
    search = driver.find_element(By.XPATH, xpath)  # поиск элемента, по методу XPATH
    search.click()  # нажатие
    time.sleep(screenshot_time)  # таймаут 1 секунда
    driver.save_screenshot(title_element + '.png')  # скриншот
    search = driver.page_source  # сбор данных
    with open(title_element + '.txt', 'w', encoding="utf-8") as f:  # создание файла, для хранения собранных данных
        soup = BeautifulSoup(search, 'html.parser')  # обработка парсером
        f.write(soup.get_text(' ', strip=True))  # извлечение и запись текста


def response_xpath(xpath, header_module,  # переход на элемент и ввод данных
                   header_module_element,  # пример ("//*[@class='navigation-panel']//*[@class='ng-star-inserted'][1]",
                   title_window):  # 'main_module', 'organization', 'ввод текста')

    """project_folder"""
    product_path = os.path.join(main_path, product_name)
    if os.path.exists(product_path):
        pass
    else:
        os.mkdir(product_path)

    """module_folder"""
    module_name = header_module
    module_path = os.path.join(product_path, module_name)
    if os.path.exists(module_path):
        pass
    else:
        os.mkdir(module_path)

    """element_folder"""
    element_name = header_module_element
    element_path = os.path.join(module_path, element_name)
    if os.path.exists(element_path):
        pass
    else:
        os.mkdir(element_path)
    os.chdir(element_path)

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
