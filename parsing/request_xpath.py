def request_xpath(xpath, title_element):  # ("//*[@class='navigation-panel']", 'main_module')
    
    """Collection"""
    driver.implicitly_wait(module_time)  # ожидание элемента
    search = driver.find_element(By.XPATH, xpath)  # поиск элемента, по методу XPATH
    search.click()  # нажатие
    time.sleep(screenshot_time)  # таймаут 1 секунда
    driver.save_screenshot(title_element + '.png')  # скриншот
    search = driver.page_source  # сбор данных
    with open(title_element + '.txt', 'a') as f:  # открытие файла
      soup = BeautifulSoup(search, 'html.parser')  # обработка парсером
      f.write(soup.get_text('\n', strip=True))  # извлечение и запись текста
