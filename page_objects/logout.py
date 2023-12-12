# from utility.config import Config
# from utility.excel_reader import read_locators
# from utility.generic import Generic
#
# locators = read_locators(Config.logout_sheet)
#
# class Logout(Generic):
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.locators = locators
#         super().__init__(driver)
#
#     def click_on_profile(self):
#         self.click_element(self.locators["btn_profile"])
#
#     def click_logout(self):
#         self.click_element(self.locators["btn_logout"])
