from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    #открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()  # поставим фокус на поле Email

    # для каждой буквы в данной строке мы делаем
    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=300)  # на каждой итерации цикла передаем сюда букву, которую будем печатать

    page.keyboard.press("ControlOrMeta+A") #выделим введенный текст
    page.wait_for_timeout(5000) #Ждем 5 сек для наглядности результата
