import pytest
from page_objects.search_products import Search_Products
from utility.excel_reader import read_testdata
from utility.config import Config

data = read_testdata(Config.search_product_sheet)

@pytest.mark.parametrize("search, nothing", data)
def test_search_products(search, nothing, ini_driver):
    _driver = ini_driver
    obj = Search_Products(_driver)
    obj.enter_product_name(search)
    obj.select_product_from_list()
    obj.get_no_products_found()
    obj.get_product_names()
    obj.get_product_prices()
    obj.get_available_prices()
