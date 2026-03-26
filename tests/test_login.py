import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from utils.config import BASE_URL

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("invalid", "wrong")
])
def test_login(username, password):
    driver = get_driver()
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(username, password)

    if username == "standard_user":
        assert "inventory" in driver.current_url
    else:
        assert login.is_error()

    driver.quit()