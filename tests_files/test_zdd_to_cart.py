import pytest
from page_objects.add_to_cart import Add_to_cart
from utility.excel_reader import read_testdata
from utility.config import Config

data = read_testdata(Config.add_to_cart_sheet)


@pytest.mark.parametrize("product, nothing", data)
def test_add_to_cart(product, nothing, ini_driver):
    driver = ini_driver
    obj = Add_to_cart(driver)
    obj.enter_product_name(product)
    obj.click_enter_button()
    obj.select_product()
    obj.click_add_to_basket()
    obj.click_checkout()
