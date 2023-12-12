from utility.wait_conditions import wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Generic:

    def __init__(self, _driver):
        self.driver = _driver

    @wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @wait
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def click_enter(self):
        a = ActionChains(self.driver)
        a.send_keys(Keys.ENTER).perform()
