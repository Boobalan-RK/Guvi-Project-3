from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    SUCCESS = (By.CLASS_NAME, "complete-header")

    def fill_details(self):
        self.type(self.FIRST, "Test")
        self.type(self.LAST, "User")
        self.type(self.ZIP, "600001")
        self.click(self.CONTINUE)

    def finish(self):
        self.click(self.FINISH)

    def is_success(self):
        return self.find(self.SUCCESS).is_displayed()