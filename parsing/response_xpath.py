def response_xpath(xpath, title_window):  # ("//*[@class='navigation-panel']", 'ввод текста')

    """response"""
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.clear()  # очистка строки
    search.send_keys(title_window)  # ввод данных
