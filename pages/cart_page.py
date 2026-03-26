from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT = (By.ID, "checkout")

    def get_items(self):
        return self.find_all(self.ITEMS)

    def checkout(self):
        self.click(self.CHECKOUT)