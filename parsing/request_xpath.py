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
    time.sleep(screenshot_time)  # таймаут
    driver.save_screenshot(title_element + '.png')  # скриншот
    search = driver.page_source  # сбор данных
    with open(title_element + '.txt', "w", encoding="utf-8") as f:  # создание файла, для хранения собранных данных
        f.write(search)  # запись данных
