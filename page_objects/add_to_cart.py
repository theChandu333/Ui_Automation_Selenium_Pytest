from utility.generic import Generic
from utility.excel_reader import read_locators
from utility.config import Config


class Add_to_cart(Generic):

    def __init__(self, _driver):
        self.driver = _driver
        self.locators = read_locators(Config.add_to_cart_sheet)
        super().__init__(_driver)

    def enter_product_name(self, product):
        self.enter_text(self.locators["txt_search"], value=product)

    def click_enter_button(self):
        self.click_enter()

    def select_product(self):
        self.click_element(self.locators["lnk_select_product"])

    def click_add_to_basket(self):
        self.click_element(self.locators["lnk_add_To_basket"])

    def click_checkout(self):
        self.click_element(self.locators["lnk_checkout"])
        val = self.get_text(self.locators["validate"])
        assert val == "Sign up or Sign in"
