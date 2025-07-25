from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser  = playwright.chromium.launch(headless=False)
    page = browser.new_page()

   #Переходим на страницу авторизации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

   #Проверяем наличие элемента email
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    #Проверяем наличие элемента password
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

   #Проверяем наличие элемента Login
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    #Нажимаем на ссылку Регистрация, редирект на страницу регистрации
    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()

    #Проверяем наличие элементов emai/password/registration
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()

    page.wait_for_timeout(5000)








