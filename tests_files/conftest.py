import pytest
from selenium import webdriver
from utility.config import Config



@pytest.fixture()
def ini_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-notifications")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=option)
    driver.get(Config.url)
    driver.maximize_window()
    yield driver
    driver.quit()

