from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle') #ждем полной загрузки страницы

    # выполняем  JS-код для замены текста заголовка

    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'NEW TEXT'
        """
    )

    page.wait_for_timeout(5000) #ждем 5 сек для наглядности