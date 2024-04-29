from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    chrome_driver.maximize_window()
    yield chrome_driver


def test_task_1(driver):
    driver.get(' https://www.qa-practice.com/elements/input/simple')
    some_text = 'some_text'
    text_string = driver.find_element(By.ID, 'id_text_string')
    text_string.send_keys(some_text)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, 'result-text')
    print(result_text)


def test_task_2(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    name_input = driver.find_element(By.ID, 'firstName')
    name_input.click()
    name_input.send_keys('Some_name')

    last_name_input = driver.find_element(By.ID, 'lastName')
    last_name_input.click()
    last_name_input.send_keys('Some_last_name')

    email_input = driver.find_element(By.ID, 'userEmail')
    email_input.click()
    email_input.send_keys('megaepicccc@gmail.com')

    radio_button = driver.find_element(By.CSS_SELECTOR, 'label.custom-control-label[for="gender-radio-1"]')
    radio_button.click()

    phone_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Mobile Number"]')
    phone_input.click()
    phone_input.send_keys('7777777777')

    date_input = driver.find_element(By.ID, 'dateOfBirthInput')
    date_input.click()
    month_dropdown = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    select = Select(month_dropdown)
    select.select_by_value('10')
    year_dropdown = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    select = Select(year_dropdown)
    select.select_by_value('1994')
    day_input = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--023')
    day_input.click()

    subject_input = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__value-container')
    subject_input.click()
    hide_input = driver.find_element(By.ID, 'subjectsInput')
    hide_input.click()
    hide_input.send_keys('E')
    hide_input.send_keys(Keys.ENTER)

    check_box = driver.find_element(By.CSS_SELECTOR, 'label.custom-control-label[for="hobbies-checkbox-3"]')
    check_box.click()

    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.click()
    current_address.send_keys('Omsk city, Russia')

    state = driver.find_element(By.ID, 'state')
    state.click()
    hide_state = driver.find_element(By.ID, 'react-select-3-input')
    hide_state.send_keys('N')
    hide_state.send_keys(Keys.ENTER)

    city = driver.find_element(By.ID, 'city')
    city.click()
    hide_city = driver.find_element(By.ID, 'react-select-4-input')
    hide_city.send_keys('D')
    hide_city.send_keys(Keys.ENTER)

    tbody = driver.find_elements(By.TAG_NAME, 'tr')
    for tr in tbody:
        print(tr.text)

    close_modal = driver.find_element(By.ID, 'closeLargeModal')
    close_modal.click()


def test_task_3_subtask1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_value('1')
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.ID, 'result')))
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'Python'


def test_task_3_subtask2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.TAG_NAME, 'button')
    start_button.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id="finish"]')))
    assert 'Hello World!' in element.text
