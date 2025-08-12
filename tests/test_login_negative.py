
import pytest
from pages.login_page import LoginPage

pytestmark = [pytest.mark.smoke, pytest.mark.e2e]

def test_login_locked_out_user(page, base_url):
    lp = LoginPage(page)
    lp.open(base_url)
    lp.login("locked_out_user", "secret_sauce")
    lp.expect_error()
