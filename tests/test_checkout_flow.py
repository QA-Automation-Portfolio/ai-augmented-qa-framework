
import os, pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_pages import CartPage, CheckoutStepOne, CheckoutStepTwo, CheckoutComplete

load_dotenv()
USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
FIRST = os.getenv("FIRST_NAME", "Alex")
LAST = os.getenv("LAST_NAME", "QA")
POSTAL = os.getenv("POSTAL_CODE", "00000")

pytestmark = pytest.mark.e2e

def test_successful_checkout(page, base_url):
    lp = LoginPage(page)
    lp.open(base_url)
    lp.login(USERNAME, PASSWORD)

    inv = InventoryPage(page)
    inv.expect_loaded()
    inv.add_first_n_products(2)
    inv.open_cart()

    cart = CartPage(page)
    cart.checkout()

    step1 = CheckoutStepOne(page)
    step1.fill(FIRST, LAST, POSTAL)

    step2 = CheckoutStepTwo(page)
    step2.finish()

    complete = CheckoutComplete(page)
    complete.expect_success()
