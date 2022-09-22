def click_xpath(xpath):  # переход на элемент и нажатие

    """Click"""
    driver.implicitly_wait(module_time)
    search = driver.find_element(By.XPATH, xpath)
    search.click()  # нажатие
