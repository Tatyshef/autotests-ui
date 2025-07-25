from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser =playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Находим поле  email/username/password и заполняем его значением
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    #Находим и нажимаем кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_timeout(20000)

    # Находим и проверяем,что на странице дашборды отображается заголовок Dashboard
    dashbord_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashbord_title).to_be_visible()
    expect(dashbord_title).to_have_text('Dashboard')








