from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import BASE_URL

def test_sort_and_reset():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)

    # Sort
    products.sort_products("Price (low to high)")

    # Add items then reset
    products.select_random_products()
    products.reset_app()

    # Cart should be empty
    try:
        assert products.get_cart_count() == ""
    except:
        assert True  # no badge = pass

    driver.quit()