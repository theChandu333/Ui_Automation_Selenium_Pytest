from utility.generic import Generic
from utility.excel_reader import read_locators
from utility.config import Config


class Search_Products(Generic):

    def __init__(self, _driver):
        self.driver = _driver
        self.locators = read_locators(Config.search_product_sheet)
        super().__init__(_driver)

    def enter_product_name(self, product):
        self.enter_text(self.locators["txt_search"], value=product)

    def select_product_from_list(self):
        self.click_element(self.locators["lnk_select_product"])

    def get_no_products_found(self):
        products = self.get_elements(self.locators["products"])
        print(len(products))

    def get_product_names(self):
        product_name = self.get_elements(self.locators["product_names"])
        names = [name.text for name in product_name]
        print(names)

    def get_product_prices(self):
        product_price = self.get_elements(self.locators["product_prices"])
        prices = [price.text for price in product_price]
        print(prices)

    def get_available_prices(self):
        product_name = self.get_elements(self.locators["product_names"])
        names = [name.text for name in product_name]
        product_price = self.get_elements(self.locators["product_prices"])
        prices = [price.text for price in product_price]
        d = {product: price for product, price in zip(names, prices)}
        print(d)

    # def search_products(self, product_name):
    #     # self.enter_text(self.locators["txt_search"])
    #     # self.click_element(self.locators["lnk_select_product"])
    #     # products = self.get_elements(self.locators["products"])
    #     # product_name = self.get_elements(self.locators["product_names"])
    #     product_price = self.get_elements(self.locators["product_prices"])
    #     d = {product: price for product, price in zip(product_name, product_price)}
    #     return f"{len(products)} products found \n", d

