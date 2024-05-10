from playwright.sync_api import Page


def test_first(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_element = page.get_by_role('link', name='Form Authentication')
    search_element.click()
    user_input = page.get_by_label('Username')
    user_input.fill('Some_user')
    password_input = page.get_by_label('Password')
    password_input.fill('Pass1234')
    button_login = page.get_by_role('button', name='Login')
    button_login.click()
