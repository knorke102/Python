import time
from playwright.sync_api import sync_playwright


def main_page(link):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # headless=False
        context = browser.new_context()
        page = context.new_page()

        main_link = link
        page.goto(main_link)
        time.sleep(2)

        for i in range(1, 100):
            element = page.query_selector_all('//*[@class="btn-group btn-group-sm"][{}]'.format(i))
            for el in element:
                el.click()
                print(page.url)

        page.close()
        context.close()
        browser.close()


if __name__ == "__main__":
    main_page(link='https://example.ru/')
