# from utility.generic import Generic
# from utility.excel_reader import read_locators
# from utility.config import Config
#
#
# locators = read_locators(Config.login_sheet)
#
# class Login(Generic):
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.locators = locators
#         super().__init__(driver)
#
#     def click_login_link(self):
#         self.click_element(self.locators["lnk_signin"])
#
#     def enter_phone_number(self, number):
#         self.enter_text(self.locators["txt_mobile_number"], value=number)
#
#     def click_continue(self):
#         self.click_element(self.locators["btn_continue"])
#
#     def give_otp(self):
#         pass
#
#     def validation(self):
#         text = self.get_text(self.locators["validation"])
#         wish = "welcome"
#         assert wish.lower() in text.lower()
