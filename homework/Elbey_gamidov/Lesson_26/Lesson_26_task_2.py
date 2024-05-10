from playwright.sync_api import Page


def test_second(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', wait_until='domcontentloaded')
    name = page.get_by_placeholder('First Name')
    name.fill('Andrew')
    last_name = page.get_by_placeholder('Last Name')
    last_name.fill('Woolf')

    email = page.get_by_placeholder('name@example.com')
    email.fill('example@gmail.com')

    radio_button = page.locator('label.custom-control-label[for="gender-radio-1"]')
    radio_button.check()

    phone = page.get_by_placeholder('Mobile Number')
    phone.fill('7777777777')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.click()
    mouth_dropdown = page.locator('.react-datepicker__month-select')
    mouth_dropdown.click()
    mouth_dropdown.select_option(value='10')
    year_dropdown = page.locator('.react-datepicker__year-select')
    year_dropdown.click()
    year_dropdown.select_option(value='1994')
    day = page.locator('.react-datepicker__day--023')
    day.click()

    subject = page.locator('.subjects-auto-complete__value-container')
    subject.click()
    subject_hide = page.locator('#subjectsInput')
    subject_hide.fill('english')
    subject_hide.press('Enter')

    check_box = page.locator('label.custom-control-label[for="hobbies-checkbox-3"]')
    check_box.check()

    current_address = page.locator('#currentAddress')
    current_address.click()
    current_address.fill('Omsk city, Russia')

    select_state = page.locator('#state')
    select_state.click()
    hide_state = page.locator('#react-select-3-input')
    hide_state.fill('N')
    hide_state.press('Enter')
    select_city = page.locator('#city')
    select_city.click()
    hide_city = page.locator('#react-select-4-input')
    hide_city.fill('D')
    hide_city.press('Enter')

    button_submit = page.get_by_role('button', name='Submit')
    button_submit.click()
