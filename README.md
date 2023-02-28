Parsing
=========================================================================================================================================================================
| Selenium                                                  | Description                                                                                               |
| ----------------------------------------------------------| ----------------------------------------------------------------------------------------------------------|
| [default.py](parsing/default.py)                          | Пример                                                                                                    |
| [artifact.py](parsing/artifact.py)                        | Переход на страницу и сбор данных, сравнивая текст, в случае если найден артефакт, он записывается в файл |
| [request_xpath.py](parsing/request_xpath.py)              | Переход на страницу и сбор данных                                                                         |
| [response_xpath.py](parsing/response_xpath.py)            | Переход на элемент и ввод данных                                                                          |
| [click_xpath.py](parsing/click_xpath.py)                  | Переход на элемент и нажатие                                                                              |

Features
=========================================================================================================================================================================
| Other                                                     | Description                                                                                               |
| ----------------------------------------------------------| ----------------------------------------------------------------------------------------------------------|
| [ocr.py](features/ocr.py)                                 | считывает текст из изображения                                                                            |
| [playwright_page.py](features/playwright_page.py)         | пример работы playwright                                                                                  |
| [request_page.py](features/request_page.py)               | ищет файл toc.json(ищет все id): делает выгрузку текста и осуществляет проверку url                       |
| [spell_checker.py](features/spell_checker.py)             | проверка орфографии, поддерживает многоязычность                                                          |
| [morphological.py](features/morphological.py)             | проверка орфографии, поддерживает многоязычность                                                          |

Other
=========================================================================================================================================================================
| Other                                                     | Description                                                                                               |
| ----------------------------------------------------------| ----------------------------------------------------------------------------------------------------------|
| [py_in_exe.py](Other/py_in_exe.py)                        | конвертация из .py в .exe                                                                                 |
| [ui_in_py.py](Other/ui_in_py.py)                          | конвертация из .ui в .py                                                                                  |
| [req.py](Other/req.py)                                    | Выгрузка в requirements.txt                                                                               |
| [txt_in_xlsx.py](Other/txt_in_xlsx.py)                    | конвертация из .txt в .xlsx                                                                               |
| [link_extractor.py](Other/link_extractor.py)              | проверка url                                                                                              |
