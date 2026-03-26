from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL

def test_full_flow():
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)

    # Cart icon visible
    assert products.find(products.CART_ICON).is_displayed()

    # Random products
    selected = products.select_random_products()
    assert len(selected) == 4

    # Cart validation
    assert products.get_cart_count() == "4"

    products.go_to_cart()

    cart = CartPage(driver)
    assert len(cart.get_items()) == 4

    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_details()
    checkout.finish()

    assert checkout.is_success()

    driver.quit()