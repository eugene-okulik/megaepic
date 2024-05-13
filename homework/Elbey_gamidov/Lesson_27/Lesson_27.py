from playwright.sync_api import Page, expect, BrowserContext, Dialog
from time import sleep


def test_task_1(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()
    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    click_button = page.locator('.a-button')
    click_button.click()
    expected_element = page.locator('.result-text')
    expect(expected_element).to_be_visible()


def test_task_2(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.locator('#new-page-button')
    with context.expect_page() as new_page:
        click_button.click()
        page_2 = new_page.value
        result_text = page_2.locator('#result-text')
        expect(result_text).to_have_text('I am a new page in a new tab')
        click_btn = page.locator('#new-page-button')
        expect(click_btn).to_be_enabled()


def test_task_3(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', wait_until='domcontentloaded')
    red_button = page.locator('#colorChange')
    expect(red_button).to_have_css('color', 'rgb(220, 53, 69)', timeout=7000)
    red_button.click()
