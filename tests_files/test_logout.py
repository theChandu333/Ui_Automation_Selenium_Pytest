# import pytest
# from utility.config import Config
# from utility.excel_reader import read_testdata
# from page_objects.login import Login
# from page_objects.logout import Logout
#
# data = read_testdata(Config.login_sheet)
#
#
# @pytest.mark.parametrize("ph_num, nothing", data)
# def test_login(ph_num, nothing, ini_driver):
#     obj = Login(Config.login_sheet)
#     obj.click_login_link()
#     # obj.enter_phone_number(ph_num)
#     obj.click_continue()
#     # obj.give_otp()
#     obj.validation()
#
# def test_logout(depends = ['test_login']):
#     ob = Logout(Config.logout_sheet)
#     ob.click_on_profile()
#     ob.click_logout()
