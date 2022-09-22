def request_xpath(xpath, title_element):  # ("//*[@class='navigation-panel']", 'main_module')
    
    """Collection"""
    driver.implicitly_wait(module_time)  # ожидание элемента
    search = driver.find_element(By.XPATH, xpath)  # поиск элемента, по методу XPATH
    search.click()  # нажатие
    time.sleep(screenshot_time)  # таймаут 1 секунда
    driver.save_screenshot(title_element + '.png')  # скриншот
    search = driver.page_source  # сбор данных
    soup = BeautifulSoup(search, 'html.parser')  # обработка парсером
    get = [str.lower(text) for text in soup.stripped_strings]  # преобразование текста в нижний регистр
    with open(artifact_path, "r") as file:  # открытие файла с артефактами
        for line in file:   # цикл текста с артефактами
            for el in get:  # цикл обработки текста
                if line.strip() in el:  # поиск совпадений
                    with open(title_element + '.txt', 'a') as f:  # открытие файла
                        f.write(el + '\n')  # запись совпадений
