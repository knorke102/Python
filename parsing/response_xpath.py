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
