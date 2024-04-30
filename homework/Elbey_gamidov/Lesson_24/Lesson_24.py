import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_task_1(driver):
    driver.get('https://www.demoblaze.com/index.html')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h4.card-title a[href="prod.html?idp_=1"]')))
    product = driver.find_element(By.CSS_SELECTOR, 'h4.card-title a[href="prod.html?idp_=1"]')

    new_tab = ActionChains(driver)
    new_tab.key_down(Keys.CONTROL).click(product).perform()
    driver.switch_to.window(driver.window_handles[1])
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')))
    button = driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(1)"]')
    button.click()
    button.send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    # alert = Alert(driver)
    # alert.accept()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h4.card-title a[href="prod.html?idp_=1"]')))
    driver.find_element(By.ID, 'cartur').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr.success td:nth-child(2)')))
    expect_phone = driver.find_element(By.CSS_SELECTOR, 'tr.success td:nth-child(2)')
    assert expect_phone.text == 'Samsung galaxy s6'


def test_task_2(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-image-photo[alt="Push It Messenger Bag"]')))
    first_element = driver.find_element(By.CSS_SELECTOR, '.product-image-photo[alt="Push It Messenger Bag"]')
    actions = ActionChains(driver)
    actions.move_to_element(first_element)
    actions.perform()
    compare = driver.find_element(By.XPATH, "(//a[@class='action tocompare' "
                                            "and @title='Add to Compare' and @aria-label='Add to Compare'])[1]")
    actions.click(compare)
    actions.perform()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="Remove This Item"]')))
    product = driver.find_element(By.XPATH, "//a[text()='Push It Messenger Bag']")
    assert product.text == "Push It Messenger Bag"
