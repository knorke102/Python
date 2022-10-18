def get_text(x, y, button, pressed):
    global count_click, driver, toaster

    if pressed or button != mouse.Button.middle:
        return

    ui.btn_stop.setEnabled(False)

    search = driver.page_source
    soup = BeautifulSoup(search, 'html.parser')
    get = set([str.lower(text) for text in soup.stripped_strings])

    with open(artifacts_path_suffix, encoding='utf-8', mode='r') as file:
        output = {}
        for line in file:
            for el in get:
                if el == "":
                    continue
                line = line.strip()
                for i in ['.', '+', '*', '?', '^', '$', '(', ')', '[', ']', '{', '}', '|']:
                    line = line.replace(i, '\\{}'.format(i))
                for i in list(string.punctuation):
                    el = el.replace(i, '')
                reg = re.compile(r"\s{2,}")
                el = el.replace("\n", " ").replace("\t", " ")
                el = re.sub(reg, " ", el)
                el = el.lstrip()

                if re.compile(r'\b{}\b'.format(line.lower())).search(el):
                    value = output.get(el, None)
                    if value is not None:
                        output[el] += [line.strip()]
                    else:
                        output[el] = [line.strip()]

                    product_name = 'report'
                    product_path = os.path.join(main_path, product_name)
                    if not os.path.exists(product_path):
                        os.mkdir(product_path)
                    os.chdir(product_path)

        if len(output) == 0:
            ui.btn_stop.setEnabled(True)
            return

        count_click += 1
        book = xlsxwriter.Workbook(str(count_click) + '.xlsx')
        sheet = book.add_worksheet()
        red = book.add_format({"bold": True, "color": "red"})
        r = 0
        for key, value in output.items():
            sheet.write_string(r, 0, ", ".join(set(value)))
            array = []
            for k in key.split(' '):
                for v in value:
                    if k == v:
                        array += [red]
                        break
                array += [k, " "]
            sheet.write_rich_string(r, 1, *array)
            sheet.write_string(r, 2, driver.current_url)
            r += 1
        book.close()

        driver.save_screenshot(str(count_click) + '.png')

    toaster.show_toast("Notification", "Artifacts found", icon_path=ico_path, duration=2)

    ui.btn_stop.setEnabled(True)
