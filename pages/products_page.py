import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductsPage(BasePage):

    ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    SORT = (By.CLASS_NAME, "product_sort_container")
    MENU = (By.ID, "react-burger-menu-btn")
    RESET = (By.ID, "reset_sidebar_link")

    def select_random_products(self, count=4):
        items = self.find_all(self.ITEMS)
        selected = random.sample(items, count)

        data = []
        for item in selected:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            item.find_element(By.TAG_NAME, "button").click()
            data.append((name, price))

        return data

    def get_cart_count(self):
        return self.find(self.CART_COUNT).text

    def go_to_cart(self):
        self.click(self.CART_ICON)


    def sort_products(self, value):
        dropdown = Select(self.find(self.SORT))
        dropdown.select_by_visible_text(value)


    def reset_app(self):
        self.click(self.MENU)

        time.sleep(1)  # allow menu animation

        wait = WebDriverWait(self.driver, 10)
        reset_btn = wait.until(
            EC.element_to_be_clickable(self.RESET)
        )

        reset_btn.click()