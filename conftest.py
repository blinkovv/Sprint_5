import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    return driver
    driver.quit()